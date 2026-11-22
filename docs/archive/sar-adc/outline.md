status: approved
<!-- v3（22:52）：讀者改成「一年後的我」，每頁都是因果鏈或計算；拿掉砝碼比喻和數據比較。 -->

# SAR ADC 回想筆記：從取樣到 monotonic（21 頁）

1. [title] SAR ADC 回想筆記 — goals: — cards:
2. [bullets] 全貌：一條因果鏈 — goals: g1–g6 — cards: c2,c10,c42,c48,c62
**A. ADC 基本量（骨架：我的 Mixed-Signal 筆記）**
3. [causal＋示意圖] 取樣：頻譜每隔 fs 複製 — g1 — c1,c2,c3,c4
4. [calc] 混疊推導：m·fs+Δf 為什麼等於 Δf — g1 — c5,c6,c3
5. [causal＋示意圖] 量化雜訊：SNR 的天花板 — g2 — c8,c9,c10,c11,c12
6. [calc] 沒滿 code，SNR 掉多少 — g2 — c13,c14,c15,c16,c17,c18
7. [diagram＋示意圖] 從頻譜讀動態參數 — g3 — c19,c20,c21,c22,c23,c24
8. [calc] 驗算 ENOB 與 FoM — g3 — c25,c26,c27,c28
9. [causal＋論文 Fig.14] 靜態參數：INL 為什麼在中間跳 — g3 — c30,c31,c32,c33
**B. SAR 與 monotonic（骨架：我的 meeting 報告）**
10. [causal] 為什麼用 SAR — g4 — c34,c35,c36,c37,c41
11. [diagram＋論文 Fig.1] SAR 怎麼運作 — g4 — c38,c39,c37,c40
12. [causal] 傳統切換的問題 — g5 — c42,c43,c44
13. [calc] 能量怎麼算：3-bit 走一遍 — g5 — c49,c50,c51,c52
14. [calc] 平均能量：省 81% 從哪來 — g5 — c53,c54,c55
15. [causal＋論文 Fig.4] monotonic：怎麼解、為什麼省 — g5 — c45,c46,c47,c48,c56
**C. 代價帶來的電路對策**
16. [causal＋論文 Fig.8] 比較器：共模下降 → 動態 offset — g6 — c57,c58,c59,c60,c61
17. [causal＋示意圖] 取樣開關：bootstrap — g6 — c74,c62,c63,c64,c65,c66
18. [causal] Cds 饋通：cross-coupled 電容 — g6 — c67,c68,c69,c70
19. [causal] 實測功耗為什麼比預期高 — g6 — c71,c72,c73
20. [quiz] 自我測驗：monotonic 之後為什麼要改比較器 — g6 — c57,c58,c59
21. [summary] 因果鏈總結 — g1–g6 — c3,c11,c46,c48,c59,c63
<!-- 22:52 由 Claude 依 Percy「全權處理」授權代為確認 v3 大綱（Percy 可隨時改回 draft 重審） -->
