---
node: mixed-signal/sar-basics
title: SAR ADC 簡史（History）
tags: [歷史]
sources: [kester-mt021, razavi-2015]
---
## 一句話
演算法比電子學還老：16 世紀的砝碼題，到 1940 年代貝爾實驗室，再到今天手機和感測器裡的 SAR。

## 原理
- 早期的 SAR 叫做 sequential coder、feedback coder 或 feedback subtractor coder。(src: kester-mt021)
- CMOS SAR 在 1970 年代就有報告，但一直到 2000 年代才因為低功耗潛力重新受到重視。(src: razavi-2015)

## 關鍵數字
- 1556 年：Tartaglia 的砝碼題（1、2、4、8、16、32 lb）。(src: kester-mt021)
- 1947 年：貝爾實驗室 Goodall 的 5 位元、8 kSPS 語音通道 SAR。(src: kester-mt021, razavi-2015)
- 1970 年代：「SAR ADC」這個名詞隨 2502、2503、2504 SAR 邏輯 IC 出現。(src: kester-mt021)
- 1978 年：AD574，12 位元、35 µs，1980 年代初成為業界標準。(src: kester-mt021)

## 常見誤解 / 衝突
- Gordon 的 DATRAC：圖說寫 1954 年、50 kSPS，內文寫 1955 年。(src: kester-mt021) 來源本身前後不一致，兩個都保留。

## 相關
[[binary-search]] [[sar-adc-overview]]
