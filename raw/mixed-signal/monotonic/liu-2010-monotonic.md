---
node: mixed-signal/monotonic
id: liu-2010-monotonic
title: "A 10-bit 50-MS/s SAR ADC With a Monotonic Capacitor Switching Procedure"
author: Chun-Cheng Liu, Soon-Jyh Chang, Guan-Ying Huang, Ying-Zu Lin（成大電機）
venue: IEEE JSSC, vol. 45, no. 4, pp. 731–740, April 2010
doi: 10.1109/JSSC.2010.2042254
type: 期刊論文
url: https://ieeexplore.ieee.org/document/5437496
access: 全文 PDF（Percy 提供，原檔 raw/mixed-signal/monotonic/liu-2010-monotonic.pdf，IEEE 授權，不進 git）
ingested: 2026-11-21（先用摘要 ingest，同日 Percy 提供全文後升級）
file: raw/mixed-signal/monotonic/liu-2010-monotonic.pdf
original_name: "2010JSSC_A_10-bit_50-MS-s_SAR_ADC_with_a_Monotonic_Capacitor_Switching_Procedure.pdf"
---
## 動機
- 中等速度、中等解析度的應用原本多用 pipeline，但 pipeline 需要好幾顆 op-amp，功耗大；先進製程的短通道效應也讓高增益放大器很難做
- SAR 不用前置放大器時沒有靜態功耗，可以做到 rail-to-rail 擺幅
- SAR 的主要功耗來源有三個：數位控制、比較器、電容 DAC。數位功耗會隨製程下降，比較器和電容則受失配與雜訊限制
- 先前的省電切換方式：split capacitor 省 37%、energy-saving 省 56%，但電容和開關變多，邏輯變複雜

## 方法：monotonic 切換
- 全差動架構，用 bootstrapped 開關在頂板取樣，同時把底板重設到 Vref
- 關掉取樣開關後，**不用切換任何電容就能直接做第一次比較**，所以第一次比較前不耗能（傳統做法在第一次比較前就要耗能）
- 依比較結果，只把「電壓較高那一邊」的最大電容切到地，另一邊不動；每個位元只切一顆電容
- 只往下切（downward），因為 nMOS 的導通電阻約只有同尺寸 pMOS 的 1/3，DAC 安定比較快
- 代價：DAC 的共模電壓會從 Vref/2 逐漸降到地
- N 位元只需要 2^(N−1) 顆單位電容，是傳統的一半
- 10 位元平均切換能量：傳統 1365.3 CVref²，monotonic 255.5 CVref²，少 81%
- 式 (1)：E_avg,conv = Σ_{i=1}^{n} 2^{n+1−2i}(2^i − 1) CVref²；式 (2)：E_avg,mono = Σ_{i=1}^{n−1} 2^{n−2−i} CVref²（假設每個輸出碼機率相同）

## Table I（切換方式比較）
- 正規化切換功率：傳統 1、split capacitor 0.63、energy-saving 0.44、proposed 0.19
- 開關數：傳統 4N+10、proposed 4N；電容數：傳統 2N+2、proposed 2N
- 單位電容數：傳統 2^N、proposed 2^(N−1)

## 比較器 offset（式 3）
- Vos = ΔV_TH1,2 + ((V_GS − V_TH)1,2 / 2)·(ΔS1,2/S1,2 + ΔR/R)
- 第一項是 static offset，不影響 SAR；第二項是 signal-dependent dynamic offset：輸入對的有效電壓 (V_GS − V_TH) 會隨輸入共模變
- 改善方法：放大比較器（耗電）、降低有效電壓（變慢）、非二進位搜尋，或在輸入對上方串一顆偏壓在飽和區的 MOS 當電流源，讓有效電壓近似固定

## 電路
- 比較器：動態比較器，用 p-type 輸入對（因為輸入會往地靠）；在頂端串一顆偏壓 MOS 當電流源，讓輸入對的有效電壓在共模變動時維持接近常數，壓低訊號相依的動態 offset（第一版原型就是被它拉低線性度）
- 非同步控制邏輯：由比較器產生 Valid 訊號，不需要高頻時脈；取樣約占整個週期的 20%
- 開關只用反相器當 buffer，不需要傳輸閘
- 電容：多層 sandwich MOM 電容，3.3 µm × 3.3 µm 約 4.8 fF（單層 sandwich 只有 2.4 fF）；每組電容網路總取樣電容 2.5 pF；兩組電容約占整顆 ADC 面積的 72%
- bootstrapped 開關讓取樣電晶體的 gate-source 電壓固定在電源電壓，導通電阻變成小的常數，改善開關線性度
- bootstrapped 開關關掉後會經約 5 fF 寄生耦合，用交叉耦合的 MOM 電容抵消到 1/2 LSB（2.5 fF）以內

## 量測（0.13 µm 1P8M CMOS）
- 1.2 V、50 MS/s：低頻 SNDR 57.0 dB、SFDR 65.9 dB、ENOB 9.18 bits；輸入 50 MHz 時 SNDR 54.4 dB；ERBW > 50 MHz
- 功耗：類比（S/H＋比較器）0.276 mW、數位控制 0.42 mW、參考電壓 0.13 mW（理想值 0.062 mW），總計 0.826 mW
- FoM 29 fJ/conversion-step；0.6 V、10 MS/s 時 FoM 9.6 fJ/conversion-step
- 面積：ADC 核心 195 µm × 265 µm（0.052 mm²）
- DNL 峰值 0.91/−0.63 LSB，INL 1.27/−1.36 LSB；INL 在中間碼有跳動，推測是佈線寄生讓 MSB 電容大了約 1 LSB，效能主要受這個固定的電容失配限制
- 參考電壓功耗：理想值（1 V、50 MS/s、單位電容 4.8 fF）0.062 mW，實測 0.13 mW；原因是 switch buffer 轉態時的動態電流，以及底板與開關 drain 的寄生電容
- 降壓操作：1 V/40 MS/s ENOB 9.15；0.8 V/20 MS/s ENOB 9.19；0.6 V/10 MS/s ENOB 8.91

## 與其他來源的關係
- 成大博士論文頁寫 0.92 mW、ENOB 8.48；期刊版本是 0.826 mW、ENOB 9.18。期刊提到第一版原型 [1] 有動態 offset 問題，論文頁的數字可能是第一版（推論）
