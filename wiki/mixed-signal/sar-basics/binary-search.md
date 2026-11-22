---
node: mixed-signal/sar-basics
title: 二元搜尋演算法（Binary Search）與秤重比喻
tags: [演算法, 入門]
sources: [kester-mt021, razavi-2015, saxena-lecture]
---
## 一句話
SAR 轉換就像用 32、16、8、4、2、1 磅的砝碼秤一個未知重量：從最大的砝碼開始試，太重就拿掉，不夠重就留下。

## 原理
- 先把 DAC 設在中間值（VREF/2），比較器判斷輸入比它大還小，得到最高位元 MSB。(src: kester-mt021)
- 接著 DAC 依 MSB 結果移到 1/4 或 3/4 量程，判斷下一個位元，一直重複到所有位元決定為止。(src: kester-mt021)
- 每一步都是拿輸入和「目前的估計值」比較，依差值的正負決定往哪邊走，目標是讓殘值小於 1 LSB。(src: razavi-2015)
- 二元搜尋怕早期判斷錯誤：中間某一步判錯，後面的步驟救不回來。(src: saxena-lecture)

## 關鍵數字
- 秤重例子：未知重量 X = 45 lb，砝碼 32、16、8、4、2、1 lb。(src: kester-mt021)
  - X ≥ 32？是 → 留 32（1）
  - X ≥ 48？否 → 拿掉 16（0）
  - X ≥ 40？是 → 留 8（1）
  - X ≥ 44？是 → 留 4（1）
  - X ≥ 46？否 → 拿掉 2（0）
  - X ≥ 45？是 → 留 1（1）
  - 結果 32 + 8 + 4 + 1 = 45，也就是 101101。(src: kester-mt021)
- 這組砝碼最多能秤到 63 lb。(src: kester-mt021)
- 這個砝碼題可以追溯到 1556 年 Tartaglia 提出的 1、2、4、8、16、32 lb 砝碼。(src: kester-mt021)

## 常見誤解 / 衝突
- 「6 次比較就能從 64 種可能中找到答案」是因為每次比較排除一半（推論，由 6 位元 = 2^6 = 64 種碼推得）。

## 相關
[[sar-adc-overview]] [[cdac-charge-redistribution]] [[redundancy-and-calibration]] [[history]]
