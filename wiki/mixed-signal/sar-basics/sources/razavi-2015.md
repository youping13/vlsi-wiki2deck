---
node: mixed-signal/sar-basics
title: "A Tale of Two ADCs: Pipelined Versus SAR"
id: razavi-2015
author: Behzad Razavi
venue: IEEE Solid-State Circuits Magazine, Summer 2015
type: 期刊專欄（教學）
url: https://www.seas.ucla.edu/brweb/papers/Journals/BRSummer15ADC.pdf
access: 全文 PDF（作者網站）
ingested: 2026-11-21
---
## 一句話
Razavi 用教學角度比較 pipeline 與 SAR：二元搜尋、電容 DAC、速度極限、冗餘。

## 論述

**在解決什麼**：pipeline 和 SAR 都能做中高速 ADC，到底差在哪、什麼時候該選哪個？

**怎麼講**：Razavi 把兩種架構並排比較。SAR 是一個比較器重複用 N 次，DAC 的電容在底板取樣，轉換時頂板電壓就是殘值；pipeline 是很多級同時做，每一級都需要 op-amp 把殘值放大。

**為什麼重要**：關鍵差異是 op-amp。先進製程、低電壓下高增益 op-amp 很難做，SAR 不需要 op-amp，電荷重分配 DAC 也沒有靜態功耗，所以 SAR 在低功耗時代翻身。文中也說明 SAR 的弱點和補救：沒有殘值放大，比較器雜訊直接限制解析度；速度則用交錯、一次多位元、冗餘來補。

**限制**：是教學專欄，不涉及電路細節和量測；沒有給出「幾位元以上用 pipeline」的明確分界。

**一年後要記得**：SAR 贏在不需要 op-amp、沒有靜態功耗；輸在比較器雜訊和串列的速度。

## 重點
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

## 可信度
- 高：領域權威的教學專欄，觀念清楚；不含能量公式。

## 被哪些概念頁引用
[[binary-search]] [[cdac-charge-redistribution]] [[comparator]] [[conversion-speed]] [[history]] [[noise-and-sizing]] [[redundancy-and-calibration]] [[sar-adc-overview]] [[sar-vs-pipeline]]
