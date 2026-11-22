---
node: mixed-signal/basic
id: percy-ms-notes
title: "Mixed-Signal IC Design 手寫筆記（Sampling / Aliasing / SNR）"
author: Percy
year: 2026
type: 我的筆記（優先：當骨架）
url: raw/mixed-signal/basic/percy-ms-notes.pdf（手寫 PDF，3 頁，本人提供）
access: 全文；Claude 轉錄成 Markdown＋LaTeX，計算已用 Python 驗算
ingested: 2026-11-21
note: 手寫轉錄，下標與正負號請本人核對（見 docs/transcription-check.md）
file: raw/mixed-signal/basic/percy-ms-notes.pdf
original_name: "Mixed-Signal IC Design.pdf"
---
## Sampling
- 理想取樣：x_s(t) 仍是 continuous，只是在其它地方是 0；資訊量沒有改變
- x_s(t) = x(t)·Σ δ(t − nTs) = Σ x(nTs) δ(t − nTs)
- 脈衝串展開成傅立葉級數：Σ δ(t − nTs) = (1/Ts) Σ e^{j2πk fs t}，轉到頻域是 (1/Ts) Σ δ(f − k fs)
- X_s(f) = (1/Ts) Σ_{k=−∞}^{∞} X(f − k fs)
- 取樣：把原頻譜每隔 fs 複製一次

## Aliasing
- 取一個頻率為 m fs + Δf 的 cosine
- x[n] = cos(2π (m fs + Δf)/fs · n) = cos(2π m n ± 2π Δf/fs · n) = cos(2π Δf/fs · n)
- 2π m n 是 2π 的整數倍可以消掉 → 取樣後和頻率 Δf 的訊號分不出來

## SNR
- 兩種公式：① SNR = 6.02 × N + 1.76　② SNR = P_signal / P_noise
- 要先知道量化雜訊（Quantization Noise）：實務上 ADC 一定會有的雜訊，量化誤差在 ±½Q 之間
- ① 就是理想上的最大值（雜訊只考慮量化雜訊，不考慮其它 non-ideal）
- N↑、Q↓ ⇒ 當然 SNR↑

## 論點：沒滿 code，SNR 會掉？
- 假設 10 bits、VDD = 1.2 V；A：Vsig 0~1.2 V，B：Vsig 0.3~0.9 V
- LSB = 1.2/1024 = 1.17 mV；量化雜訊 RMS = LSB/√12 = 0.34 mV
- A：Vp-p 1.2 V、振幅 0.6 V、訊號 RMS 0.424 V（÷√2）、量化雜訊 RMS 0.34 mV
- A：SNR = 0.424 / (0.34×10⁻³) = 1247 = 61.9 dB = 6.02×10 + 1.76
- B：Vp-p 0.6 V、振幅 0.3 V、訊號 RMS 0.212 V、量化雜訊 RMS 0.34 mV
- B：SNR = 55.9 dB，是用 ② SNR = P_signal / P_noise 直接算出來的（不是套 6.02N + 1.76）
- B 旁註：61.9 − 6.02 = 6.02×9 + 1.76，訊號少半（對照用：振幅減半，SNR 少 6.02 dB，等於少 1 bit）
- 0.6 / 1.17m = 512 → 等效 9 bits ADC
- ⇒ 訊號↓，相對雜訊↑，SNR↓
