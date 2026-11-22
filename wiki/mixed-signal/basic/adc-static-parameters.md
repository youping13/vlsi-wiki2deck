---
node: mixed-signal/basic
title: ADC 靜態參數（LSB、DNL、INL、Gain/Offset Error）
tags: [指標]
sources: [percy-meeting1, liu-2010-monotonic]
---
## 一句話
靜態參數看的是轉換曲線「每一階寬度對不對」（DNL）和「整條線歪了多少」（INL、gain、offset）。

## 因果鏈
- 動機：電容失配會讓某些碼特別寬或特別窄，要量出來。(src: percy-meeting1)
- 問題：Liu 的晶片 INL 在中間碼 0111111111 → 1000000000 跳動。(src: percy-meeting1)
- 原因：佈線寄生讓 MSB 電容大了約 1 LSB；中間碼正是 MSB 翻轉的位置。(src: liu-2010-monotonic)
- 代價：效能主要受這個固定的電容失配限制。(src: liu-2010-monotonic)

## 原理
- 1 LSB = (Vref − Vgnd)/2^N；例：5 V、10 bits → 5/1024 = 4.88 mV (src: percy-meeting1)
- 靜態誤差：DNL、INL、gain error、offset error (src: percy-meeting1)
- 動態參數看頻譜，靜態參數看轉換曲線，兩者互補。(src: percy-meeting1)

## 關鍵數字
- Liu 2010：峰值 DNL 0.91/−0.63 LSB，INL 1.27/−1.36 LSB (src: liu-2010-monotonic)

## 常見誤解 / 衝突
- INL 的跳動不是隨機雜訊，每顆測試晶片都有，所以是佈線造成的固定誤差。(src: liu-2010-monotonic)

## 相關
[[adc-dynamic-parameters]] [[cdac-charge-redistribution]] [[monotonic-sar-case-study]]
