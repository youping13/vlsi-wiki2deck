---
node: mixed-signal/basic
title: 各種 ADC 架構（Flash、Two-step、Pipeline、Integrating、Time-interleaved、SAR）
tags: [架構, 比較]
sources: [percy-meeting1, razavi-2015, saxena-lecture, kester-mt021]
---
## 一句話
各種 ADC 都在「一次做完（快但貴）」和「分好幾次做（省但慢）」之間取捨：Flash 一次比完，SAR 一次只決定 1 bit，其他架構介於兩者之間，或用多顆並排來換速度。

## 因果鏈
- 動機：Flash 最快、最簡單，把輸入同時和很多個 Vref 比較，直接給出數位輸出。(src: percy-meeting1)
- 問題：Flash 要 2^n − 1 個比較器，耗電，高解析度時很複雜。(src: percy-meeting1)
- 解法 1（分段）：Two-step 先用 Coarse ADC 決定高位元，把殘值放大後再用 Fine ADC 決定低位元。(src: percy-meeting1)
- 解法 2（再多分幾段）：Pipeline 每一級做 ADC → DAC → 相減，把殘值傳給下一級；每級 3 bits，合起來 3n bits。(src: percy-meeting1)
- 代價：pipeline 需要 op-amp 放大殘值，op-amp 的增益和線性度會限制效能。(src: razavi-2015)
- 解法 3（一次 1 bit）：SAR 只用一個比較器重複 N 次，中速時效率好、低功耗。(src: percy-meeting1, razavi-2015)
- 解法 4（用時間換精度）：Integrating 先用輸入對電容充電固定時間 T1，再用參考電壓放電，數放電時間。(src: percy-meeting1)
- 解法 5（並排換速度）：Time-interleaved 讓多個通道輪流取樣，單一通道來不及，就多顆並排錯開時間。(src: percy-meeting1)

## 原理
- Flash：電阻梯分出參考電壓，2^n − 1 個比較器，thermometer code 轉成 n-bit binary 輸出。(src: percy-meeting1)
- Two-step：Coarse ADC 先轉出 D_coarse → DAC 轉回類比 → 和 Vin 相減 → 放大 G → Fine ADC 轉出 D_fine → 兩段合成 D_out。(src: percy-meeting1)
- Pipeline：SHA → Stage 1 … Stage n，每一級都是 ADC → DAC → 相減得到殘值 V_res1 傳給下一級。(src: percy-meeting1)
- Pipeline 多級同時運作；SAR 只用一級，重複 N 個週期。(src: razavi-2015)
- Integrating：控制開關先讓電容用輸入充電一段固定時間 T1，再用參考電壓放電，數位計數器數放電到零花了多久（到 T2）。(src: percy-meeting1)
- Time-interleaved：Ch1~Ch4 四個通道輪流取樣，每個通道 S/H 佔 t_s、轉換佔 3t_s。(src: percy-meeting1)
- SAR + Time-interleaved：多顆 SAR ADC 共用時脈，各自寫進 RAM，再輪流讀出到 OUT。(src: percy-meeting1)

## 關鍵數字
- Flash 比較器數：2^n − 1 (src: percy-meeting1)
- Two-step 例子：4-bit Flash ADC（15 個碼階）對照 ideal 2-step（2-2）ADC：先決定 2 個 MSB，再對殘值決定 2 個 LSB (src: percy-meeting1)
- Pipeline：每級 3 bits，合起來 3n bits (src: percy-meeting1)
- 交錯的極端例子：8 位元 56 GS/s 用了 320 個 175 MS/s 的 SAR 通道 (src: saxena-lecture)
- 以 4 位元為例：Flash 要 2^4 − 1 = 15 個比較器；2-2 two-step 每段只要 2^2 − 1 = 3 個，兩段共 6 個（計算）

## 常見誤解 / 衝突
- 「SAR 的缺點」在 meeting 報告裡只寫「滿多的，但算是 limitation」(src: percy-meeting1)；具體是：一個 bit 一個週期所以速度有限，比較器雜訊直接限制解析度。(src: razavi-2015)
- Two-step 和 pipeline 是同一個想法（粗轉 → 殘值 → 細轉）；差別是 pipeline 分很多級，而且各級同時處理不同的取樣點。(src: percy-meeting1, razavi-2015)

## 相關
[[sar-vs-pipeline]] [[sar-adc-overview]] [[conversion-speed]] [[sampling-aliasing]]
