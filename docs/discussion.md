# 先討論、後生成：建 Wiki 前的討論紀錄

> 日期：2026-11-21　參與：Percy、Claude
> 這份記錄「在生成任何 wiki 頁面之前」決定了什麼。Percy 在第 3 輪授權 Claude 全權決定之後的細節，Claude 的決定都標成 **[C 決定]**。

## 第 1 輪：要做什麼？

- Percy：想做一個「之後可以一直用」的東西，例如簡報模板；太麻煩的話，就用自己的 SAR ADC、VLSI 論文和筆記建 wiki。
- Claude 提案：兩個一起做。**可重用的 Wiki→簡報流水線（wiki2deck）＋第一個主題 SAR ADC**。
- 決定：專案名稱 **wiki2deck**，題目「把論文筆記變成教學簡報的 AI 流水線——以 SAR ADC 為例」。

## 第 2 輪：資料從哪來？

- Claude 想讀 `SSCAS_專題二`、`VLSI` 資料夾，Percy 拒絕。
- Percy：「檔案先不給，就先用一般論文的 PDF」。
- 決定：**只用網路上公開、可以合法閱讀的 PDF 和論文頁面**。付費論文只用摘要和書目層級的資訊，並在來源卡標明「僅摘要」。

## 第 3 輪：規則

- Percy：這次不用照專案規則，不用 Claude Output，但要有 AGENTS.md，之後 Claude 全權處理。

## Claude 依授權做的 schema 決定

| 問題 | 選項 | 決定 |
|---|---|---|
| 讀者是誰？ | 電機大三／完全沒學過的人 | **完全沒學過但懂「電壓、電容」的人** [C 決定]：作業要求「原本不熟悉該主題的人能理解」 |
| wiki 粒度 | 一篇論文一頁 vs 一個概念一頁 | **兩層：sources/ 一篇一頁＋concepts/ 一概念一頁** [C 決定]：概念頁才能合併多篇來源，也才能記錄來源之間的衝突 |
| 數字怎麼處理 | 直接寫 vs 標出處 | **每個數字都標 `(src: id)`，衝突時兩個都留** [C 決定]：SAR 的數字很容易互相矛盾，例如 monotonic 省 81% 還是 63%？ |
| 來源組合 | 全部 paper vs 混教材 | **教材 2＋論文 2＋綜述 1＋課程講義 1** [C 決定]：初學者需要教材的比喻，深度靠論文 |
| 簡報流程 | 一次生成 vs graph | **照課堂 graph（第 43 頁）實作，關卡用腳本跑** [C 決定]：檢查要可重現，不能只靠 AI 自己說「我檢查過了」 |
| 簡報格式 | Reveal.js vs 自製模板 | **自製單一 HTML 模板，零相依** [C 決定]：離線能開，GitHub Pages 直接放，以後換主題只改 JSON |

## 第一批 ingest 清單（討論後才開始生成）

| id | 來源 | 類型 | 取得程度 | 打算寫進哪些 concept |
|---|---|---|---|---|
| kester-mt021 | Walt Kester, ADI MT-021 | 教材 | 全文 PDF | overview、binary-search、cdac、history、timing |
| razavi-2015 | Razavi, "A Tale of Two ADCs", SSC Mag. 2015 | 期刊專欄 | 全文 PDF | cdac、comparator、speed、redundancy、sar-vs-pipeline |
| saxena-lecture | V. Saxena, SAR ADC lecture (Boise State) | 講義 | 全文 PDF | cdac、parasitic、sizing、async |
| tang-2022-survey | Tang et al., TCAS-I 2022 低功耗 SAR 綜述 | 綜述 | 全文 PDF | fom、noise、energy、switching、calibration |
| liu-2010-monotonic | C.-C. Liu et al., JSSC 2010（成大張順志實驗室） | 論文 | 摘要＋書目 | switching-schemes |
| hu-2024-hybrid | Y. Hu et al., Micromachines 2024 | 論文（OA） | 摘要 | switching-schemes |

→ 確認後才開始寫 `raw/` 和 `wiki/`。

## 第 4 輪：Percy 提供全文（21:37）

- Percy 把 Liu 2010 JSSC 全文 PDF 放進 `raw/`：「資料我給一篇論文了，在 raw，自行處理」。
- [C 決定] `liu-2010-monotonic` 從「只有摘要」升級成全文 ingest。另外新增一頁 concept `monotonic-sar-case-study`，把這顆成大晶片當成簡報的「真實案例」。
- [C 決定] PDF 原檔不進 git（IEEE 授權），在 `.gitignore` 加上 `raw/*.pdf`；wiki 只放改寫過的重點。
- 全文解開了一個衝突：「81%」是 10 位元平均切換能量 1365.3 → 255.5 CVref² 的比較。綜述寫的 63% 仍然對不上，兩個數字都保留。

## 第 5 輪：讀者改成「一年後的我」（22:45）

- Percy 提供兩份自己的文件：Mixed-Signal 手寫筆記、專題 meeting 1 簡報（他說不是要照那份的風格），「我要看你怎麼做」。
- Percy 的新要求：
  - 所有教學簡報的讀者都是我自己；目的是一年後看到可以快速回想
  - 要有強烈的因果關係：動機、問題、為什麼這樣解決、優缺點（例如 monotonic 是為了解決 power）
  - 砝碼比喻不必要，數據比較也不重要；**計算部分保留**
  - 示意圖可以自己畫，也可以從網路抓
- [C 決定] 這次就當成 roadmap 第 2 項「論文＋筆記，以筆記為主」的實際試做：wiki 的順序和觀點跟 Percy 的筆記/報告，論文只補證據、數字和圖。
- [C 決定] 手寫筆記先轉成 Markdown＋LaTeX，計算全部用 `docs/calc-check.py` 驗算；不確定的字列在 `docs/transcription-check.md` 給 Percy 核對。
- [C 決定] 模板新增 `causal`（動機 → 問題 → 解法 → 代價）和 `calc`（條件 → 步驟 → 結論）兩種版型；規則寫進 AGENTS.md §4。
- [C 決定] 示意圖自己畫（標「示意圖（自己畫）」），網路上的圖沒有抓，因為授權不明；論文圖沿用已登錄的 4 張。

## 第 6 輪：大目錄（22:57）

- Percy：「我要一個大目錄，所有起始點都在這邊，之後再導到小的簡報。」
- [C 決定] v3 的 21 頁拆成三份小簡報，每份一條因果鏈：`adc-basics`（A，骨架：Mixed-Signal 筆記）、`sar-monotonic`（B，骨架：meeting 1）、`sar-circuits`（C，骨架：meeting 1）。`sar-adc` 保留成作業完整版。
- [C 決定] 大目錄由腳本從各份 `brief.md` 自動產生（`wiki2deck.py hub`），不手寫，以後新增簡報不用改目錄；最上面的因果鏈寫在 `decks/hub.json`，每一項直接跳到某份簡報的某一頁。
- [C 決定] 每份簡報加「⌂ 目錄」連結（快捷鍵 H）回大目錄。

## 第 7 輪：raw 整理（2026-11-22 21:47）

- Percy：「整理 raw 的資料，之後你也要整理，我會亂丟在最外層。」
- [C 決定] `raw/` 分成 `cards/`（來源卡，進 git）和 `papers/`、`notes/`、`slides/`（原檔，不進 git）。原檔改名成和來源卡同一個 id，原檔名記在來源卡的 `original_name:`。
- [C 決定] 新增 `wiki2deck.py inbox`：掃描最外層和 `raw/` 最上層，依「有沒有文字層、橫式還是直式、有沒有 Abstract/IEEE」猜分類並建議 id；`lint` 發現未整理檔案時會提醒。規則寫進 AGENTS.md §0.5（開工第一件事）和 `raw/README.md`。

## 第 8 輪：VLSI 分類樹（2026-11-22 21:53）

- Percy：「整個都有問題。我的大目錄是 VLSI，下面會分 mix-signal、bias-circuit、opamp、LDO、basic 等，之後會新增；mix-signal 再下面是 basic（INL/DNL、沒滿 code、取樣問題等）、monotonic 論文、論文 2、論文 3 等相關資訊。之後加一個東西，都先問我怎麼分類。」
- 問了 4 個問題，Percy 的回答：
  - 5 份網路 SAR 通論資料 → 新增 `mixed-signal/sar-basics` 節點，**但每一篇都要有單純的論述**
  - 還沒內容的 bias-circuit、opamp、ldo、basic → 大目錄顯示「待新增」
  - 21 頁作業完整版 `decks/sar-adc` → 刪掉（檢查紀錄備份到 `docs/archive/sar-adc/`）
  - 資料夾命名 → `mixed-signal`、`bias-circuit`、`opamp`、`ldo`、`basic`
- [C 決定] 分類樹寫在 `taxonomy.json`，raw、wiki、decks、大目錄全部照它放：`raw/<節點>/`（原檔＋來源卡同資料夾）、`wiki/<節點>/`、`wiki/<節點>/sources/`、`decks/<節點>/<slug>/`。
- [C 決定] 概念頁的歸類（請 Percy 確認）：basic ← 取樣、量化雜訊、動態參數、靜態參數、FoM；sar-basics ← SAR 總覽、二元搜尋、電容 DAC、比較器、速度、雜訊與尺寸、冗餘校正、SAR vs Pipeline、簡史；monotonic ← 切換方式與能量推導、bootstrap、成大晶片案例。
- 硬規則寫進 AGENTS.md §0.5：新增任何東西前先問 Percy 分類；`taxonomy.json` 只有 Percy 同意才改。
