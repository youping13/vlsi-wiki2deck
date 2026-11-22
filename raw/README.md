# raw/：原始資料（照 VLSI 分類樹放）

> Percy 會把新檔案直接丟在專案最外層或 `raw/`。agent 每次開工先跑 `python pipeline/wiki2deck.py inbox`，**拿清單去問 Percy 每個檔案要放哪個節點**，得到回答才整理。

## 結構（和 `taxonomy.json` 一一對應）

```
raw/
  mixed-signal/
    basic/        percy-ms-notes.pdf ＋ percy-ms-notes.md
    sar-basics/   kester-mt021.md、razavi-2015.md、saxena-lecture.md、tang-2022-survey.md、hu-2024-hybrid.md
    monotonic/    liu-2010-monotonic.pdf ＋ .md、percy-meeting1.pdf ＋ .md
  basic/ bias-circuit/ opamp/ ldo/   （待新增，有東西時才建資料夾）
```

- 每個節點資料夾裡：原檔 `<id>.<副檔名>`（**不進 git**）和同名來源卡 `<id>.md`（進 git）放在一起
- 一篇論文和我對它做的筆記、報告，放在**同一個節點**（例如 `monotonic/` 同時有論文和 meeting 1）

## 命名規則

- 論文：`第一作者姓-年份-關鍵字`，例如 `liu-2010-monotonic`
- 我的筆記和簡報：`percy-` 開頭，例如 `percy-ms-notes`、`percy-meeting1`
- 來源卡前段要有 `node:`（等於所在資料夾）、`file:`（原檔路徑）、`original_name:`（原本的檔名）

## 整理流程（inbox）

1. `python pipeline/wiki2deck.py inbox`：列出未整理的檔案、猜類型、建議 id、印出目前的分類樹
2. **問 Percy**：每個檔案放哪個節點？需要新節點嗎？（附上建議）
3. 移到 `raw/<節點>/<id>.<副檔名>`，同資料夾寫 `<id>.md` 來源卡；手寫筆記要轉錄成 Markdown＋LaTeX，不確定的字列進 `docs/transcription-check.md`
4. 寫 `wiki/<節點>/sources/<id>.md`，**一定要有 `## 論述`**（只講這一篇）
5. 更新下面的清單 → 照 AGENTS.md §2 ingest → `python pipeline/wiki2deck.py build`
6. 同一份東西不要存兩次：新版本覆蓋舊檔，並在來源卡記一筆更新紀錄

## 檔案清單

| 節點 | id | 原檔 | 原本的檔名 | 說明 |
|---|---|---|---|---|
| mixed-signal/basic | percy-ms-notes | `percy-ms-notes.pdf` | Mixed-Signal IC Design.pdf | 我的手寫筆記：取樣、aliasing、SNR（3 頁） |
| mixed-signal/sar-basics | kester-mt021 | （網路公開，未下載） | — | ADI MT-021 教材 |
| mixed-signal/sar-basics | razavi-2015 | （網路公開，未下載） | — | Razavi, SSC Magazine 2015 |
| mixed-signal/sar-basics | saxena-lecture | （網路公開，未下載） | — | Saxena SAR 講義 |
| mixed-signal/sar-basics | tang-2022-survey | （網路公開，未下載） | — | Tang et al., TCAS-I 2022 |
| mixed-signal/sar-basics | hu-2024-hybrid | （只有摘要） | — | Hu et al., Micromachines 2024 |
| mixed-signal/monotonic | liu-2010-monotonic | `liu-2010-monotonic.pdf` | 2010JSSC_A_10-bit_50-MS-s_SAR_ADC_with_a_Monotonic_Capacitor_Switching_Procedure.pdf | Liu et al., JSSC 2010（成大）全文 |
| mixed-signal/monotonic | percy-meeting1 | `percy-meeting1.pdf` | 專題（一)_meeting1 的副本.pdf | 我的專題 meeting 1 報告（78 頁） |
