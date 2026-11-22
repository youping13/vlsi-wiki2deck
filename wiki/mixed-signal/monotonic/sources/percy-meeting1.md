---
node: mixed-signal/monotonic
title: "專題（一）meeting 1：A 10-bit 50-MS/s SAR ADC With a Monotonic Capacitor Switching Procedure（報告簡報）"
id: percy-meeting1
author: Percy，指導教授 張順志
year: 2026（報告日 2026/03/27）
type: 我的報告簡報（優先：當骨架）
url: raw/mixed-signal/monotonic/percy-meeting1.pdf（PowerPoint 匯出，78 頁，本人提供）
access: 全文；文字萃取＋逐頁看圖
ingested: 2026-11-21
---
## 一句話
我在專題（一）meeting 1 報告 Liu 2010 的 78 頁簡報：monotonic 的 ΔQ 能量推導、bootstrap、cross-coupled 電容、比較器、動態/靜態參數。

## 論述

**這份報告在講什麼**：我在專題（一）meeting 1 報告 Liu 2010 這篇 monotonic SAR ADC。順序是：為什麼選 SAR → 傳統切換的瓶頸 → monotonic 怎麼切（3-bit 一步一步用 ΔQ 算能量）→ 代價和電路對策（bootstrap、cross-coupled 電容、改良比較器、非同步邏輯）→ 量測與參數定義。附錄 A 整理了各種 ADC 架構（放在 mixed-signal/basic 的 [[adc-architectures]]）。

**我的理解重點**：能量 = Vref × ΔQ，只算從 Vref 抽出的電荷。monotonic 第一步 0、第二步 CVref²、第三步 ¾CVref²，每一步只有一側抽電荷。代價是 Vcm 往地降，造成 signal-dependent offset。

**一年後要記得**：這份是 monotonic 節點的骨架，wiki 和簡報的因果順序照它走。

## 重點
## 為什麼選 SAR、傳統 SAR 的瓶頸（p4–5）
- Why SAR：架構簡單、沒有靜態功耗
- 傳統 SAR 的瓶頸：速度有限、trial-and-error 很沒效率、第一步就消耗大量能量、settling 慢、面積沒效率
- 提出的創新：第一步零切換、只往下（monotonic）切；改良比較器避免線性度劣化
- 成果：高功率效率、面積好、settling 變快

## 傳統 SAR（p7–10）
- 傳統陣列：512C … 8C、4C、2C、C、C（含 dummy 電容），底板取樣
- 傳統：Vcm 保持不變，但功耗較高
- 功耗推導：Power consumption = Vref × ΔQ（ΔQ 是接在 Vref 上的電容充多少電）

## Proposed（p11–17）
- 第一次比較不用切任何電容 → 不需要 512C
- 每個 bit cycle 只切一顆電容 → 功耗較小
- 3-bit 例子：a、b：V+ = Vip，V− = Vin，比 Vip > Vin
- c：V+ = Vip，V− = Vin − Vref/2 → 比 Vip − Vin > −Vref/2
- d：V+ = Vip − Vref/4，V− = Vin − Vref/2 → 比 Vip − Vin > −Vref/4
- 能量：Power consumption = Vref·ΔQ，ΔQ = Ci·[(Vref − Vtop,final) − (Vbottom,initial − Vtop,initial)]
- 步驟 1：ΔV = 0，ΔQ+ = ΔQ− = 0，E = 0
- 步驟 2：ΔV = Vref/2，ΔQ+ = 0，ΔQ− = (C + C)(Vref/2)，E = CVref²
- 步驟 3：ΔV = Vref/4，ΔQ+ = (2C + C)(Vref/4)，ΔQ− = 0，E = ¾CVref²
- 波形：Vcm 從 Vref/2 → ground ⇒ signal-dependent offset；只往下切 ⇒ DAC 變快；第一次比較不用切電容
- 比較：E_avg,conv = 1365.3 CVref²，E_avg,mono = 255.5 CVref²；最低切換功耗，開關和單位電容最少

## S/H：Bootstrapped switch（p20–24、附錄 C p64–72）
- 問題：一般 MOS 開關的 Vgs 會隨訊號變，Ron 跟訊號有關 → 非線性失真
- 解法：bootstrapped switch 讓 Vgs 固定在 VDD → 改善開關線性度；取樣電容 Cs = 2.5 pF
- IDEA：要讓 Vgs 為定值 ⇒ 在 gate 上接一個電壓源 ⇒ 用充好電的電容實現；電容靠 gate 那端的電荷無處可去而守恆，Vg 被抬高，所以叫自舉（bootstrapped）
- 導通時 gate = VDD + Vin，source = Vin，Vgs = VDD
- Problem 1：Vin 在 0~VDD 時，Cb 上板電壓是 VDD~2VDD，M1 控制訊號最大只有 VDD → M1 會導通，Drain/Source 反過來，電荷從 M1 流走，Vgs 不再固定；M4 的導通電阻也跟 Vin 有關；M3 導通時 Vgs 到 2VDD 會 breakdown；M5 的 Vgd、Vds 太大，通常不要大於 VDD
- Solution 1：M1、M4 的 gate 也自舉一個 Vin（接到 M6 gate）；多一個常開開關 M5a 限制 M5 drain 電壓（最高 VDD − Vth）；M3 的 Vsg 變成 VDD 定值 → 導通電阻與電壓過大的問題解決
- Problem 2：M3 怎麼斷開？hold 時 M3 gate 要被拉到 VDD，但現在被拉到地 → Solution 2：bootstrap M3 gate / close M3

## Cross-coupled capacitors（p25–26）
- 問題：寄生 Cds 在開關 OFF（比較期間）時造成訊號饋通，劣化高頻表現並造成 dynamic offset：Vip + vi·Cds/Cs
- 解法：兩顆交叉耦合 MOM 電容（約 5 fF）從差動另一路注入大小相等、方向相反的電荷 → 中和：Vip + vi·Cds/Cs − vi·Cds/Cs = Vip

## Dynamic comparator with a current source（p27–30）
- Clkc = 1：reset；Clkc = 0 且 V+ > V− ⇒ IM1 < IM2 ⇒ VY = 1、VX = 0 ⇒ Outp = 1
- offset 來源：threshold voltage offset、physical dimension mismatch、parasitic capacitance mismatch
- static offset 不影響 SAR；signal-dependent dynamic offset 才是問題 → 用 PMOS 輸入對＋電流源改善

## 控制邏輯、電容陣列（p31–36）
- 非同步控制邏輯：sampling / holding 由比較器結果推進
- DAC control：Clki 上升緣且 Outp/Outn = 1 → 對應電容從 Vref 切到地；= 0 → 保持接 Vref；Clki 下降緣 → 所有電容接回 Vref；delay buffer 保證 Clki 在 flip-flop 輸出之後才觸發 AND gate
- 電容：MIM → MOM；只用三層金屬、單位面積電容小；多層 sandwich 讓有效電容面積加倍；佈線寄生對電容比例影響很大

## 量測與參數（p38–50、附錄 D p73–78）
- 1 LSB = (Vref − Vgnd)/2^N；例：5 V、10 bits → 5/1024 = 4.88 mV
- 靜態誤差：DNL、INL、gain error、offset error
- INL 在 0111111111 → 1000000000 跳動：佈線造成的寄生電容
- SNR(dB) = 10·log10(P_signal/P_noise)
- THD(dB) = 10·log10(P_harmonics/P_signal)
- SFDR(dBc) = 10·log10(P_signal/P_max_spur)
- SNDR(dB) = 10·log10(P_signal/(P_noise + P_harmonics))
- ENOB(bits) = (SNDR − 1.76)/6.02
- dBc（相對載波／輸入訊號）vs dBFS（相對滿刻度）
- FFT 頻譜：輸入 10 MHz、1.2 V、50 MS/s，Nyquist limit = 50M/2；問題：DC component？second harmonic 20M？
- 高頻劣化原因：clock jitter、dynamic non-linearity（寄生電容）、settling time failure
- 取樣頻率太高劣化：settling time failure、digital logic timing（delay buffer）、comparator timing；50 MHz 以下表現良好
- 實測功耗和預期不同：switch buffer 在轉態時消耗動態電流；底板與開關 drain 的寄生電容也增加功耗
- FOM = Power / (2^ENOB × min{2×ERBW, fs})

## 附錄 A：各種 ADC 介紹（p59–65）
- Flash：優點是快、簡單；缺點是耗電、高解析度時很複雜。基本概念：把輸入同時和很多個 Vref 比較，直接給出數位輸出
- Flash 的圖：電阻梯分出參考電壓，2^n − 1 個比較器，thermometer code 轉成 n-bit binary 輸出
- SAR：優點是中速時效率好、低功耗；缺點滿多的，但算是 limitation
- Two-step：Coarse ADC 先轉出 D_coarse → DAC 轉回類比 → 和 Vin 相減 → 放大 G → Fine ADC 轉出 D_fine → 兩段合成 D_out
- Two-step 的圖：4-bit Flash ADC（0000~1111，15 個碼階）對照 ideal 2-step（2-2）ADC：先決定 2 個 MSB，再對殘值決定 2 個 LSB
- Pipeline：SHA → Stage 1 … Stage n，每一級都是 ADC → DAC → 相減得到殘值 V_res1 傳給下一級；每級 3 bits，合起來 3n bits（Combine Bits）
- Integrating：控制開關先讓電容用輸入充電一段固定時間 T1，再用參考電壓放電，數位計數器數放電到零花了多久（到 T2）
- Time-interleaved：Ch1~Ch4 四個通道輪流取樣，每個通道 S/H 佔 t_s、轉換佔 3t_s；單一通道來不及，就多顆並排錯開時間
- SAR + Time-interleaved：多顆 SAR ADC 共用時脈，各自寫進 RAM，再輪流讀出到 OUT
- 附錄 B：C-2C 電容陣列（只有標題頁）

## 可信度
- 最高（我的報告，當骨架）：內容是我對論文的理解；數字和論文衝突時，以論文為準，並記在衝突段落。

## 被哪些概念頁引用
[[adc-dynamic-parameters]] [[adc-static-parameters]] [[bootstrapped-switch]] [[comparator]] [[monotonic-sar-case-study]] [[quantization-noise-snr]] [[switching-schemes]]
