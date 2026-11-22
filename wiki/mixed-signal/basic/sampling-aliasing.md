---
node: mixed-signal/basic
title: 取樣與混疊（Sampling, Aliasing）
tags: [基礎, 訊號]
sources: [percy-ms-notes]
---
## 一句話
取樣就是把原頻譜每隔 fs 複製一次；複製品一旦疊在一起，就分不出原本的頻率（aliasing）。

## 因果鏈
- 動機：ADC 只能處理離散時間的值，所以要先取樣。(src: percy-ms-notes)
- 問題：取樣會把頻譜每隔 fs 複製一次，頻率 m·fs + Δf 和 Δf 取樣後變成同一個序列。(src: percy-ms-notes)
- 結論：輸入頻寬必須限制在 fs/2 以內，否則高頻會折回低頻（推論，依 Nyquist）。

## 原理
- 理想取樣：x_s(t) 仍是 continuous，只是在其它地方是 0；資訊量沒有改變。(src: percy-ms-notes)
- 時域：$x_s(t) = x(t)\sum_n \delta(t-nT_s) = \sum_n x(nT_s)\,\delta(t-nT_s)$ (src: percy-ms-notes)
- 脈衝串展開：$\sum_n \delta(t-nT_s) = \frac{1}{T_s}\sum_k e^{j2\pi k f_s t} \;\xrightarrow{\mathcal{F}}\; \frac{1}{T_s}\sum_k \delta(f-kf_s)$ (src: percy-ms-notes)
- 頻域：$X_s(f) = \frac{1}{T_s}\sum_{k=-\infty}^{\infty} X(f-kf_s)$，把原頻譜每隔 fs 複製一次。(src: percy-ms-notes)

## 關鍵數字
- 混疊推導：$x[n] = \cos\!\left(2\pi\frac{mf_s+\Delta f}{f_s}n\right) = \cos(2\pi mn \pm 2\pi\frac{\Delta f}{f_s}n) = \cos\!\left(2\pi\frac{\Delta f}{f_s}n\right)$ (src: percy-ms-notes)
- 2πmn 是 2π 的整數倍，所以可以消掉。(src: percy-ms-notes)

## 常見誤解 / 衝突
- 「取樣會失去資訊」：理想取樣不會，筆記明確寫資訊量沒有改變；會失去資訊的是 aliasing 和量化。(src: percy-ms-notes)

## 相關
[[quantization-noise-snr]] [[adc-dynamic-parameters]]
