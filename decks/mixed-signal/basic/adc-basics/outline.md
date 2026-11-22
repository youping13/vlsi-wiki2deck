status: approved
<!-- 22:58 由 decks/sar-adc v3 已確認的大綱拆出，頁序與卡片不變（Claude 依 Percy 授權代為確認） -->

# ADC 基本量：取樣、量化、參數（11 頁）

0. [title] ADC 基本量：架構、取樣、量化、參數
3. [causal＋示意圖] 取樣：頻譜每隔 fs 複製 — g1 — c1,c2,c3,c4
4. [calc] 混疊推導：m·fs+Δf 為什麼等於 Δf — g1 — c5,c6,c3
5. [causal＋示意圖] 量化雜訊：SNR 的天花板 — g2 — c8,c9,c10,c11,c12
6. [calc] 沒滿 code，SNR 掉多少 — g2 — c13,c14,c15,c16,c48,c17,c18
7. [diagram＋示意圖] 從頻譜讀動態參數 — g3 — c19,c20,c21,c22,c23,c24
7b. [diagram＋meeting 圖] SFDR：dBc 還是 dBFS — g3 — c22,c54,c55
8. [calc＋論文 Fig.15] 驗算 ENOB 與 FoM — g3 — c25,c26,c27,c28
9a. [diagram＋meeting 圖] 靜態誤差：DNL 與 INL — g3 — c49,c50,c53
9b. [diagram＋meeting 圖] 靜態誤差：Offset 與 Gain — g3 — c51,c52
9. [causal＋論文 Fig.14] 靜態參數：INL 為什麼在中間跳 — g3 — c30,c31,c32,c33

<!-- 2026-11-22 22:15 v4：依 Percy 要求加入 meeting 附錄 A 的各種 ADC 介紹（a1–a3）。大綱改了，status 退回 draft -->
<!-- 22:15 Claude 依授權代為確認 v4（Percy 可改回 draft 重審） -->

<!-- 2026-11-22 22:27 Percy 核對手寫轉錄 p3：B 的 55.9 dB 是用 P_signal/P_noise 算的 → 重做 c16、新增 c48，只改算例那一頁 -->

<!-- 2026-11-22 23:30 v5：Percy 要求「圖片才是重點」→ 架構 a1–a3 拆到 adc-architectures；加 meeting 1 的圖（7b、9a、9b）與 Fig.15。Claude 依授權代為確認（Percy 可改回 draft 重審） -->
