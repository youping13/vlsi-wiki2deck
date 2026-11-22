# 圖表登錄表（Figure Registry）

> 簡報只能使用這張表登錄過的圖。圖說和出處由 `wiki2deck.py render` 從這張表**自動產生**，AI 不能自己寫出處。
> 圖檔放在 `assets/figures/`。來源論文的版權屬於原出版者；簡報引用時一律標出處。
> 格式：`| id | source | 原圖編號 | 這張圖在說什麼（自己的話） |`

| id | source | label | 說明 |
|---|---|---|---|
| liu2010-fig01 | liu-2010-monotonic | Fig. 1 | 傳統 10 位元全差動 SAR ADC：上下兩排二進位電容陣列、比較器、SAR 邏輯 |
| liu2010-fig02 | liu-2010-monotonic | Fig. 2 | 提出的架構：bootstrapped 開關在頂板取樣，電容數少一顆 |
| liu2010-fig03 | liu-2010-monotonic | Fig. 3 | monotonic 切換的流程圖：比較 → 決定位元 → 高電位那一側往下切 |
| liu2010-fig04 | liu-2010-monotonic | Fig. 4 | (a) 傳統切換波形，(b) monotonic 切換波形：共模電壓逐步往地下降 |
| liu2010-fig06 | liu-2010-monotonic | Fig. 6 | 四種切換方式的切換能量對輸出碼：proposed 曲線最低 |
| liu2010-table1 | liu-2010-monotonic | Table I | 四種切換方式比較：正規化切換功率、開關數、電容數、單位電容數 |
| liu2010-fig08 | liu-2010-monotonic | Fig. 8 | 加了電流源的動態比較器，用來壓低共模變動造成的動態 offset |
| liu2010-fig13 | liu-2010-monotonic | Fig. 13 | 晶片照片與放大圖：ADC 核心 195 µm × 265 µm，電容陣列占大部分 |
| liu2010-fig14 | liu-2010-monotonic | Fig. 14 | 量測 DNL / INL，INL 在中間碼有跳動 |
