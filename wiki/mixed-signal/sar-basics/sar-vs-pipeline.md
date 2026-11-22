---
node: mixed-signal/sar-basics
title: SAR 與 Pipeline ADC 比較（SAR vs. Pipelined）
tags: [架構比較]
sources: [razavi-2015, saxena-lecture, tang-2022-survey]
---
## 一句話
Pipeline 是「很多級同時做」，靠 op-amp 放大殘值；SAR 是「一級重複用 N 次」，不需要 op-amp。

## 原理
- Pipeline 由多個 MDAC 級同時運作；SAR 只用一級，重複 N 個週期。(src: razavi-2015)
- Pipeline 需要 op-amp，op-amp 的增益和線性度會限制效能；SAR 不需要 op-amp。(src: razavi-2015)
- 在先進製程、低電壓下 op-amp 很難做，這是 SAR 受歡迎的原因之一。(src: razavi-2015)
- SAR 大部分是數位電路，會隨製程縮小。(src: saxena-lecture)
- 綜述提到 pipelined-SAR、noise-shaping SAR 等混合架構是下一步的方向。(src: tang-2022-survey)

## 關鍵數字
- Pipeline 每級只需要兩顆電容；SAR 需要 2^N 顆單位電容（10 位元 1,024 顆）。(src: razavi-2015)
- Pipeline 用 1.5 bit/stage 容忍比較器 offset；SAR 用冗餘容忍 DAC 安定誤差。(src: razavi-2015)

## 常見誤解 / 衝突
- 文章沒有給出「幾位元以上用 pipeline」的明確分界點。(src: razavi-2015)

## 相關
[[sar-adc-overview]] [[conversion-speed]] [[redundancy-and-calibration]]
