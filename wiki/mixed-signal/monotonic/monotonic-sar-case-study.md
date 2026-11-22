---
node: mixed-signal/monotonic
title: 案例：成大 10 位元 50 MS/s Monotonic SAR ADC（Liu et al., JSSC 2010）
tags: [案例, 論文]
sources: [liu-2010-monotonic, percy-meeting1]
---
## 一句話
這是一顆把「省電切換」、「改良比較器」和「非同步邏輯」放在一起，用 0.13 µm 製程做到 29 fJ/conversion-step 的 SAR ADC。

## 原理
- 動機：pipeline ADC 需要多顆 op-amp，功耗大，在先進製程又難做；SAR 不用前置放大器時沒有靜態功耗。(src: liu-2010-monotonic)
- 架構：全差動、bootstrapped 開關頂板取樣，電容網路同時當 S/H 和參考 DAC。(src: liu-2010-monotonic)
- 切換：monotonic，每個位元只切一顆電容，只往下切。(src: liu-2010-monotonic)
- 比較器：輸入會往地靠，所以用 p-type 輸入對；再串一顆偏壓 MOS 當電流源，讓共模變動時有效電壓幾乎不變，壓低動態 offset。(src: liu-2010-monotonic)
- 邏輯：非同步控制，由比較器的 Valid 訊號觸發下一步，不需要高頻時脈。(src: liu-2010-monotonic)
- 電容：多層 sandwich MOM 電容，同樣面積的電容值是單層的兩倍。(src: liu-2010-monotonic)
- 限制：INL 在中間碼有跳動，推測是佈線寄生讓 MSB 電容大了約 1 LSB。(src: liu-2010-monotonic)

## 關鍵數字
- 0.13 µm 1P8M CMOS、1.2 V、50 MS/s。(src: liu-2010-monotonic)
- 低頻 SNDR 57.0 dB、SFDR 65.9 dB、ENOB 9.18 bits。(src: liu-2010-monotonic)
- 總功耗 0.826 mW：類比 0.276 mW、數位 0.42 mW、參考電壓 0.13 mW。(src: liu-2010-monotonic)
- FoM 29 fJ/conversion-step；降到 0.6 V、10 MS/s 時是 9.6 fJ/conversion-step。(src: liu-2010-monotonic)
- 單位電容約 4.8 fF（3.3 µm × 3.3 µm），每組電容網路取樣電容 2.5 pF，電容約占 ADC 面積的 72%。(src: liu-2010-monotonic)
- 核心面積 195 µm × 265 µm，也就是 0.052 mm²。(src: liu-2010-monotonic)
- 峰值 DNL 0.91/−0.63 LSB，INL 1.27/−1.36 LSB。(src: liu-2010-monotonic)

- 參考電壓功耗：理想值 0.062 mW，實測 0.13 mW。(src: liu-2010-monotonic)

## 常見誤解 / 衝突
- 實測功耗比預期高：switch buffer 在轉態時消耗動態電流；底板與開關 drain 的寄生電容也增加功耗。(src: percy-meeting1)
- 「SAR 的功耗主要在 DAC」在這顆晶片並不成立：數位邏輯 0.42 mW 是最大宗。(src: liu-2010-monotonic)
- 成大博士論文頁的 0.92 mW、ENOB 8.48 可能是第一版原型的數字（推論）。(src: liu-2010-monotonic)

## 相關
[[switching-schemes]] [[comparator]] [[conversion-speed]] [[figures-of-merit]]
