---
node: mixed-signal/basic
title: ADC 動態參數（SNR、THD、SFDR、SNDR、ENOB、dBc/dBFS、FoM）
tags: [指標, 計算]
sources: [percy-meeting1, liu-2010-monotonic, tang-2022-survey]
---
## 一句話
動態參數都是從同一張 FFT 頻譜讀出來的：訊號、諧波、最大雜散、雜訊地板，各取一組比值。

## 因果鏈
- 動機：靜態的 DNL/INL 看不出高頻時 ADC 表現多差，要用正弦波輸入、看 FFT。(src: percy-meeting1)
- 問題：頻譜上同時有雜訊和諧波，單一個數字不夠，所以分成 SNR、THD、SFDR、SNDR。(src: percy-meeting1)
- 結論：SNDR 最能代表實際表現，再換算成 ENOB；FoM 再把功耗放進來。(src: percy-meeting1)

## 原理
- $\mathrm{SNR(dB)} = 10\log_{10}\frac{P_{signal}}{P_{noise}}$ (src: percy-meeting1)
- $\mathrm{THD(dB)} = 10\log_{10}\frac{P_{harmonics}}{P_{signal}}$ (src: percy-meeting1)
- $\mathrm{SFDR(dBc)} = 10\log_{10}\frac{P_{signal}}{P_{max\_spur}}$ (src: percy-meeting1)
- $\mathrm{SNDR(dB)} = 10\log_{10}\frac{P_{signal}}{P_{noise}+P_{harmonics}}$ (src: percy-meeting1)
- $\mathrm{ENOB(bits)} = \frac{\mathrm{SNDR}-1.76}{6.02}$ (src: percy-meeting1)
- dBc 是相對載波（輸入訊號），dBFS 是相對滿刻度。(src: percy-meeting1)
- $\mathrm{FOM} = \frac{\mathrm{Power}}{2^{\mathrm{ENOB}}\times \min\{2\times \mathrm{ERBW},\, f_s\}}$ (src: percy-meeting1)
- 綜述用的 Walden FoM = P / (2·BW·2^ENOB)，單位 J/conversion-step。(src: tang-2022-survey)
- 高頻劣化原因：clock jitter、dynamic non-linearity（寄生電容）、settling time failure。(src: percy-meeting1)

## 關鍵數字
- Liu 2010 實測：低頻 SNDR 57.0 dB、ENOB 9.18 bits、FoM 29 fJ/conversion-step、50 MS/s、0.826 mW (src: liu-2010-monotonic)
- 驗算 ENOB：(57.0 − 1.76)/6.02 = 9.18 bits（計算）
- 驗算 FoM：2^9.18 ≈ 580；0.826 mW / (580 × 50 MHz) ≈ 28.5 fJ，四捨五入就是論文的 29 fJ（計算）

## 常見誤解 / 衝突
- meeting 時對 FFT 留下的疑問：DC component？second harmonic 20M？(src: percy-meeting1) 輸入 10 MHz、取樣 50 MS/s，二次諧波 20 MHz 仍在 Nyquist 25 MHz 以內，所以直接出現在 20 MHz；三次諧波 30 MHz 會折回到 20 MHz 附近（推論，依 aliasing）。
- dBc 和 dBFS 差的就是「輸入離滿刻度多遠」，比較兩份 SFDR 要先確認單位。(src: percy-meeting1)

## 相關
[[quantization-noise-snr]] [[adc-static-parameters]] [[figures-of-merit]] [[sampling-aliasing]]
