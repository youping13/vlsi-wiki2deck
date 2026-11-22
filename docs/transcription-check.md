# 手寫筆記轉錄：請本人核對

來源：`raw/mixed-signal/basic/percy-ms-notes.pdf`（3 頁）→ `raw/mixed-signal/basic/percy-ms-notes.md`。轉錄時最容易錯的是下標和正負號，下面列出我判讀過、比較不確定的地方。核對完把 `[ ]` 改成 `[x]`。

- [x] p1：「Ideal：x_s(t) 仍是 continuous，只是在其它地方是 0，資訊量沒有改變」，「仍是」是我推測的字
- [x] p1：傅立葉展開那行，指數我讀成 $e^{j2\pi k f_s t}$
- [x] p1：aliasing 推導中間項 $2\pi mn \pm 2\pi\frac{\Delta f}{f_s}n$，± 是照手寫保留的（原式只有 +Δf）
- [x] p2：①「就是理想上的最大值（不考慮其它 non-ideal？）」，原文帶問號，wiki 寫成肯定句
- [x] p3：B 欄 SNR「55.9 dB ⇒ 用 ②」，以及「61.9 − 6.02」旁邊的小字我讀成「訊號少半」
  - Percy 2026-11-22 確認：55.9 dB 是用 ② P_signal / P_noise 算的；61.9 − 6.02 是旁邊的對照。已改正 wiki 與簡報（原本寫成像是由 61.9 − 6.02 推出來）

計算部分全部用 `docs/calc-check.py` 驗算過，數字沒有問題。
