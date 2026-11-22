---
node: mixed-signal/sar-basics
id: kester-mt021
title: "MT-021 Tutorial — ADC Architectures II: Successive Approximation ADCs"
author: Walt Kester (Analog Devices)
year: 2008 (Rev. A, 10/08)
type: 廠商教材
url: https://web.eng.fiu.edu/watsonh/eel4730/Appendix/MT-021.pdf
access: 全文 PDF（公開）
ingested: 2026-11-21
---
- 基本架構四塊：SHA、比較器、DAC、SAR 邏輯；圖 1 稱為 feedback subtraction ADC
- 演算法：DAC 先設中間值，比較器決定 MSB，再設 1/4 或 3/4 量程，依此類推
- 秤重比喻：32/16/8/4/2/1 lb 砝碼量 45 lb → 101101
- N 位元要 N 步；DAC 必須安定到 N 位元精度，所以 16 位元遠比 8 位元慢（8 位元約數百 ns，16 位元約數 µs）
- 沒有 pipeline delay，適合單次轉換與多工通道
- 3 位元開關電容 DAC：C、C/2、C/4 加一顆額外的 C/4，總和 2C
- 歷史：1556 年 Tartaglia 的砝碼題、1947 年 Goodall 5 位元 8 kSPS、「SAR ADC」一詞出現在 1970 年代（2502/2503/2504 SAR 邏輯 IC）、1978 年 AD574
- 精度主要由內部 DAC 決定；開關電容 DAC 的匹配靠黃光製程
- 來源本身的不一致：DATRAC 圖說寫 1954／50 kSPS，內文寫 1955
- 這組砝碼實際上最多能秤到 63 lb（原題目說 40 lb）
- 1978 年 AD574：單晶片 12 位元、35 µs，1980 年代初成為業界標準 12 位元 ADC
