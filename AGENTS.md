# AGENTS.md — vlsi-wiki2deck

> 給任何 coding agent（Claude Code / Codex / Copilot）讀的工作守則。
> 本 repo 做兩件事：**(1) 維護一個主題 LLM Wiki；(2) 用 wiki 當唯一知識來源，產生教學 HTML 簡報。**
> 所有內容都掛在 **VLSI 分類樹**（`taxonomy.json`）上：VLSI → basic、mixed-signal、bias-circuit、opamp、ldo …；mixed-signal → basic、sar-basics、monotonic（Liu 2010）、之後的論文 2、論文 3 …

## 0. 一句話原則

**簡報上的每一句話都要能追回 wiki 的某一段原文；wiki 的每一句話都要能追回某一篇來源。**
沒有證據的內容，寧可不寫。

## 0.5 新增任何東西之前：先問 Percy 怎麼分類（硬規則）

- **新資料、新筆記、新簡報、新的分類節點，放在分類樹的哪裡，一律先問 Percy**，可以附上你的建議，但不可以自己決定後直接搬。
- Percy 會把新檔案**直接丟在最外層或 `raw/`**。每次開工先跑 `python pipeline/wiki2deck.py inbox`：它會列出未整理的檔案、猜類型（論文／手寫筆記／簡報）並印出目前的分類樹。拿這份清單去問 Percy 每個檔案要放哪個節點。
- Percy 回答後，照 `raw/README.md` 的流程整理、ingest、`build`。`lint` 看到未整理檔案也會提醒。
- `taxonomy.json` 只有在 Percy 同意後才能新增或改名節點。

## 1. 目錄

```
taxonomy.json        分類樹（VLSI → …）。raw、wiki、decks、大目錄全部照這棵樹放
raw/<節點>/          <id>.<副檔名> 原檔（不進 git）＋ <id>.md 來源卡（進 git）；清單在 raw/README.md
wiki/
  index.md           wiki 首頁（照分類樹列出所有頁面，每次 ingest 都要更新）
  log.md             ingest / 修改紀錄（append only）
  figures.md         論文圖登錄表
  <節點>/<slug>.md   概念頁：定義、原理、數字、[[連結]]、出處
  <節點>/sources/<id>.md  一篇來源一頁：**## 論述**（單純講這一篇）＋重點、可信度、衝突
pipeline/
  prompts/           每個 AI 節點的 prompt
  wiki2deck.py       所有「檢查關卡」與渲染（純 Python，無相依套件）
template/deck.html   可重用的 HTML 簡報模板
decks/<節點>/<slug>/ 一份簡報的所有中間產物與成品
docs/                討論紀錄、執行紀錄、驗算腳本
docs/private/        反思、loop/graph 設計、繳交說明（只在本機，不進 git）
```

## 2. Wiki 規則（ingest 時）

1. **先問分類、先討論、後生成**：先問 Percy 放哪個節點；再寫 `raw/<節點>/<id>.md` 來源卡並列出「打算新增/修改哪些頁」，確認後才動 `wiki/`。
2. 每個 concept 頁格式固定：
   ```md
   ---
   node: mixed-signal/basic   ← 必須等於檔案所在的資料夾，而且在 taxonomy.json 裡
   title: 中文名（English）
   tags: [..]
   sources: [source-id, ...]
   ---
   ## 一句話
   ## 原理
   ## 關鍵數字        ← 每個數字後面加 (src: source-id)
   ## 常見誤解 / 衝突
   ## 相關            ← [[slug]] 連結
   ```
3. 數字一律標出處 `(src: id)`。不同來源數字衝突時**不要擇一**，兩個都寫並說明原因。
4. 只寫來源有講的。自己的推論要標 `（推論）`；自己算出來的數字標 `（計算）`，並把算式加進 `docs/calc-check.py`。
5. 不貼大段原文；用自己的話改寫，引用 ≤ 15 字。
6. 每次 ingest 結束：更新 `wiki/index.md`、append `wiki/log.md`、跑 `python pipeline/wiki2deck.py lint`。
7. 概念頁可以多一段 `## 因果鏈`（動機／問題／解法／代價），簡報的 causal 頁從這裡取卡。
8. 手寫筆記先轉成 Markdown＋LaTeX，不確定的地方列進 `docs/transcription-check.md` 給本人核對。
9. **數字溯源**：concept 頁裡標 `(src: X)` 的每個數字都必須出現在來源卡 `raw/<節點>/X.md`。來源卡「## 與其他來源的關係」之後的數字（舊版、有爭議的）只能寫在 concept 頁的「常見誤解 / 衝突」段落。
10. **每篇來源都要有單純的論述**：`wiki/<節點>/sources/<id>.md` 一定要有 `## 論述`，只講這一篇——在解決什麼 → 怎麼做 → 為什麼有效 → 限制 → 一年後要記得的一句（大目錄會顯示這一句）。lint 會檢查。
11. 來源升級（例如摘要 → 全文）時，先全文搜尋 `wiki/` 裡所有引用這個來源的數字，再改。

## 3. 簡報流程（graph）

依序執行，**任何關卡失敗就照「退回」欄處理，不准跳過**：

| # | 節點 | 類型 | 產物 | 失敗退回 |
|---|------|------|------|----------|
| 1 | brief | 人工 | `decks/<d>/brief.md` 學習目標＋每個目標的關鍵字 | — |
| 2 | retrieve | 腳本 | `retrieval.json` | — |
| 3 | coverage gate | 檢查 | `check-report.md` | 不足 → **停**，先回 wiki ingest |
| 4 | evidence cards | AI | `evidence.json`（每張卡 `wiki_text` 必須是 wiki 原文子字串） | 回 4，只重做失敗的卡 |
| 5 | evidence gate | 檢查 | 卡片逐字比對 wiki | 回 4 |
| 6 | outline | AI | `outline.md` | 回 6 |
| 7 | human approve | 人工 | `outline.md` 頂端 `status: approved` | 修大綱或補檢索（回 2/6） |
| 8 | slides | AI | `deck.json`（每個 bullet 帶 `[c#]` 卡片編號） | — |
| 9 | faithfulness gate | 檢查 | 每句（含標題、圖裡的字）有卡、數字都出現在卡裡 | 寫錯 → **只重寫失敗的那幾頁**（回 8）；證據不足 → 回 4 補卡 |
| 10 | render | 腳本 | `index.html` | — |
| 11 | render gate | 檢查 | 頁數、字數、殘留 placeholder、引用連結 | 回 8 |
| 12 | 交付 | — | `decks/<d>/index.html` | — |

指令：
```bash
python pipeline/wiki2deck.py lint                      # wiki 格式檢查
python pipeline/wiki2deck.py retrieve  decks/mixed-signal/monotonic/sar-monotonic   # 2
python pipeline/wiki2deck.py coverage  decks/mixed-signal/monotonic/sar-monotonic   # 3
python pipeline/wiki2deck.py evidence  decks/mixed-signal/monotonic/sar-monotonic   # 5
python pipeline/wiki2deck.py approve   decks/mixed-signal/monotonic/sar-monotonic   # 7（只檢查狀態，不會幫你按同意）
python pipeline/wiki2deck.py faithful  decks/mixed-signal/monotonic/sar-monotonic   # 9
python pipeline/wiki2deck.py render    decks/mixed-signal/monotonic/sar-monotonic   # 10 + 11
python pipeline/wiki2deck.py all       decks/mixed-signal/monotonic/sar-monotonic   # 2→11 一次跑，遇到失敗就停
```
每次執行都會 append 到 `decks/<d>/check-report.md`。

## 4. AI 節點的寫作規則

- **讀者：一年後的 Percy**（學過但忘了），目的是快速回想。不要入門比喻（例如砝碼），也不要堆數據比較；**計算保留**。
- **每個主題都寫成因果鏈**：動機 → 問題 → 為什麼這樣解 → 優點 / 代價（例：monotonic 為了解決 DAC 切換功耗 → 代價是共模下降 → 所以要改比較器）。優先用 `causal` 版型，推導用 `calc` 版型。
- 每頁一個觀念，≤ 5 個 bullet，每個 bullet ≤ 70 字。專有名詞直接用英文縮寫（SNDR、Vcm），不用另外解釋。
- **筆記為主**：同一個主題在我的筆記/報告（`percy-*`）和論文都有寫時，順序和觀點跟我的；論文只補證據、數字和圖；兩邊衝突記在「常見誤解 / 衝突」段落。
- 示意圖可以自己畫（SVG，標「示意」），也可以用登錄過的論文圖。
- 每個 bullet 結尾寫 `[c3]` 或 `[c3,c7]`；沒有卡片支持的句子不准寫。
- 數字要原封不動出現在被引用的卡片 `wiki_text` 裡（腳本會比對）。
- 重做時只改 check-report 指出的頁，其他頁不要動。
- **數學符號用 LaTeX**：行內 `$V_X = V_i - \frac{V_R}{2}$`，分數一律寫 `\frac{a}{b}`（腳本靠大括號分開數字）。由 KaTeX 渲染，檔案在 `template/vendor/katex/`，離線也能用。
- **論文原圖**：只能用 `wiki/figures.md` 登錄過的圖，在 slide 加 `"figure": "<id>"`。圖說和出處由腳本從登錄表自動產生，AI 不寫出處。登錄表第 5 欄「原始出處」填圖真正的來源（網址、論文；自己的手寫寫 Percy 手寫註解），沒填就用 source 的論文引用。圖是重點：meeting 簡報裡的架構圖、電路圖、手寫推導，優先放進對應的頁。放圖的那一頁，至少要有一張卡片引用該圖的來源論文。

## 5. 大目錄（所有起點）

- 根目錄 `index.html` 是大目錄，由 `python pipeline/wiki2deck.py hub` 依 `taxonomy.json` 產生，**不要手改**。根目錄只放分類卡（標題、一句話、數量、子分類）；每個節點各有一頁 `nodes/<節點>/index.html`，點進去才看：因果鏈、子分類、簡報（含每頁標題）、每篇來源的論述、概念頁；沒有內容的節點顯示「待新增」。
- 一份簡報 = `decks/<節點>/<slug>/`；`brief.md` 前段要有 `node`、`order`、`summary`、`skeleton`（骨架來源）。
- 節點的因果鏈寫在 `taxonomy.json` 該節點的 `chain`，每一項指向某份簡報的某一頁（slide id），指錯頁 hub 會失敗。
- 簡報要短：一份只講一條因果鏈，超過約 10 頁就拆。每份簡報左上角都有「⌂ 回分類」（快捷鍵 H）回到這份簡報所在的節點頁（會回到原本捲到的位置）；左右兩側有 ◀ ▶ 換頁；點圖可以放大。
- 改完任何東西：`python pipeline/wiki2deck.py build`。

## 6. 可重用

換主題時只需要：問 Percy 放哪個節點 → 新 wiki 內容 + `decks/<節點>/<new>/brief.md`。`pipeline/` 與 `template/` 不用改。

## 7. 不要做的事

- 不要用 wiki 以外的知識補內容（包括你自己的訓練知識）。缺資料 → 回 ingest。
- 不要把 PDF 原檔、付費論文全文 commit 進 git。
- 不要為了通過關卡去改檢查腳本的門檻；要改門檻請寫進本機的 `docs/private/reflection.md` 並說明理由。
