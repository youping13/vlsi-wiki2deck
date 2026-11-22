---
node: mixed-signal/sar-basics
title: "A Hybrid Energy-Efficient, Area-Efficient, Low-Complexity Switching Scheme in SAR ADC for Biosensor Applications"
id: hu-2024-hybrid
author: Yunfeng Hu, Chaoyi Chen, Qingming Huang, Lexing Hu, Bin Tang, Mengsi Hu, Bingbing Yuan, Zhaohui Wu, Bin Li
venue: Micromachines, vol. 15, no. 1, 60 (2024; online 2023-12-27)
doi: 10.3390/mi15010060
type: 期刊論文（Open Access）
url: https://www.mdpi.com/2072-666X/15/1/60
access: 摘要（全文頁被驗證頁擋住，未取得表格）
ingested: 2026-11-21
---
## 一句話
生醫用的超低功耗 SAR：混合式切換，切換能量少 98.4%、單位電容少 87.5%。

## 論述

**在解決什麼**：生醫感測器的 ADC 很慢（100 kS/s）但要極省電，DAC 的切換能量和電容面積是主要負擔。

**怎麼做**：在 monotonic 的基礎上，再把 MSB 電容分割，並加入新的切換方法。除了少數幾次比較，其餘都是單邊切換，DAC 的驅動電路因此比較簡單。

**為什麼有效**：沿用 monotonic「先比再切、只切一邊」的思路，再用電容分割進一步減少每一步要搬的電荷，所以切換能量比傳統少 98.4%、單位電容少 87.5%。

**限制**：只取得摘要；應用在低速生醫，數字不能直接拿來跟 50 MS/s 的設計比。切換能量省 98% 也不代表整顆 ADC 省這麼多，比較器和邏輯照樣耗電。

**一年後要記得**：monotonic 之後的切換方式，大多是「monotonic＋電容分割」的變形。

## 重點
- 結合 monotonic、MSB 電容分割，加上新的切換方法
- 相對傳統切換：切換能量少 98.4%，單位電容少 87.5%
- 除了第 2 次與最後 2 次比較，其餘都是單邊切換，DAC 驅動電路比較簡單
- 180 nm、1 V、100 kS/s、SNDR 61.51 dB、SFDR 79.21 dB、0.278 µW
- 用途：生醫感測器（低速、超低功耗）

## 可信度
- 中：OA 期刊一手論文，只取得摘要；應用在低速生醫，數字不能直接拿來和 50 MS/s 設計比較。

## 被哪些概念頁引用
[[switching-schemes]]
