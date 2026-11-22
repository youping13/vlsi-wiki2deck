---
node: mixed-signal/sar-basics
title: 冗餘與校正（Redundancy, Calibration）
tags: [精度, 設計]
sources: [razavi-2015, tang-2022-survey, saxena-lecture, kester-mt021]
---
## 一句話
冗餘是「多花一步，換取改錯的機會」；校正是「量出電容誤差，再用電路或數位方式補回去」。

## 原理
- 冗餘讓前面判錯的結果可以在後面修正，常用來容忍 DAC 沒完全安定。(src: razavi-2015, tang-2022-survey)
- 冗餘要多花週期，修正範圍也要夠大。(src: razavi-2015)
- 非二進位的步距可以在暫存器後面接一張查表（look-up table）轉回二進位碼。(src: razavi-2015)
- 講義提到用非二進位搜尋演算法處理「判錯救不回」的問題。(src: saxena-lecture)
- 校正方式：類比自我校正（額外的子 DAC 加 RAM）、LMS 數位權重估計、mismatch error shaping。(src: tang-2022-survey)
- 開關電容 DAC 可以並聯小電容，在自動校正時切換來修正，不需要雷射修整。(src: kester-mt021)

## 關鍵數字
- Razavi 的例子：Vin = 12.5 LSB 時誤差 7 LSB，後續步距 5+3+2+1+1 = 12 LSB，可修正到 5 LSB 的誤差，代價是多一個週期。(src: razavi-2015)

## 常見誤解 / 衝突
- 二元搜尋「判錯就救不回」是指純二進位、沒有冗餘的情況；加了冗餘就可以修。(src: saxena-lecture, razavi-2015)

## 相關
[[binary-search]] [[conversion-speed]] [[noise-and-sizing]]
