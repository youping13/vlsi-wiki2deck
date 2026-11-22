# vlsi-wiki2deck

把 LLM Wiki 變成**每一句都有出處**的教學 HTML 簡報。第一個主題：**SAR ADC**。

- 📚 Wiki：[`wiki/index.md`](wiki/index.md)
- 🧭 **大目錄（所有起點）**：[`index.html`](index.html)，只放分類卡；點進去是各節點頁 `nodes/<節點>/`（簡報、論述、概念頁），照 VLSI 分類樹（[`taxonomy.json`](taxonomy.json)）產生
- 🖼 論文圖登錄：[`wiki/figures.md`](wiki/figures.md)（圖檔在 `assets/figures/`）
- 🤖 Agent 規則：[`AGENTS.md`](AGENTS.md)

延伸計畫見 [`docs/roadmap.md`](docs/roadmap.md)。

## 快速開始

```bash
python pipeline/wiki2deck.py lint                 # 檢查 wiki
python pipeline/wiki2deck.py all decks/mixed-signal/monotonic/sar-monotonic   # 跑一份簡報的完整流程
python pipeline/wiki2deck.py build                # 一次重建：lint → 每份簡報 → 大目錄 index.html
```
只需要 Python 3.10 以上，不用安裝任何套件。打開根目錄的 `index.html` 就是大目錄。

## 做一份新簡報（可重用）

1. 新檔案丟在最外層就好，跑 `python pipeline/wiki2deck.py inbox` 整理到 `raw/`（規則見 `raw/README.md`），再 ingest 進 `wiki/`（AGENTS.md §2），然後跑 `lint`
2. **先問 Percy 放在分類樹哪個節點**，再建 `decks/<節點>/<名字>/brief.md`，寫學習目標和關鍵字（格式照 `decks/mixed-signal/basic/adc-basics/brief.md`）
3. 請 agent 依 `pipeline/prompts/` 依序產生 `evidence.json` → `outline.md` → `deck.json`
4. 自己看過大綱，把它改成 `status: approved`
5. `brief.md` 填 `node`、`order`、`summary`，再跑 `python pipeline/wiki2deck.py build`，大目錄會自動出現在那個節點底下
6. 要放進節點的因果鏈，就在 `taxonomy.json` 那個節點的 `chain` 加一項

## 目錄

```
AGENTS.md            agent 工作守則
taxonomy.json        VLSI 分類樹（所有東西都照它放）
raw/<節點>/          原檔（不進 git）＋ 同名來源卡 .md，清單見 raw/README.md
wiki/                LLM Wiki：index、log、sources/、concepts/
pipeline/            prompts/、wiki2deck.py
template/deck.html   可重用簡報模板（零相依、可列印成 PDF；KaTeX 在 template/vendor/）
assets/figures/      論文原圖（簡報引用時自動標出處）
decks/<節點>/<slug>/ brief → retrieval → evidence → outline → deck.json → index.html＋check-report
docs/                討論紀錄、執行紀錄、反思、繳交說明、流程圖
```
