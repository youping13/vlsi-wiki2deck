---
node: mixed-signal/sar-basics
id: razavi-2015
title: "A Tale of Two ADCs: Pipelined Versus SAR"
author: Behzad Razavi
venue: IEEE Solid-State Circuits Magazine, Summer 2015
type: 期刊專欄（教學）
url: https://www.seas.ucla.edu/brweb/papers/Journals/BRSummer15ADC.pdf
access: 全文 PDF（作者網站）
ingested: 2026-11-21
---
- 二元搜尋：從 VREF/2 開始，依殘值極性往 3/4、5/8… 逼近，直到殘值 < 1 LSB
- 比較器＋邏輯＋DAC 形成負回授迴路；N 位元要 N 個時脈
- 比較器 offset 只會平移特性曲線，不會造成失真
- 電容 DAC：底板取樣，所以不需要獨立的 SHA；轉換時 X 點電壓就是殘值；結束時 X≈0（虛擬接地）
- 電荷重分配 DAC 沒有靜態功耗
- 速度：轉換時間 ≈ N(tcomp + tlogic + tDAC)
- 10 位元需要 1,024 顆單位電容（全差動 2,048 顆）；電容大小常由匹配決定，而不是 kT/C
- 加速：交錯（interleaving）、一次多位元（最高 3 bit/cycle）、冗餘（redundancy，用來容忍 DAC 沒安定好）
- 橋接電容：8 位元例子只用 31 顆單位電容
- SAR vs pipeline：SAR 不需要 op-amp，比較適合先進製程與低功耗
- 歷史：1947 年 Goodall；CMOS SAR 在 1970 年代出現，2000 年代才因為低功耗重新受到重視
- 冗餘例子：Vin = 12.5 LSB 時誤差 7 LSB，後續步距 5+3+2+1+1 = 12 LSB，可修正 5 LSB 以內的誤差，多花一個週期
- pipeline 用 1.5 bit/stage 容忍 ±VREF/4 的比較器 offset
