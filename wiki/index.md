# VLSI LLM Wiki — 首頁

> 分類樹定義在 [`../taxonomy.json`](../taxonomy.json)；新增東西前先問 Percy 放哪個節點。規則見 [`../AGENTS.md`](../AGENTS.md)。所有數字都標 `(src: id)`。

- [圖表登錄表](figures.md)：簡報能用的論文原圖（附出處）
- [ingest 紀錄](log.md)

## Basic（`basic`）

VLSI 共通基礎

_待新增_

## Mixed-Signal（`mixed-signal`）

ADC 與混合訊號電路

### Basic（`mixed-signal/basic`）

ADC 共通基礎：取樣與混疊、量化雜訊與 SNR（沒滿 code）、動態參數、INL / DNL、FoM

**來源與論述**

- [Mixed-Signal IC Design 手寫筆記（Sampling / Aliasing / SNR）](mixed-signal/basic/sources/percy-ms-notes.md)

**概念頁**

- [各種 ADC 架構（Flash、Two-step、Pipeline、Integrating、Time-interleaved、SAR）](mixed-signal/basic/adc-architectures.md)
- [ADC 動態參數（SNR、THD、SFDR、SNDR、ENOB、dBc/dBFS、FoM）](mixed-signal/basic/adc-dynamic-parameters.md)
- [ADC 靜態參數（LSB、DNL、INL、Gain/Offset Error）](mixed-signal/basic/adc-static-parameters.md)
- [效能指標（Figures of Merit：ENOB、SNDR、Walden FoM）](mixed-signal/basic/figures-of-merit.md)
- [量化雜訊與 SNR（Quantization Noise, SNR = 6.02N + 1.76）](mixed-signal/basic/quantization-noise-snr.md)
- [取樣與混疊（Sampling, Aliasing）](mixed-signal/basic/sampling-aliasing.md)

### SAR 通論（`mixed-signal/sar-basics`）

SAR 架構本身：二元搜尋、電容 DAC、比較器、速度、冗餘、SAR vs Pipeline；每篇參考資料都有單獨的論述

**來源與論述**

- [A Hybrid Energy-Efficient, Area-Efficient, Low-Complexity Switching Scheme in SAR ADC for Biosensor Applications](mixed-signal/sar-basics/sources/hu-2024-hybrid.md)
- [MT-021 Tutorial — ADC Architectures II: Successive Approximation ADCs](mixed-signal/sar-basics/sources/kester-mt021.md)
- [A Tale of Two ADCs: Pipelined Versus SAR](mixed-signal/sar-basics/sources/razavi-2015.md)
- [Successive Approximation ADCs (lecture slides)](mixed-signal/sar-basics/sources/saxena-lecture.md)
- [Low-Power SAR ADC Design: Overview and Survey of State-of-the-Art Techniques](mixed-signal/sar-basics/sources/tang-2022-survey.md)

**概念頁**

- [二元搜尋演算法（Binary Search）與秤重比喻](mixed-signal/sar-basics/binary-search.md)
- [電容 DAC 與電荷重分配（Capacitive DAC, Charge Redistribution）](mixed-signal/sar-basics/cdac-charge-redistribution.md)
- [比較器（Comparator）](mixed-signal/sar-basics/comparator.md)
- [轉換速度與時序（Conversion Speed, Async SAR）](mixed-signal/sar-basics/conversion-speed.md)
- [SAR ADC 簡史（History）](mixed-signal/sar-basics/history.md)
- [雜訊與電容尺寸（kT/C Noise, Matching）](mixed-signal/sar-basics/noise-and-sizing.md)
- [冗餘與校正（Redundancy, Calibration）](mixed-signal/sar-basics/redundancy-and-calibration.md)
- [SAR ADC 總覽（Successive Approximation Register ADC）](mixed-signal/sar-basics/sar-adc-overview.md)
- [SAR 與 Pipeline ADC 比較（SAR vs. Pipelined）](mixed-signal/sar-basics/sar-vs-pipeline.md)

### Monotonic（Liu 2010）（`mixed-signal/monotonic`）

論文：A 10-bit 50-MS/s SAR ADC With a Monotonic Capacitor Switching Procedure（JSSC 2010），含我的專題 meeting 1 報告

**來源與論述**

- [A 10-bit 50-MS/s SAR ADC With a Monotonic Capacitor Switching Procedure](mixed-signal/monotonic/sources/liu-2010-monotonic.md)
- [專題（一）meeting 1：A 10-bit 50-MS/s SAR ADC With a Monotonic Capacitor Switching Procedure（報告簡報）](mixed-signal/monotonic/sources/percy-meeting1.md)

**概念頁**

- [取樣開關：Bootstrapped Switch 與 Cross-coupled 電容](mixed-signal/monotonic/bootstrapped-switch.md)
- [案例：成大 10 位元 50 MS/s Monotonic SAR ADC（Liu et al., JSSC 2010）](mixed-signal/monotonic/monotonic-sar-case-study.md)
- [電容切換方式與能量推導（conventional vs monotonic …）](mixed-signal/monotonic/switching-schemes.md)

## Bias Circuit（`bias-circuit`）

偏壓電路

_待新增_

## OpAmp（`opamp`）

運算放大器

_待新增_

## LDO（`ldo`）

低壓降線性穩壓器

_待新增_

## 已知衝突（不擇一，兩個都留）

- 式 (1) 代入 n = 10 得 **1363.3**，論文和 meeting 都寫 **1365.3** → [switching-schemes](mixed-signal/monotonic/switching-schemes.md)

- monotonic 省 **81%**（原論文、講義）vs **63%**（綜述）→ [switching-schemes](mixed-signal/monotonic/switching-schemes.md)
- Liu 2010：期刊 0.826 mW / ENOB 9.18 vs 博士論文頁 0.92 mW / ENOB 8.48 → [case study](mixed-signal/monotonic/monotonic-sar-case-study.md)
- SAR 功耗分配：綜述說三者相近 vs 成大晶片數位最大 → [overview](mixed-signal/sar-basics/sar-adc-overview.md)
- DATRAC 年份 1954 vs 1955（來源本身不一致）→ [history](mixed-signal/sar-basics/history.md)
