---
node: mixed-signal/basic
title: 效能指標（Figures of Merit：ENOB、SNDR、Walden FoM）
tags: [指標]
sources: [tang-2022-survey, liu-2010-monotonic]
---
## 一句話
FoM 回答的是「每轉換一個有效量化階，要花多少能量」，數字越小越好。

## 原理
- Walden FoM = P / (2·BW·2^ENOB)，單位是 J/conversion-step。(src: tang-2022-survey)
- ENOB（有效位元數）是由實測 SNDR 換算的「真正有用的位元數」，通常小於設計位元數，例如成大的 10 位元晶片實測 ENOB 9.18 bits。(src: liu-2010-monotonic)
- 高解析度（13 位元以上）常改用 Schreier FoM，因為類比電路主導功耗。(src: tang-2022-survey)

## 關鍵數字
- 最佳 ADC 效率：2000 年約 3 pJ/conversion-step → 2019 年約 0.4 fJ/conversion-step，約 7,500 倍。(src: tang-2022-survey)
- 其中製程縮小約貢獻 100 倍，其餘約 75 倍來自架構與電路創新。(src: tang-2022-survey)
- 例：成大 monotonic SAR 的 FoM 為 29 fJ/conversion-step。(src: liu-2010-monotonic)
- 低到中速 SAR 的製程甜蜜點是 90 nm 到 55 nm。(src: tang-2022-survey)

## 常見誤解 / 衝突
- 製程越先進不一定越省電：28 nm 以下的 FinFET 主要提升速度，因為熱雜訊不會跟著製程縮小。(src: tang-2022-survey)

## 相關
[[switching-schemes]] [[noise-and-sizing]] [[sar-adc-overview]]
