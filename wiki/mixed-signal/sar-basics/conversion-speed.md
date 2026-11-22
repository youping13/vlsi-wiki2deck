---
node: mixed-signal/sar-basics
title: 轉換速度與時序（Conversion Speed, Async SAR）
tags: [時序, 速度]
sources: [kester-mt021, razavi-2015, saxena-lecture, tang-2022-survey]
---
## 一句話
SAR 每個時脈只決定一個位元，所以位元越多越慢；而且每一步 DAC 都要安定到足夠精度，高解析度又更慢。

## 原理
- 每個位元的週期由三段組成：比較器反應時間、邏輯延遲、DAC 安定時間。(src: razavi-2015)
- DAC 必須在每次判斷前安定到 N 位元精度：16 位元要安定到 16 位元精度，比 8 位元久得多。(src: kester-mt021)
- DAC 要在時間內安定到 ±½ LSB。(src: saxena-lecture)
- 一個時脈約一半時間給電荷重分配，一半給比較和數位邏輯。(src: saxena-lecture)
- 非同步 SAR 自己產生內部時脈，只需要取樣頻率的主時脈。(src: saxena-lecture, tang-2022-survey)
- 加速方法：交錯（interleaving）、一次決定多個位元、冗餘（容忍 DAC 沒安定好）。(src: razavi-2015)

## 關鍵數字
- 轉換時間 ≈ N(tcomp + tlogic + tDAC)。(src: razavi-2015)
- 8 位元 SAR 約數百 ns，16 位元約數 µs。(src: kester-mt021)
- 一次多位元的做法最高展示到 3 bit/cycle。(src: razavi-2015)
- 交錯的極端例子：8 位元 56 GS/s 用了 320 個 175 MS/s 的 SAR 通道。(src: saxena-lecture)

## 常見誤解 / 衝突
- 誤解：「16 位元只比 8 位元慢 2 倍」。週期數是 2 倍，但每一步的安定時間也變長。(src: kester-mt021)

## 相關
[[sar-adc-overview]] [[redundancy-and-calibration]] [[sar-vs-pipeline]]
