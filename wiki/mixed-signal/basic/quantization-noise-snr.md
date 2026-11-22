---
node: mixed-signal/basic
title: 量化雜訊與 SNR（Quantization Noise, SNR = 6.02N + 1.76）
tags: [基礎, 雜訊, 計算]
sources: [percy-ms-notes, percy-meeting1, tang-2022-survey]
---
## 一句話
量化雜訊是 ADC 一定會有的雜訊；6.02N + 1.76 是「滿刻度正弦波、只有量化雜訊」時的理想 SNR 上限，訊號沒用滿就達不到。

## 因果鏈
- 動機：要知道一顆 N 位元 ADC 理論上最好能多乾淨。(src: percy-ms-notes)
- 問題：量化誤差在 ±½Q 之間，是實務上一定存在的雜訊。(src: percy-ms-notes)
- 結果：SNR = 6.02 × N + 1.76 是理想最大值，不考慮其它 non-ideal。(src: percy-ms-notes)
- 代價／陷阱：訊號沒滿 code 時，訊號↓、相對雜訊↑、SNR↓。(src: percy-ms-notes)

## 原理
- SNR 有兩種公式：① SNR = 6.02 × N + 1.76　② SNR = P_signal / P_noise (src: percy-ms-notes)
- 量化雜訊 RMS = LSB/√12 (src: percy-ms-notes)
- N↑、Q↓ ⇒ 當然 SNR↑ (src: percy-ms-notes)
- 1 LSB = (Vref − Vgnd)/2^N (src: percy-meeting1)
- 綜述提醒：設計良好的 SAR 應該被雜訊限制，而不是被失真限制。(src: tang-2022-survey)

## 關鍵數字
- 算例條件：10 bits、VDD = 1.2 V；A：Vsig 0~1.2 V；B：Vsig 0.3~0.9 V (src: percy-ms-notes)
- LSB = 1.2/1024 = 1.17 mV；量化雜訊 RMS = LSB/√12 = 0.34 mV (src: percy-ms-notes)
- A：振幅 0.6 V、訊號 RMS 0.424 V；SNR = 0.424 / (0.34×10⁻³) = 1247 = 61.9 dB = 6.02×10 + 1.76 (src: percy-ms-notes)
- B：振幅 0.3 V、訊號 RMS 0.212 V；用 ② SNR = P_signal / P_noise 直接算出 55.9 dB (src: percy-ms-notes)
- B 旁註：61.9 − 6.02 = 6.02×9 + 1.76，訊號少半 (src: percy-ms-notes)
- 驗算 B：0.212 / (0.34×10⁻³) ≈ 624，20·log₁₀(624) ≈ 55.9 dB（計算）
- 0.6 / 1.17m = 512 → 等效 9 bits ADC (src: percy-ms-notes)
- 驗算：用不四捨五入的 0.338 mV，A = 61.97 dB、B = 55.95 dB，和 6.02N + 1.76 的 61.96、55.94 一致（計算）

## 常見誤解 / 衝突
- 6.02N + 1.76 不是「量到的 SNR」，是只有量化雜訊時的上限；實測要看 SNDR。(src: percy-ms-notes, percy-meeting1)
- 擺幅減半 ⇒ SNR 掉 6.02 dB ⇒ 等於少 1 bit：這是「訊號沒滿 code」最直觀的代價。(src: percy-ms-notes)

## 相關
[[adc-dynamic-parameters]] [[noise-and-sizing]] [[sampling-aliasing]]
