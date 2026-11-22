---
node: mixed-signal/sar-basics
title: 比較器（Comparator）
tags: [電路]
sources: [razavi-2015, saxena-lecture, tang-2022-survey, liu-2010-monotonic, percy-meeting1]
---
## 一句話
比較器是 SAR 的「裁判」：每個時脈只回答一個問題，輸入比估計值大還是小。

## 因果鏈（monotonic 之後為什麼要改比較器）
- 動機：monotonic 讓 DAC 共模從 Vref/2 一路降到地。(src: percy-meeting1)
- 問題：offset 第二項跟輸入對的有效電壓 (V_GS − V_TH) 有關，而有效電壓會隨輸入共模變 → signal-dependent dynamic offset，第一版原型就被它拉低線性度。(src: liu-2010-monotonic)
- 解法：用 p-type 輸入對（輸入會往地靠），並在輸入對上方串一顆偏壓在飽和區的 MOS 當電流源，讓有效電壓近似固定。(src: liu-2010-monotonic)
- 為什麼不用其他方法：放大比較器會耗電、降低有效電壓會變慢。(src: liu-2010-monotonic)
- 代價：多一顆電流源電晶體；static offset 仍在，但它只平移特性曲線，對 SAR 沒影響。(src: liu-2010-monotonic, razavi-2015)

## 原理
- offset 式 (3)：$V_{os} = \Delta V_{TH1,2} + \frac{(V_{GS}-V_{TH})_{1,2}}{2}\left(\frac{\Delta S_{1,2}}{S_{1,2}} + \frac{\Delta R}{R}\right)$ (src: liu-2010-monotonic)
- 第一項是 static offset，不影響 SAR；第二項是 signal-dependent dynamic offset。(src: liu-2010-monotonic)
- 比較器的 offset 只會讓整條轉換特性平移，不會造成失真，所以 SAR 對 offset 相對寬容。(src: razavi-2015)
- SAR 沒有殘值放大，比較器的雜訊會直接限制解析度，通常在 8 位元以上就會成為問題。(src: razavi-2015)
- 低雜訊比較器的反應時間和功耗可能遠高於一般設計。(src: razavi-2015)
- offset 必須是固定值；有遲滯或會隨時間變化的 offset 會造成錯誤。(src: saxena-lecture)
- 共模電壓會變動的設計（例如 monotonic 切換）要注意訊號相依的動態 offset；成大的做法是在輸入對上方串一顆偏壓 MOS 當電流源。(src: liu-2010-monotonic)
- 動態（再生式）比較器只在比較時耗電，非同步 SAR 也靠它產生「比完了」的訊號。(src: saxena-lecture)

## 關鍵數字
- 低雜訊設計中，前置放大器約占比較器功耗的 80%。(src: tang-2022-survey)
- 兩顆比較器架構（只在最後幾位用低雜訊那顆）：9 位元設計約省 55% 比較器功耗。(src: tang-2022-survey)
- 雜訊從 MSB 到 LSB 遞減分配：10 位元設計的最後 3 位用低雜訊比較器，省 42% 功耗。(src: tang-2022-survey)

## 常見誤解 / 衝突
- 誤解：比較器 offset 一定要很小。對 SAR 來說，offset 只造成平移；真正要顧的是雜訊和 offset 的穩定性。(src: razavi-2015, saxena-lecture)

## 相關
[[sar-adc-overview]] [[noise-and-sizing]] [[conversion-speed]] [[monotonic-sar-case-study]]
