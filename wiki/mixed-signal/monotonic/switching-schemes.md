---
node: mixed-signal/monotonic
title: 電容切換方式與能量推導（conventional vs monotonic …）
tags: [低功耗, DAC, 計算]
sources: [liu-2010-monotonic, percy-meeting1, tang-2022-survey, saxena-lecture, hu-2024-hybrid]
---
## 一句話
DAC 的能量 = Vref × 從 Vref 抽出的電荷；monotonic 靠「先比再切、每位元只往下切一顆」把抽電荷的次數和量都壓到最低。

## 因果鏈
- 動機：SAR 沒有靜態功耗，剩下的功耗大頭之一是電容 DAC 的切換。(src: percy-meeting1, tang-2022-survey)
- 問題 1：傳統是 trial-and-error，猜錯就要切回來，浪費能量。(src: percy-meeting1)
- 問題 2：傳統在第一步就消耗大量能量，因為第一次比較前就要把 MSB 電容切到 Vref。(src: percy-meeting1, liu-2010-monotonic)
- 解法：第一步零切換、只往下（monotonic）切。(src: percy-meeting1)
- 為什麼省：第一次比較不用切任何電容 → 不需要 512C；每個 bit cycle 只切一顆電容 → 功耗較小。(src: percy-meeting1)
- 附帶好處：只往下切 ⇒ DAC 變快，因為 nMOS 的導通電阻約只有同尺寸 pMOS 的 1/3。(src: percy-meeting1, liu-2010-monotonic)
- 代價：Vcm 從 Vref/2 → ground ⇒ signal-dependent offset，要改比較器。(src: percy-meeting1)

## 原理
- 能量：Power consumption = Vref·ΔQ，ΔQ = Ci·[(Vref − Vtop,final) − (Vbottom,initial − Vtop,initial)] (src: percy-meeting1)
- 3-bit 走一遍（monotonic）：(src: percy-meeting1)
  - 步驟 1：ΔV = 0，ΔQ+ = ΔQ− = 0，E = 0
  - 步驟 2：ΔV = Vref/2，ΔQ+ = 0，ΔQ− = (C + C)(Vref/2)，E = CVref²
  - 步驟 3：ΔV = Vref/4，ΔQ+ = (2C + C)(Vref/4)，ΔQ− = 0，E = ¾CVref²
- 比較器看到的：c：V+ = Vip，V− = Vin − Vref/2 → 比 Vip − Vin > −Vref/2；d：V+ = Vip − Vref/4，V− = Vin − Vref/2 → 比 Vip − Vin > −Vref/4 (src: percy-meeting1)
- 平均能量公式（每個輸出碼機率相同）：$E_{avg,conv} = \sum_{i=1}^{n} 2^{n+1-2i}(2^i-1)\,CV_{ref}^2$，$E_{avg,mono} = \sum_{i=1}^{n-1} 2^{n-2-i}\,CV_{ref}^2$ (src: liu-2010-monotonic)
- Vcm-based 需要額外 Vcm 參考與驅動功率；split-capacitor 不需 Vcm 也能維持共模固定。(src: tang-2022-survey)
- 混合式（monotonic＋MSB 電容分割）：大多數步驟單邊切換，驅動電路比較簡單。(src: hu-2024-hybrid)

## 關鍵數字
- 10 位元平均切換能量：傳統 1365.3 CVref²，monotonic 255.5 CVref²，少 81%。(src: liu-2010-monotonic)
- Monotonic 的 N 位元陣列只要 2^(N−1) 顆單位電容，總電容少 50%。(src: liu-2010-monotonic)
- 原論文 Table I 的正規化切換功率：傳統 1、split capacitor 0.63、energy-saving 0.44、proposed 0.19。(src: liu-2010-monotonic)
- 開關數從傳統的 4N+10 降到 4N。(src: liu-2010-monotonic)
- 同一篇論文比較：split capacitor 省 37%，energy-saving 省 56%。(src: liu-2010-monotonic)
- 綜述整理（相對傳統）：monotonic 省 63%、bi-directional single-side 省 66%、Vcm-based 省 75%、split-capacitor 省 37%。(src: tang-2022-survey)
- 混合式（Hu 2024）：切換能量少 98.4%，單位電容少 87.5%。(src: hu-2024-hybrid)

## 常見誤解 / 衝突
- **1365.3 還是 1363.3？** 把式 (1) 代入 n = 10 算出 1363.3 CVref²，論文內文和 meeting 簡報都寫 1365.3；式 (2) 代入算出 255.5，跟論文一致。省電比例 1 − 255.5/1363.3 = 81.3%，結論不變（計算）
- **monotonic 到底省 81% 還是 63%？** 原論文和講義寫 81% (src: liu-2010-monotonic, saxena-lecture)，綜述寫 63% (src: tang-2022-survey)。綜述沒寫算法，兩個都保留；原論文 Table I 中 split capacitor 的正規化功率剛好是 0.63，也可能是彙整時抄錯欄（推論，未證實）。
- 切換能量省 98.4% (src: hu-2024-hybrid) 不代表整顆 ADC 也省這麼多：在成大的晶片裡，參考電壓只占 0.13 mW，數位邏輯就占了 0.42 mW。(src: liu-2010-monotonic)

## 相關
[[cdac-charge-redistribution]] [[monotonic-sar-case-study]] [[comparator]] [[figures-of-merit]]
