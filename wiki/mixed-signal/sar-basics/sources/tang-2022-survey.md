---
node: mixed-signal/sar-basics
title: "Low-Power SAR ADC Design: Overview and Survey of State-of-the-Art Techniques"
id: tang-2022-survey
author: Xiyuan Tang, Jiaxin Liu, Yi Shen, Shaolan Li, Linxiao Shen, Arindam Sanyal, Kareem Ragab, Nan Sun
venue: IEEE TCAS-I, vol. 69, no. 6, pp. 2249–2262, June 2022
doi: 10.1109/TCSI.2022.3166792
type: 綜述論文
url: https://labs.engineering.asu.edu/mixedsignals/wp-content/uploads/sites/58/2023/04/Low-Power_SAR_ADC_Design_Overview_and_Survey_of_State-of-the-Art_Techniques-1.pdf
access: 全文 PDF（作者實驗室網站）
ingested: 2026-11-21
---
## 一句話
2022 年低功耗 SAR 綜述：FoM 趨勢、雜訊、比較器與 DAC 切換的省電技巧、校正。

## 論述

**在解決什麼**：SAR 的能效在 20 年內大幅進步，這篇綜述整理「省下來的能量從哪裡來」，以及下一步往哪走。

**怎麼講**：先定義 Walden FoM，指出最佳 ADC 效率從 2000 年約 3 pJ 進步到 2019 年約 0.4 fJ（約 7,500 倍），其中製程只貢獻約 100 倍，其餘來自架構和電路。接著把功耗拆成 DAC、比較器、邏輯三塊，逐一整理技巧：DAC 用各種切換方式（monotonic、Vcm-based、split-capacitor…），比較器用雙比較器或雜訊分配，邏輯用非同步時序，失配用校正。

**為什麼重要**：它提醒設計良好的 SAR 應該被雜訊限制，而不是被失真限制；也指出熱雜訊不會跟著製程縮小，所以更先進的製程不一定更省電（低中速 SAR 的甜蜜點在 90–55 nm）。

**限制**：數字是彙整別人的論文，例如 monotonic 寫省 63%，和原論文的 81% 對不上，綜述沒說明算法。

**一年後要記得**：核心 SAR 已接近極限，下一步是 noise-shaping、pipelined-SAR 這類混合架構。

## 重點
- Walden FoM = P / (2·BW·2^ENOB)，單位 J/conversion-step
- 最佳效率：2000 年約 3 pJ/conv-step → 2019 年約 0.4 fJ/conv-step，進步 7,500 倍（約每 1.5 年 2 倍）；其中製程約貢獻 100 倍，其餘約 75 倍來自架構與電路創新
- 經典做法是底板取樣；製程縮小後，bootstrapped 頂板取樣變得常見
- kT/C：1 pF、300 K 約 64 µV rms；1 V p-p、10 位元至少要 52 fF；14 位元要大於 13 pF
- 優化良好的設計中，比較器、DAC、SAR 邏輯的功耗差不多
- DAC 切換功率 α·Cdac·Vref²，MSB 電容占大宗
- 切換方式相對傳統做法：monotonic 省 63%（共模單調下降）、Vcm-based 省 75%、split-capacitor 省 37%、bi-directional single-side 省 66%
- 比較器雜訊：低雜訊比較器很耗電；技巧有兩顆比較器、MSB→LSB 雜訊分配、多次平均、統計估計
- 失配：類比自我校正、LMS 數位校正、mismatch error shaping
- 非同步時序：只需要低頻的全域取樣時脈
- 低到中速 SAR 的製程甜蜜點是 90–55 nm
- 結論：核心 SAR 已接近極限，下一步是 noise-shaping、pipelined-SAR 等混合架構

## 可信度
- 高：同儕審查綜述（TCAS-I），涵蓋 2022 年以前的技術；數字是彙整其他論文而來。

## 被哪些概念頁引用
[[cdac-charge-redistribution]] [[comparator]] [[conversion-speed]] [[figures-of-merit]] [[noise-and-sizing]] [[redundancy-and-calibration]] [[sar-adc-overview]] [[sar-vs-pipeline]] [[switching-schemes]]
