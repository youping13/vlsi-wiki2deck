---
node: mixed-signal/basic
deck: adc-basics
title: ADC 基本量：取樣、量化、參數
order: 2
summary: 取樣為什麼會混疊、量化雜訊怎麼決定 SNR 上限、從頻譜讀動態參數、DNL/INL/offset/gain 長什麼樣、INL 為什麼跳
skeleton: 我的 Mixed-Signal 筆記
audience: 一年後的我（學過但忘了）。目的是快速回想，不是入門
style: 每個主題都寫成「動機 → 問題 → 為什麼這樣解 → 代價」；不要比喻和數據比較，計算保留
split_from: decks/sar-adc v3（2026-11-21 22:58 拆成小簡報）
---
## 學習目標（格式：- id | 目標 | 檢索關鍵字）
- g1 | 想起取樣為什麼會混疊、要怎麼限頻 | 取樣, aliasing, 混疊, fs
- g2 | 想起量化雜訊怎麼決定 SNR 上限、沒滿 code 會掉多少 | 量化雜訊, SNR, LSB, 6.02
- g3 | 會從頻譜讀動態參數、會算 ENOB 與 FoM、認得靜態誤差、知道 INL 跳的原因 | SNDR, ENOB, FOM, INL, DNL, dBFS, offset
