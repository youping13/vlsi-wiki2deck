---
node: mixed-signal/sar-basics
id: tang-2022-survey
title: "Low-Power SAR ADC Design: Overview and Survey of State-of-the-Art Techniques"
author: Xiyuan Tang, Jiaxin Liu, Yi Shen, Shaolan Li, Linxiao Shen, Arindam Sanyal, Kareem Ragab, Nan Sun
venue: IEEE TCAS-I, vol. 69, no. 6, pp. 2249–2262, June 2022
doi: 10.1109/TCSI.2022.3166792
type: 綜述論文
url: https://labs.engineering.asu.edu/mixedsignals/wp-content/uploads/sites/58/2023/04/Low-Power_SAR_ADC_Design_Overview_and_Survey_of_State-of-the-Art_Techniques-1.pdf
access: 全文 PDF（作者實驗室網站）
ingested: 2026-11-21
---
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
- 低雜訊比較器中，前置放大器約占比較器功耗的 80%
- 兩顆比較器（只在最後幾位用低雜訊那顆）：9 位元設計約省 55% 比較器功耗
- 雜訊分配：10 位元設計的最後 3 位用低雜訊比較器，省 42% 功耗
- 28 nm 以下的 FinFET 主要提升轉換速度、不提升效率，因為熱雜訊不隨製程縮小
- 客製 MOM 電容單位值可小到 0.5 fF
- 奈瓦級設計中，數位漏電仍約占總功耗 25%
