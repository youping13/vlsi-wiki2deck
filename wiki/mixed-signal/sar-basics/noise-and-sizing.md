---
node: mixed-signal/sar-basics
title: 雜訊與電容尺寸（kT/C Noise, Matching）
tags: [雜訊, 設計]
sources: [tang-2022-survey, saxena-lecture, razavi-2015]
---
## 一句話
電容越小越省電、越快，但會被兩件事卡住：熱雜訊 kT/C 和製程失配。

## 原理
- 取樣電容上的熱雜訊功率是 kT/Cdac，電容越大雜訊越小。(src: tang-2022-survey)
- 實務上，電容大小常由匹配需求決定，而不是 kT/C，所以高解析度 SAR 的 DAC 會很大。(src: razavi-2015)
- 電容失配讓中間判斷出錯，二元搜尋本身無法修正。(src: saxena-lecture)
- 設計良好的 SAR 應該是被雜訊限制，而不是被失真限制。(src: tang-2022-survey)

## 關鍵數字
- 1 pF、300 K 的 kT/C 雜訊約 64 µV rms。(src: tang-2022-survey)
- 1 V p-p 輸入、10 位元至少要 52 fF；14 位元要大於 13 pF。(src: tang-2022-survey)
- 16 位元、Cmin = 10 fF 時，若以匹配決定尺寸，陣列要約 655 pF；從 kT/C 角度看約 100 pF 就合理。(src: saxena-lecture)
- 客製 MOM 電容的單位值可小到 0.5 fF。(src: tang-2022-survey)

## 常見誤解 / 衝突
- 「655 pF」與「100 pF」不是矛盾：前者是匹配的要求，後者是雜訊的要求，取兩者較大的那個（推論）。

## 相關
[[cdac-charge-redistribution]] [[redundancy-and-calibration]] [[figures-of-merit]]
