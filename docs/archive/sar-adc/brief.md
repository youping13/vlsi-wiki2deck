---
deck: sar-adc
category: 全集
order: 9
summary: 上面三份合在一起的完整版（作業繳交用），21 頁
title: SAR ADC 回想筆記：從取樣到 monotonic
audience: 一年後的我（學過但忘了）。目的是快速回想，不是入門
style: 每個主題都寫成「動機 → 問題 → 為什麼這樣解 → 代價」；不要比喻和數據比較，計算保留
version: v3（2026-11-21 22:50，依 Percy 的新要求改寫；v1/v2 的版本見 docs/run-2026-11-21.md）
---
## 學習目標（格式：- id | 目標 | 檢索關鍵字）
- g1 | 想起取樣為什麼會混疊、要怎麼限頻 | 取樣, aliasing, 混疊, fs
- g2 | 想起量化雜訊怎麼決定 SNR 上限、沒滿 code 會掉多少 | 量化雜訊, SNR, LSB, 6.02
- g3 | 會從頻譜讀動態參數、會算 ENOB 與 FoM、知道 INL 跳的原因 | SNDR, ENOB, FOM, INL, DNL
- g4 | 想起為什麼用 SAR、它怎麼運作 | 靜態功耗, op-amp, pipeline, 二元搜尋, VX
- g5 | 想起 monotonic 解決什麼、怎麼算出省 81%、代價是什麼 | monotonic, ΔQ, 切換能量, Vcm, trial-and-error
- g6 | 想起代價帶來的電路對策：比較器、bootstrap、cross-coupled | dynamic offset, bootstrap, Cds, 電流源, cross-coupled
