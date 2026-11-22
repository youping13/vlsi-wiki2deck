#!/usr/bin/env python3
"""wiki2deck — 用 LLM Wiki 產生教學 HTML 簡報的「檢查關卡＋渲染器」。

AI 節點（evidence / outline / slides）由 agent 依 pipeline/prompts/ 產生檔案；
這支腳本只負責「可重現的檢查」與「渲染」，不呼叫任何模型，也沒有外部相依套件。

所有東西都掛在 taxonomy.json 的分類樹上（VLSI → mixed-signal → basic / sar-basics / monotonic …）：
  raw/<節點>/<id>.<副檔名> ＋ raw/<節點>/<id>.md（來源卡）
  wiki/<節點>/<slug>.md（概念頁）、wiki/<節點>/sources/<id>.md（每篇來源的論述）
  decks/<節點>/<slug>/（一份簡報）

用法：python pipeline/wiki2deck.py <cmd> [decks/<節點>/<slug>]
  lint | retrieve | coverage | evidence | approve | faithful | render | all <deck>
  inbox  列出亂丟在最外層或 raw/ 的檔案，建議類型與 id（分類節點一律先問 Percy）
  hub    產生根目錄 index.html（大目錄）
  build  lint → 每份簡報 all → hub（一次全部重建）
"""
from __future__ import annotations

import datetime as _dt
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
FIG_DIR = ROOT / "assets" / "figures"
RAW = ROOT / "raw"
TAXONOMY = ROOT / "taxonomy.json"
WIKI_SPECIAL = {"index.md", "log.md", "figures.md"}
TEMPLATE = ROOT / "template" / "deck.html"

# ---- 門檻（要改請寫進本機的 docs/private/reflection.md）----
MIN_HITS_PER_GOAL = 2          # coverage：每個目標至少命中幾頁
MIN_SOURCES_PER_GOAL = 2       # coverage：命中頁面合計至少幾個不同來源
MIN_CARDS_PER_GOAL = 2         # evidence：每個目標至少幾張卡
MAX_BULLETS = 5                # render：每頁最多 bullet 數
MAX_BULLET_CHARS = 70          # render：每個 bullet 最多字數（去掉引用標記）
CITE_RE = re.compile(r"\[(c\d+(?:\s*,\s*c\d+)*)\]")
NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")


# ---------------------------------------------------------------- utils
def norm(s: str) -> str:
    """比對用：去掉 markdown 強調、合併空白。"""
    s = s.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")


def norm_num(s: str) -> str:
    return s.translate(SUP).replace(",", "")


def numbers(text: str) -> list[str]:
    """抽出數字；LaTeX 指令（\\frac、\\mathrm…）與 {,} 先清掉，避免把指令當內容。"""
    t = CITE_RE.sub("", text).replace("{,}", ",")
    t = re.sub(r"\\[a-zA-Z]+", " ", t)
    return NUM_RE.findall(t.translate(SUP))


MATH_RE = re.compile(r"\$[^$]+\$")


def parse_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        body = m.group(2)
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                v = v.strip()
                if v.startswith("[") and v.endswith("]"):
                    v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
                meta[k.strip()] = v
    return {"meta": meta, "body": body, "text": text}


def taxonomy_nodes() -> dict[str, dict]:
    """{'mixed-signal/basic': node, …}；根節點的路徑是 ''。"""
    out = {}

    def walk(node, path):
        out[path] = dict(node, path=path)
        for ch in node.get("children", []):
            walk(ch, f"{path}/{ch['id']}" if path else ch["id"])
    walk(load_json(TAXONOMY), "")
    return out


def is_source(key: str) -> bool:
    return "/sources/" in f"/{key}"


def slug_of(key: str) -> str:
    return key.rsplit("/", 1)[-1]


def node_of_key(key: str) -> str:
    """wiki 頁面 key（相對 wiki/、不含 .md）所在的分類節點。"""
    parts = key.split("/")[:-1]
    if parts and parts[-1] == "sources":
        parts = parts[:-1]
    return "/".join(parts)


def wiki_pages() -> dict[str, dict]:
    pages = {}
    for p in sorted(WIKI.rglob("*.md")):
        if p.parent == WIKI and p.name in WIKI_SPECIAL:
            continue
        pages[p.relative_to(WIKI).with_suffix("").as_posix()] = parse_page(p)
    return pages


def card_paths() -> dict[str, Path]:
    """來源卡：raw/ 底下除了 README.md 以外的所有 .md，id = 檔名。"""
    return {p.stem: p for p in sorted(RAW.rglob("*.md")) if p.name != "README.md"}


def page_sources(key: str, page: dict) -> set[str]:
    if is_source(key):
        return {slug_of(key)}
    src = page["meta"].get("sources", [])
    return set(src if isinstance(src, list) else [src])


class Report:
    def __init__(self, deck: Path | None, step: str):
        self.deck, self.step, self.lines, self.ok = deck, step, [], True

    def fail(self, msg: str):
        self.ok = False
        self.lines.append(f"- ❌ {msg}")

    def info(self, msg: str):
        self.lines.append(f"- {msg}")

    def finish(self) -> bool:
        status = "PASS" if self.ok else "FAIL"
        head = f"### [{_dt.datetime.now().astimezone():%Y-%m-%d %H:%M:%S %z}] {self.step} — {status}"
        out = "\n".join([head, *self.lines, ""])
        print(out)
        if self.deck is not None:
            with open(self.deck / "check-report.md", "a", encoding="utf-8") as f:
                f.write(out + "\n")
        return self.ok


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- figures
def figure_registry() -> dict[str, dict]:
    reg = {}
    p = WIKI / "figures.md"
    if not p.exists():
        return reg
    for line in p.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[0] not in ("id", "---") and not cells[0].startswith("-"):
            reg[cells[0]] = {"source": cells[1], "label": cells[2], "desc": cells[3]}
    return reg


def source_citation(sid: str) -> str:
    pg = parse_page(card_paths()[sid])["meta"]
    first = str(pg.get("author", sid)).split(",")[0].split("（")[0].strip()
    venue = str(pg.get("venue", pg.get("year", ""))).strip()
    return f"{first} et al., {venue}" if "," in str(pg.get("author", "")) else f"{first}, {venue}"


def card_sources(card: dict, pages: dict | None = None) -> set[str]:
    """卡片本身的 (src:)；沒有的話（例如縮排的子項目），往上找最近一行有 (src:) 的父行。"""
    own = {s.strip() for m in re.finditer(r"\(src: ([^)]+)\)", card["wiki_text"]) for s in m.group(1).split(",")}
    if own or pages is None or card.get("page") not in pages:
        return own
    lines = pages[card["page"]]["body"].splitlines()
    key = card["wiki_text"][:20]
    for i, l in enumerate(lines):
        if key in l:
            for j in range(i - 1, -1, -1):
                m = re.search(r"\(src: ([^)]+)\)", lines[j])
                if m:
                    return {s.strip() for s in m.group(1).split(",")}
                if lines[j].startswith("## "):
                    break
    return own


# ---------------------------------------------------------------- lint
def cmd_lint(_deck=None) -> bool:
    r = Report(None, "lint")
    pages = wiki_pages()
    nodes = taxonomy_nodes()
    src_ids = {slug_of(k) for k in pages if is_source(k)}
    slugs = [slug_of(k) for k in pages]
    for s in {x for x in slugs if slugs.count(x) > 1}:
        r.fail(f"slug「{s}」重複，[[連結]] 會分不清")
    slugs = set(slugs)
    need = ["## 一句話", "## 原理", "## 關鍵數字", "## 常見誤解 / 衝突", "## 相關"]
    for key, pg in pages.items():
        node = pg["meta"].get("node")
        if node not in nodes:
            r.fail(f"{key}: node「{node}」不在 taxonomy.json（新增分類要先問 Percy）")
        elif node != node_of_key(key):
            r.fail(f"{key}: node 是 {node}，但檔案放在 wiki/{node_of_key(key)}/")
        if is_source(key) and "## 論述" not in pg["body"]:
            r.fail(f"{key}: 來源頁缺少「## 論述」（每篇都要有單純的論述）")
        if not is_source(key):
            for sec in need:
                if sec not in pg["body"]:
                    r.fail(f"{key}: 缺少段落 {sec}")
            for s in page_sources(key, pg):
                if s not in src_ids:
                    r.fail(f"{key}: front matter 的來源 '{s}' 沒有來源頁 wiki/<節點>/sources/{s}.md")
            num_sec = pg["body"].split("## 關鍵數字", 1)[-1].split("\n## ", 1)[0]
            for line in num_sec.splitlines():
                if line.strip().startswith("- ") and NUM_RE.search(line) and "(src:" not in line \
                        and "（計算）" not in line and not line.startswith("  "):
                    r.fail(f"{key}: 數字沒標出處 → {line.strip()[:50]}")
        for m in re.finditer(r"\(src: ([^)]+)\)", pg["body"]):
            for s in [x.strip() for x in m.group(1).split(",")]:
                if s not in src_ids:
                    r.fail(f"{key}: (src: {s}) 不存在")
        for m in re.finditer(r"\[\[([^\]]+)\]\]", pg["body"]):
            if m.group(1) not in slugs:
                r.fail(f"{key}: 連結 [[{m.group(1)}]] 指向不存在的頁")
    # 數字溯源（2026-11-21 反思後新增）：concept 頁裡標了 (src: X) 的數字，必須出現在來源卡 raw/<節點>/X.md
    # 來源卡「## 與其他來源的關係」之後是次要/有爭議的數字，只能被 concept 頁的「衝突」段落引用
    raw_all, raw_main = {}, {}
    cards = card_paths()
    for p in cards.values():
        t = p.read_text(encoding="utf-8")
        raw_all[p.stem] = norm_num(norm(t))
        raw_main[p.stem] = norm_num(norm(t.split("## 與其他來源的關係", 1)[0]))
    for key, pg in pages.items():
        if is_source(key):
            continue
        section = ""
        for line in pg["body"].splitlines():
            if line.startswith("## "):
                section = line
            if "(src:" not in line or "推論" in line or "（計算）" in line:
                continue  # （計算）的數字由 docs/calc-check.py 驗算，不從來源卡比對
            # 每一段文字歸給它後面最近的 (src: …)
            for seg, ids_s in re.findall(r"(.*?)\(src: ([^)]+)\)", line):
                ids = [x.strip() for x in ids_s.split(",")]
                raw = raw_all if "衝突" in section else raw_main
                evidence = " ".join(raw.get(i, "") for i in ids)
                for n in NUM_RE.findall(seg):
                    if norm_num(n) not in evidence:
                        r.fail(f"{key}: 數字 {n} 不在來源卡 {'+'.join(ids)} → {seg.strip()[:40]}")
    # raw 整理狀態：來源卡放在 raw/<節點>/，原檔和來源卡同名同資料夾；每張來源卡都要有 wiki 來源頁
    for cid, cp in cards.items():
        cnode = parse_page(cp)["meta"].get("node")
        rel = cp.parent.relative_to(RAW).as_posix()
        if cnode not in nodes or cnode != rel:
            r.fail(f"raw/{rel}/{cp.name}: node「{cnode}」和所在資料夾不一致，或不在 taxonomy.json")
        if cid not in src_ids:
            r.fail(f"來源卡 {cid} 沒有 wiki 來源頁（要寫論述）")
        fpath = parse_page(cp)["meta"].get("file")
        if fpath and not (ROOT / str(fpath)).exists() and (ROOT / str(fpath)).parent.exists() \
                and any(x.suffix != ".md" for x in (ROOT / str(fpath)).parent.iterdir()):
            r.fail(f"{cp.relative_to(ROOT)} 的 file: {fpath} 不存在")  # 原檔不進 git，只在本機有原檔時檢查
    for f in sorted(RAW.rglob("*")):
        if f.is_file() and f.suffix != ".md" and f.parent != RAW and f.stem not in cards:
            r.fail(f"{f.relative_to(ROOT)} 沒有同名來源卡")
    stray = inbox_items()
    if stray:
        r.info(f"⚠ inbox 有 {len(stray)} 個未整理檔案 → 跑 `python pipeline/wiki2deck.py inbox`")
    for fid, fg in figure_registry().items():
        if not (FIG_DIR / f"{fid}.png").exists():
            r.fail(f"figures.md: {fid} 找不到圖檔 assets/figures/{fid}.png")
        if fg["source"] not in src_ids:
            r.fail(f"figures.md: {fid} 的來源 {fg['source']} 不存在")
    index = (WIKI / "index.md").read_text(encoding="utf-8")
    for key in pages:
        if slug_of(key) not in index:
            r.fail(f"index.md 沒列出 {key}")
    r.info(f"檢查 {len(pages)} 頁（{len(src_ids)} 個來源）")
    return r.finish()


# ---------------------------------------------------------------- retrieve / coverage
def parse_brief(deck: Path) -> list[dict]:
    goals = []
    for line in (deck / "brief.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- (g\d+) \| (.+?) \| (.+)$", line.strip())
        if m:
            goals.append({"id": m.group(1), "goal": m.group(2),
                          "keywords": [k.strip() for k in m.group(3).split(",") if k.strip()]})
    return goals


def cmd_retrieve(deck: Path) -> bool:
    r = Report(deck, "retrieve")
    pages = wiki_pages()
    out = {}
    for g in parse_brief(deck):
        scored = []
        for key, pg in pages.items():
            title = str(pg["meta"].get("title", ""))
            score = sum(pg["text"].count(k) + 3 * title.count(k) for k in g["keywords"])
            if score:
                scored.append((score, key))
        scored.sort(reverse=True)
        hits = [{"page": k, "score": s, "sources": sorted(page_sources(k, pages[k]))}
                for s, k in scored[:5]]
        out[g["id"]] = {"goal": g["goal"], "keywords": g["keywords"], "hits": hits}
        r.info(f"{g['id']} {g['goal']} → " + ", ".join(f"{h['page']}({h['score']})" for h in hits))
    (deck / "retrieval.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return r.finish()


def cmd_coverage(deck: Path) -> bool:
    r = Report(deck, "coverage gate")
    ret = load_json(deck / "retrieval.json")
    for gid, g in ret.items():
        hits = g["hits"]
        concepts = [h for h in hits if not is_source(h["page"])]
        srcs = set().union(*[set(h["sources"]) for h in hits]) if hits else set()
        if len(hits) < MIN_HITS_PER_GOAL or not concepts:
            r.fail(f"{gid}「{g['goal']}」命中不足（{len(hits)} 頁，concept {len(concepts)}）→ 停，回 wiki ingest")
        elif len(srcs) < MIN_SOURCES_PER_GOAL:
            r.fail(f"{gid}「{g['goal']}」只有 {len(srcs)} 個來源支持 → 停，回 wiki ingest")
        else:
            r.info(f"{gid} OK：{len(hits)} 頁、{len(srcs)} 個來源")
    return r.finish()


# ---------------------------------------------------------------- evidence
def load_cards(deck: Path) -> dict[str, dict]:
    return {c["id"]: c for c in load_json(deck / "evidence.json")["cards"]}


def cmd_evidence(deck: Path) -> bool:
    r = Report(deck, "evidence gate")
    pages = wiki_pages()
    goals = {g["id"] for g in parse_brief(deck)}
    raw = load_json(deck / "evidence.json")["cards"]
    seen, per_goal = set(), {g: 0 for g in goals}
    for c in raw:
        cid = c.get("id")
        if cid in seen:
            r.fail(f"{cid}: 卡片編號重複")
        seen.add(cid)
        if c.get("goal") not in goals:
            r.fail(f"{cid}: goal '{c.get('goal')}' 不在 brief 裡")
        else:
            per_goal[c["goal"]] += 1
        pg = pages.get(c.get("page", ""))
        if pg is None:
            r.fail(f"{cid}: 頁面 {c.get('page')} 不存在")
            continue
        if norm(c.get("wiki_text", "")) not in norm(pg["body"]):
            r.fail(f"{cid}: wiki_text 不是 {c['page']} 的原文子字串 → 回 evidence 重做這張卡")
    for g, n in per_goal.items():
        if n < MIN_CARDS_PER_GOAL:
            r.fail(f"{g}: 只有 {n} 張卡（需要 ≥ {MIN_CARDS_PER_GOAL}）")
    r.info(f"{len(raw)} 張卡")
    return r.finish()


# ---------------------------------------------------------------- approve
def cmd_approve(deck: Path) -> bool:
    r = Report(deck, "human approve gate")
    text = (deck / "outline.md").read_text(encoding="utf-8")
    cards = load_cards(deck)
    m = re.search(r"^status:\s*(\w+)", text, re.M)
    status = m.group(1) if m else "missing"
    if status != "approved":
        r.fail(f"outline.md status = {status}，需要人工改成 approved 才能往下")
    for cid in set(re.findall(r"\bc\d+\b", text)):
        if cid not in cards:
            r.fail(f"outline 引用了不存在的卡片 {cid}")
    return r.finish()


# ---------------------------------------------------------------- faithfulness
def slide_units(s: dict) -> list[tuple[str, str]]:
    """回傳 (欄位, 文字) — 需要引用的文字單位。"""
    units = []
    for field in ("bullets", "left", "right"):
        for i, t in enumerate(s.get(field, []) or []):
            units.append((f"{field}[{i}]", t))
    if s.get("explain"):
        units.append(("explain", s["explain"]))
    for j, c in enumerate(s.get("chain", []) or []):
        for i, t in enumerate(c.get("items", [])):
            units.append((f"chain[{c.get('tag', j)}][{i}]", t))
    for field in ("given", "steps"):
        for i, t in enumerate(s.get(field, []) or []):
            units.append((f"{field}[{i}]", t))
    if s.get("result"):
        units.append(("result", s["result"]))
    return units


def svg_texts(svg: str) -> list[str]:
    return [html.unescape(t) for t in re.findall(r"<text[^>]*>(.*?)</text>", svg or "", re.S)]


def cmd_faithful(deck: Path) -> bool:
    r = Report(deck, "faithfulness gate")
    cards = load_cards(deck)
    slides = load_json(deck / "deck.json")["slides"]
    bad_slides = []
    for s in slides:
        sid, errs, slide_cards = s["id"], [], set()
        if s.get("layout") == "title":
            continue
        for field, text in slide_units(s):
            cites = [c.strip() for m in CITE_RE.finditer(text) for c in m.group(1).split(",")]
            if not cites:
                errs.append(f"{field} 沒有引用卡片：「{text[:30]}…」")
                continue
            missing = [c for c in cites if c not in cards]
            if missing:
                errs.append(f"{field} 引用不存在的卡片 {missing}")
                continue
            slide_cards.update(cites)
            evidence = norm_num(" ".join(cards[c]["wiki_text"] for c in cites))
            for n in numbers(text):
                if norm_num(n) not in evidence:
                    errs.append(f"{field} 的數字 {n} 不在引用卡片 {cites} 中")
        # 圖裡的數字：必須出現在本頁引用過的卡片
        if s.get("svg"):
            evidence = norm_num(" ".join(cards[c]["wiki_text"] for c in slide_cards if c in cards))
            for t in svg_texts(s["svg"]):
                for n in numbers(t):
                    if norm_num(n) not in evidence:
                        errs.append(f"svg 文字「{t}」的數字 {n} 不在本頁卡片中")
        # 論文原圖：必須登錄在 wiki/figures.md，且來源要是本頁引用卡片的來源之一
        if s.get("figure"):
            reg = figure_registry()
            fg = reg.get(s["figure"])
            srcs = set().union(*[card_sources(cards[c], wiki_pages()) for c in slide_cards if c in cards]) if slide_cards else set()
            if fg is None:
                errs.append(f"圖 {s['figure']} 沒登錄在 wiki/figures.md")
            elif fg["source"] not in srcs:
                errs.append(f"圖 {s['figure']} 來自 {fg['source']}，但本頁沒有引用該來源的卡片")
        # 標題的數字也要有卡片支持（2026-11-21 實跑時發現標題沒被檢查）
        evidence = norm_num(" ".join(cards[c]["wiki_text"] for c in slide_cards if c in cards))
        for n in numbers(s.get("title", "")):
            if norm_num(n) not in evidence:
                errs.append(f"標題的數字 {n} 不在本頁卡片中")
        if errs:
            bad_slides.append(sid)
            for e in errs:
                r.fail(f"{sid}「{s.get('title','')}」：{e}")
    r.info(f"{len(slides)} 頁；需要重寫：{', '.join(bad_slides) if bad_slides else '無'}")
    return r.finish()


# ---------------------------------------------------------------- render + render check
def visible_len(t: str) -> int:
    t = CITE_RE.sub("", t)
    t = MATH_RE.sub(lambda m: re.sub(r"\\[a-zA-Z]+|[{}_^$]", "", m.group(0)), t)
    return len(t.strip())


def cmd_render(deck: Path) -> bool:
    data = load_json(deck / "deck.json")
    cards = load_cards(deck)
    pages = wiki_pages()
    used = {c.strip() for s in data["slides"] for _, t in slide_units(s)
            for m in CITE_RE.finditer(t) for c in m.group(1).split(",")}
    card_meta = {}
    for cid in sorted(used, key=lambda x: int(x[1:])):
        c = cards[cid]
        pg = pages.get(c["page"])
        card_meta[cid] = {"page": c["page"],
                          "title": pg["meta"].get("title", c["page"]) if pg else c["page"],
                          "sources": ["自己算（docs/calc-check.py）"] if "（計算）" in c["wiki_text"]
                                     else sorted(card_sources(c, pages)) or (sorted(page_sources(c["page"], pg)) if pg else []),
                          "text": c["wiki_text"]}
    import os
    rel = os.path.relpath(ROOT, deck).replace(os.sep, "/") + "/"   # 簡報在樹的第幾層，就往上幾層
    data = dict(data, home=rel + "index.html")
    reg = figure_registry()
    figs = {}
    for s in data["slides"]:
        if s.get("figure") in reg:
            fg = reg[s["figure"]]
            figs[s["figure"]] = {"src": f"{rel}assets/figures/{s['figure']}.png", "label": fg["label"],
                                 "desc": fg["desc"], "cite": source_citation(fg["source"])}
    payload = json.dumps({"deck": data, "cards": card_meta, "figures": figs}, ensure_ascii=False)
    payload = payload.replace("</", "<\\/")
    tpl = TEMPLATE.read_text(encoding="utf-8")
    out = tpl.replace("/*__DECK_DATA__*/null", payload).replace("__DECK_TITLE__", html.escape(data["title"]))
    out = out.replace("../../template/", rel + "template/").replace('href="../../index.html"', f'href="{rel}index.html"')
    (deck / "index.html").write_text(out, encoding="utf-8")

    r = Report(deck, "render + render gate")
    if "__DECK" in out:
        r.fail("模板 placeholder 沒有被取代")
    plain = MATH_RE.sub("", json.dumps(data, ensure_ascii=False))  # LaTeX 本來就會有 }}，只檢查數學式以外
    if re.search(r"TODO|\{\{|\}\}|lorem", plain, re.I):
        r.fail("內容殘留 TODO / {{ }} / lorem")
    ids = [s["id"] for s in data["slides"]]
    if len(ids) != len(set(ids)):
        r.fail("slide id 重複")
    for s in data["slides"]:
        b = s.get("bullets", []) or []
        if len(b) > MAX_BULLETS:
            r.fail(f"{s['id']}：{len(b)} 個 bullet > {MAX_BULLETS}")
        for f, t in slide_units(s):
            if visible_len(t) > MAX_BULLET_CHARS:
                r.fail(f"{s['id']} {f}：{visible_len(t)} 字 > {MAX_BULLET_CHARS}")
        for c in s.get("chain", []) or []:
            if len(c.get("items", [])) > 3:
                r.fail(f"{s['id']}：因果鏈「{c.get('tag')}」超過 3 點，太長就拆頁")
        if s.get("layout") == "causal" and len(s.get("chain", [])) < 3:
            r.fail(f"{s['id']}：causal 頁至少要有 3 段（動機/問題/解法/代價）")
        if s.get("layout") == "quiz":
            if not (0 <= s.get("answer", -1) < len(s.get("options", []))):
                r.fail(f"{s['id']}：quiz answer 索引超出選項範圍")
        for f, txt in slide_units(s) + [("title", s.get("title", ""))]:
            if txt.replace("\\$", "").count("$") % 2:
                r.fail(f"{s['id']} {f}：$ 數學符號沒有成對")
        if s.get("figure"):
            if s["figure"] not in figs:
                r.fail(f"{s['id']}：圖 {s['figure']} 沒登錄，不能渲染")
            elif not (FIG_DIR / f"{s['figure']}.png").exists():
                r.fail(f"{s['id']}：找不到圖檔 {s['figure']}.png")
        if s.get("svg") and not s["svg"].lstrip().startswith("<svg"):
            r.fail(f"{s['id']}：svg 欄位不是 <svg> 開頭")
    r.info(f"輸出 {(deck / 'index.html').relative_to(ROOT)}（{len(ids)} 頁，{len(card_meta)} 張卡片被引用，{len(out)//1024} KB）")
    return r.finish()


# ---------------------------------------------------------------- inbox（整理亂丟的檔案）
ROOT_KNOWN = {".gitignore", ".nojekyll", "AGENTS.md", "README.md", "index.html", ".git", "taxonomy.json",
              "raw", "wiki", "decks", "docs", "pipeline", "template", "assets"}


def inbox_items() -> list[Path]:
    """未整理的東西：最外層的陌生檔案、raw/ 最上層的陌生檔案、raw/<節點>/ 裡沒有來源卡的原檔、不在分類樹上的資料夾。"""
    nodes = taxonomy_nodes()
    items = [p for p in ROOT.iterdir() if p.name not in ROOT_KNOWN and not p.name.startswith((".", "_"))]
    cards = card_paths()
    for p in sorted(RAW.rglob("*")):
        rel = p.relative_to(RAW).as_posix()
        if p.name == "README.md" or p.name.startswith("."):
            continue
        if p.is_dir():
            if rel not in nodes:
                items.append(p)
        elif p.parent == RAW or (p.suffix != ".md" and p.stem not in cards) \
                or p.parent.relative_to(RAW).as_posix() not in nodes:
            items.append(p)
    return sorted(set(items))


def guess_kind(p: Path) -> tuple[str, str]:
    """回傳（類型, 理由）。類型只是建議；分類節點一律先問 Percy。"""
    import shutil, subprocess
    ext = p.suffix.lower()
    if p.is_dir():
        return "?", "資料夾：逐一看裡面的檔案"
    if ext in (".pptx", ".ppt", ".key", ".odp"):
        return "slides", "簡報檔"
    if ext in (".md", ".txt", ".docx", ".doc", ".png", ".jpg", ".jpeg", ".heic"):
        return "notes", "文字或圖片筆記"
    if ext != ".pdf":
        return "?", f"不認得的副檔名 {ext}"
    if not shutil.which("pdftotext"):
        return "?", "沒有 pdftotext，請人工判斷"
    info = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True).stdout
    pages = int((re.search(r"Pages:\s+(\d+)", info) or [0, 0])[1])
    size = re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info)
    landscape = bool(size) and float(size[1]) > float(size[2])
    text = subprocess.run(["pdftotext", "-l", "2", str(p), "-"], capture_output=True, text=True).stdout
    if len(text.strip()) < 100 * max(1, min(pages, 2)):
        return "notes", f"{pages} 頁、幾乎沒有文字層 → 手寫或掃描筆記（要轉錄）"
    if landscape:
        return "slides", f"{pages} 頁橫式 → 簡報匯出"
    if re.search(r"Abstract|Index Terms|IEEE|doi\.org|DOI|References", text):
        return "papers", f"{pages} 頁直式、有 Abstract/IEEE/DOI → 論文"
    return "notes", f"{pages} 頁直式、有文字 → 可能是講義或筆記"


def suggest_id(p: Path, kind: str) -> str:
    stem = re.sub(r"[^0-9A-Za-z]+", "-", p.stem).strip("-").lower()[:40] or "item"
    return ("percy-" + stem) if kind in ("notes", "slides") and not stem.startswith("percy") else stem


def tree_text(nodes: dict) -> list[str]:
    lines = []
    for path, n in nodes.items():
        depth = path.count("/") + 1 if path else 0
        lines.append(f"{'  ' * depth}- `{path or '(根)'}` {n['title']}")
    return lines


def cmd_inbox(_deck=None) -> bool:
    r = Report(None, "inbox")
    items = inbox_items()
    if not items:
        r.info("沒有未整理的檔案")
        return r.finish()
    r.info("| 檔案 | 類型 | 建議 id | 理由 |")
    r.info("|---|---|---|---|")
    for p in items:
        kind, why = guess_kind(p)
        r.info(f"| `{p.relative_to(ROOT)}` | {kind} | `{suggest_id(p, kind)}` | {why} |")
    r.info("**分類節點不要自己決定：先問 Percy 要放在哪裡**（可以附上建議）。目前的分類樹：")
    for line in tree_text(taxonomy_nodes()):
        r.info(line)
    r.info("Percy 回答後：移到 raw/<節點>/<id>.<副檔名> → 同資料夾寫 <id>.md 來源卡（node、file、original_name）→ "
           "wiki/<節點>/sources/<id>.md 寫論述 → 更新 raw/README.md → ingest → build")
    return r.finish()


# ---------------------------------------------------------------- hub（大目錄）
def deck_dirs() -> list[Path]:
    return sorted(p.parent for p in (ROOT / "decks").rglob("brief.md") if (p.parent / "deck.json").exists())


def deck_summary(d: Path) -> dict:
    meta = parse_page(d / "brief.md")["meta"]
    data = load_json(d / "deck.json")
    cards = load_cards(d) if (d / "evidence.json").exists() else {}
    srcs = set()
    for c in cards.values():
        srcs |= card_sources(c)
    report = (d / "check-report.md").read_text(encoding="utf-8") if (d / "check-report.md").exists() else ""
    last = re.findall(r"^### .*?— (PASS|FAIL)$", report, re.M)
    return {"slug": d.name, "href": d.relative_to(ROOT).as_posix() + "/index.html", "node": meta.get("node", ""),
            "title": data["title"], "summary": meta.get("summary", ""), "skeleton": meta.get("skeleton", ""),
            "order": int(meta.get("order", 99)), "sources": sorted(srcs), "status": last[-1] if last else "未檢查",
            "slides": [{"id": s["id"], "title": s.get("title", ""), "layout": s.get("layout", "bullets")} for s in data["slides"]]}


def cmd_hub(_deck=None) -> bool:
    """依 taxonomy.json 的分類樹產生根目錄 index.html：每個節點列出簡報、每篇來源的論述、概念頁。"""
    r = Report(None, "hub")
    tax = load_json(TAXONOMY)
    nodes = taxonomy_nodes()
    pages = wiki_pages()
    blob = "https://github.com/youping13/vlsi-wiki2deck/blob/main/"
    decks = [deck_summary(d) for d in deck_dirs()]
    for d in decks:
        if d["node"] not in nodes:
            r.fail(f"{d['href']}：node「{d['node']}」不在 taxonomy.json")
        if d["status"] != "PASS":
            r.fail(f"{d['href']}：最後一次關卡不是 PASS，大目錄會標紅")
    by_slug = {d["slug"]: d for d in decks}

    def build(node, path):
        here = [d for d in decks if d["node"] == path]
        here.sort(key=lambda x: x["order"])
        srcs, cons = [], []
        for key, pg in pages.items():
            if node_of_key(key) != path:
                continue
            item = {"title": str(pg["meta"].get("title", slug_of(key))).strip('"'), "href": f"{blob}wiki/{key}.md"}
            if is_source(key):
                m = re.search(r"\*\*一年後要記得\*\*：(.+)", pg["body"]) or re.search(r"## 論述\n+(.+)", pg["body"])
                item["lead"] = re.sub(r"^\*\*[^*]+\*\*：", "", m.group(1).strip()) if m else ""
                srcs.append(item)
            else:
                cons.append(item)
        chain = []
        for c in node.get("chain", []):
            d = by_slug.get(c["deck"])
            ids = [s["id"] for s in d["slides"]] if d else []
            if c["slide"] not in ids:
                r.fail(f"taxonomy.json 的因果鏈指向不存在的頁：{c['deck']} {c['slide']}")
                continue
            chain.append({"text": c["text"], "href": f"{d['href']}#{ids.index(c['slide']) + 1}", "node": d["node"]})
        kids = [build(ch, f"{path}/{ch['id']}" if path else ch["id"]) for ch in node.get("children", [])]
        total = len(here) + len(srcs) + len(cons) + sum(k["total"] for k in kids)
        return {"id": node["id"], "path": path, "title": node["title"], "desc": node.get("desc", ""),
                "kind": node.get("kind", ""), "decks": here, "sources": srcs, "concepts": cons,
                "chain": chain, "children": kids, "total": total}

    tree = build(tax, "")
    hub = {"tree": tree, "links": tax.get("links", []), "generated": f"{_dt.datetime.now().astimezone():%Y-%m-%d %H:%M}"}
    payload = json.dumps(hub, ensure_ascii=False).replace("</", "<\\/")
    tpl = (ROOT / "template" / "hub.html").read_text(encoding="utf-8")
    (ROOT / "index.html").write_text(tpl.replace("/*__HUB_DATA__*/null", payload)
                                     .replace("__HUB_TITLE__", html.escape(tax["title"])), encoding="utf-8")
    used = [d["node"] for d in decks] + [node_of_key(k) for k in pages]
    empty = [n["path"] for n in nodes.values() if n["path"] and not any(u == n["path"] or u.startswith(n["path"] + "/") for u in used)]
    r.info(f"index.html：{len(nodes) - 1} 個節點、{len(decks)} 份簡報、{sum(len(d['slides']) for d in decks)} 頁、"
           f"{sum(1 for k in pages if is_source(k))} 篇論述；待新增：{', '.join(empty) or '無'}")
    return r.finish()


def cmd_build(_deck=None) -> bool:
    """lint → 每份簡報跑 all → 產生大目錄。"""
    ok = cmd_lint()
    for d in deck_dirs():
        print(f"\n======== {d.relative_to(ROOT).as_posix()} ========")
        for step in ORDER:
            if not STEPS[step](d):
                ok = False
                print(f"⛔ {d.name} 停在 {step}")
                break
    return cmd_hub() and ok


# ---------------------------------------------------------------- main
STEPS = {
    "lint": cmd_lint, "retrieve": cmd_retrieve, "coverage": cmd_coverage,
    "evidence": cmd_evidence, "approve": cmd_approve, "faithful": cmd_faithful,
    "render": cmd_render, "hub": cmd_hub, "build": cmd_build, "inbox": cmd_inbox,
}
ORDER = ["retrieve", "coverage", "evidence", "approve", "faithful", "render"]


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] not in [*STEPS, "all"]:
        print(__doc__)
        return 2
    cmd = argv[1]
    deck = Path(argv[2]).resolve() if len(argv) > 2 else None
    if cmd not in ("lint", "hub", "build", "inbox") and deck is None:
        print("需要 deck 路徑，例如 decks/mixed-signal/monotonic/sar-monotonic")
        return 2
    if cmd == "all":
        for step in ORDER:
            if not STEPS[step](deck):
                print(f"\n⛔ 停在 {step}。依 AGENTS.md §3 的「失敗退回」處理後再跑。")
                return 1
        print("\n✅ 全部關卡通過。")
        return 0
    return 0 if STEPS[cmd](deck) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
