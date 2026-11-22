---
node: mixed-signal/sar-basics
title: SAR ADC 總覽（Successive Approximation Register ADC）
tags: [架構, 入門]
sources: [kester-mt021, razavi-2015, saxena-lecture, tang-2022-survey, liu-2010-monotonic]
---
## 一句話
SAR ADC 用「猜一個值 → 比大小 → 修正」的二元搜尋，把類比電壓一位一位轉成數位碼。

## 原理
- SAR ADC 由四個主要電路組成：取樣保持（SHA）、比較器（comparator）、內部 DAC、逐次逼近暫存器（SAR 邏輯）。(src: kester-mt021)
- SAR 這個縮寫本來指的是控制轉換的那塊邏輯（successive approximation register），後來大家拿它來稱呼整個架構。(src: kester-mt021)
- 比較器、邏輯和 DAC 組成一個負回授迴路，DAC 的輸出會一步步逼近取樣到的輸入。(src: razavi-2015)
- 用開關電容 DAC 時，DAC 的電容本身就能取樣輸入，所以不需要另外一顆 SHA。(src: razavi-2015)
- 每次轉換的結果在轉換結束時就能拿到，沒有 pipeline delay，很適合多通道輪流轉換。(src: kester-mt021)

## 關鍵數字
- N 位元需要 N 個時脈週期。(src: razavi-2015, saxena-lecture)
- 典型速度 0.1–10 MHz，可做到 16 位元以上。(src: saxena-lecture)
- 優化良好的設計中，比較器、DAC、SAR 邏輯三者的功耗差不多。(src: tang-2022-survey)

## 常見誤解 / 衝突
- 功耗分配因設計而異：綜述說三者相近 (src: tang-2022-survey)；成大的 50 MS/s 晶片是數位 0.42 mW、類比 0.276 mW、參考電壓 0.13 mW。(src: liu-2010-monotonic)
- 誤解：「SAR」是架構的名字。其實是暫存器的名字。(src: kester-mt021)
- 講義說同步 SAR「只有比較器吃直流功率」(src: saxena-lecture)；綜述則提醒，數位邏輯的漏電在奈瓦級設計中仍可能占約 25%。(src: tang-2022-survey) 兩者並不矛盾：前者講的是動態功率結構，後者講的是極低功耗時的漏電。

## 相關
[[binary-search]] [[cdac-charge-redistribution]] [[comparator]] [[conversion-speed]] [[sar-vs-pipeline]] [[monotonic-sar-case-study]]
