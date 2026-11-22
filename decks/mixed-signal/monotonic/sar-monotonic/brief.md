---
node: mixed-signal/monotonic
deck: sar-monotonic
title: SAR 與 monotonic：為什麼省 81%
order: 2
summary: 為什麼用 SAR、傳統切換哪裡浪費、ΔQ 能量推導、monotonic 怎麼省與代價
skeleton: 我的專題 meeting 1
audience: 一年後的我（學過但忘了）。目的是快速回想，不是入門
style: 每個主題都寫成「動機 → 問題 → 為什麼這樣解 → 代價」；不要比喻和數據比較，計算保留
split_from: decks/sar-adc v3（2026-11-21 22:58 拆成小簡報）
---
## 學習目標（格式：- id | 目標 | 檢索關鍵字）
- g4 | 想起為什麼用 SAR、它怎麼運作 | 靜態功耗, op-amp, pipeline, 二元搜尋, VX
- g5 | 想起 monotonic 解決什麼、怎麼算出省 81%、代價是什麼 | monotonic, ΔQ, 切換能量, Vcm, trial-and-error
