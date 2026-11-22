---
node: mixed-signal/sar-basics
title: 電容 DAC 與電荷重分配（Capacitive DAC, Charge Redistribution）
tags: [電路, DAC]
sources: [kester-mt021, razavi-2015, saxena-lecture, tang-2022-survey]
---
## 一句話
用一排二進位比例的電容同時當取樣器和 DAC：切換電容底板接 VREF 或地，頂板電壓就等於「估計值 − 輸入」。

## 原理
- 取樣：所有電容底板接輸入、頂板接地，電容把輸入電壓「記」下來（底板取樣）。(src: razavi-2015)
- 轉換：把最大電容的底板切到 VREF、其他接地，頂板 X 點的電壓就是殘值。比較器只要看 X 點的正負。(src: razavi-2015)
- 判斷 MSB 時 VX = Vi − VR/2，判斷次位元時 VX = Vi − 3VR/4。(src: saxena-lecture)
- 某個位元切到 VREF 就會把它的權重加到 X 點；切到地就把同樣的電壓減掉。運作方式類似 R-2R 電阻 DAC。(src: kester-mt021)
- 轉換結束時 X 點會收斂到接近 0，相當於虛擬接地，這樣可以避開開關的非線性接面電容。(src: razavi-2015)
- 電荷重分配 DAC 沒有靜態功耗，這是 SAR 省電的關鍵之一。(src: razavi-2015)
- 製程縮小後，除了經典的底板取樣，bootstrapped 頂板取樣也變得常見。(src: tang-2022-survey)

## 關鍵數字
- 3 位元例子：C、C/2、C/4，再加一顆額外的 C/4，總和 2C；多出的那顆讓二分比例成立。(src: kester-mt021)
- 4 位元例子：8C、4C、2C、C、C，總和 16C。(src: saxena-lecture)
- 10 位元需要 1,024 顆單位電容，全差動要 2,048 顆。(src: razavi-2015)
- 用橋接電容（bridge capacitor）可以縮小陣列：8 位元例子只用 31 顆單位電容。(src: razavi-2015)

## 常見誤解 / 衝突
- 寄生電容 CP 會衰減 X 點電壓，但比較器沒有 offset 時不影響最終結果；有 offset 時，等效輸入 offset ≈ (1 + CP/ΣCj)·Vos。(src: saxena-lecture)
- DAC 另一端的寄生只會造成增益誤差，在 SAR 裡可以容忍。(src: razavi-2015)

## 相關
[[sar-adc-overview]] [[switching-schemes]] [[noise-and-sizing]] [[comparator]]
