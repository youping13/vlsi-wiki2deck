---
node: mixed-signal/sar-basics
title: "MT-021 Tutorial — ADC Architectures II: Successive Approximation ADCs"
id: kester-mt021
author: Walt Kester (Analog Devices)
year: 2008 (Rev. A, 10/08)
type: 廠商教材
url: https://web.eng.fiu.edu/watsonh/eel4730/Appendix/MT-021.pdf
access: 全文 PDF（公開）
ingested: 2026-11-21
---
## 一句話
ADI 的 SAR ADC 入門教材：架構、秤重演算法、開關電容 DAC 與 SAR 的歷史。

## 論述

**在解決什麼**：工程師要選 ADC 時，需要先搞懂 SAR 這種架構「怎麼一位一位決定出數位碼」，以及速度和精度被什麼卡住。

**怎麼講**：這份 ADI 教材先把 SAR 拆成四個方塊（SHA、比較器、DAC、SAR 邏輯），用秤砝碼的例子走一遍二元搜尋，再把 DAC 換成開關電容陣列，說明取樣和比較怎麼在同一排電容上完成。最後回顧歷史：演算法很早就有，1970 年代才出現「SAR ADC」這個名字和第一批邏輯 IC。

**為什麼重要**：它把「N 位元要 N 步」和「每一步 DAC 都要安定到 N 位元精度」放在一起講，所以讀完就知道：位元越多，不只步數多，每一步也更慢。

**限制**：偏廠商實務角度，沒有低功耗切換或比較器雜訊的分析；本身也有年份前後不一致的小錯（DATRAC 1954 vs 1955）。

**一年後要記得**：SAR = 比較器＋DAC＋邏輯組成的回授迴路，精度主要由內部 DAC 決定。

## 重點
- 基本架構四塊：SHA、比較器、DAC、SAR 邏輯；圖 1 稱為 feedback subtraction ADC
- 演算法：DAC 先設中間值，比較器決定 MSB，再設 1/4 或 3/4 量程，依此類推
- 秤重比喻：32/16/8/4/2/1 lb 砝碼量 45 lb → 101101
- N 位元要 N 步；DAC 必須安定到 N 位元精度，所以 16 位元遠比 8 位元慢（8 位元約數百 ns，16 位元約數 µs）
- 沒有 pipeline delay，適合單次轉換與多工通道
- 3 位元開關電容 DAC：C、C/2、C/4 加一顆額外的 C/4，總和 2C
- 歷史：1556 年 Tartaglia 的砝碼題、1947 年 Goodall 5 位元 8 kSPS、「SAR ADC」一詞出現在 1970 年代（2502/2503/2504 SAR 邏輯 IC）、1978 年 AD574
- 精度主要由內部 DAC 決定；開關電容 DAC 的匹配靠黃光製程
- 來源本身的不一致：DATRAC 圖說寫 1954／50 kSPS，內文寫 1955

## 可信度
- 高：廠商官方教材，偏實務、入門友善。注意本身有年份前後不一致。

## 被哪些概念頁引用
[[binary-search]] [[cdac-charge-redistribution]] [[conversion-speed]] [[history]] [[redundancy-and-calibration]] [[sar-adc-overview]]
