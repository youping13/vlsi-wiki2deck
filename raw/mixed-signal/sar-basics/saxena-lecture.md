---
node: mixed-signal/sar-basics
id: saxena-lecture
title: "Successive Approximation ADCs (lecture slides)"
author: Vishal Saxena (Boise State University)
year: 2014
type: 大學課程講義
url: https://www.eecis.udel.edu/~vsaxena/courses/ece614/Handouts/SAR%20ADC%202014.pdf
access: 全文 PDF（公開）
ingested: 2026-11-21
note: 部分方程式在文字萃取時破碎，只收錄可辨識的部分
---
- SAR = 對 DAC 輸入做二元搜尋；N 位元需要 N·Tclk；典型速度 0.1–10 MHz；可做到 16 位元以上，但需要很準的比較器
- 一旦中間某次判斷錯誤，二元搜尋就救不回來
- 4 位元電荷重分配例子：8C、4C、2C、C、C，總和 16C；MSB 測試 VX = Vi − VR/2，次位元 VX = Vi − 3VR/4
- 約一半 Tclk 給電荷重分配，一半給比較與邏輯
- 寄生電容 CP：offset 為 0 時不影響結果；等效輸入 offset ≈ (1 + CP/ΣCj)·Vos
- 同步 SAR 只有比較器吃直流功率（講義的說法）
- 尺寸：Cmin = 10 fF 時，16 位元陣列要 2^16·Cmin ≈ 655 pF；從 kT/C 角度看，約 100 pF 就合理
- DAC 必須在時間內安定到 ±½ LSB
- monotonic switching 可省 81% 切換能量；共模電壓會逐漸往地收斂
- 非同步 SAR：自我計時，只需要取樣頻率的主時脈
- 優點：大部分是數位電路、會隨製程縮小、不需要高精度線性放大器、只用一個比較器
- 交錯例子：Fujitsu 8 位元 56 GS/s，用 320 個 175 MS/s 的 SAR 通道
