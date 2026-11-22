# 圖表登錄表（Figure Registry）

> 簡報只能使用這張表登錄過的圖。圖說和出處由 `wiki2deck.py render` 從這張表**自動產生**，AI 不能自己寫出處。
> 圖檔放在 `assets/figures/`。來源論文的版權屬於原出版者；簡報引用時一律標出處。
> 格式：`| id | source | 原圖編號 | 這張圖在說什麼（自己的話） | 原始出處（選填） |`
> `source` 是放進 wiki 的來源 id（簡報那頁必須引用它）；`原始出處` 是圖真正的出處（網站、論文），會一起印在圖說上。

| id | source | label | 說明 | 原始出處 |
| --- | --- | --- | --- | --- |
| liu2010-fig01 | liu-2010-monotonic | Fig. 1 | 傳統 10 位元全差動 SAR ADC：上下兩排二進位電容陣列、比較器、SAR 邏輯 |  |
| liu2010-fig02 | liu-2010-monotonic | Fig. 2 | 提出的架構：bootstrapped 開關在頂板取樣，電容數少一顆 |  |
| liu2010-fig03 | liu-2010-monotonic | Fig. 3 | monotonic 切換的流程圖：比較 → 決定位元 → 高電位那一側往下切 |  |
| liu2010-fig04 | liu-2010-monotonic | Fig. 4 | (a) 傳統切換波形，(b) monotonic 切換波形：共模電壓逐步往地下降 |  |
| liu2010-fig06 | liu-2010-monotonic | Fig. 6 | 四種切換方式的切換能量對輸出碼：proposed 曲線最低 |  |
| liu2010-table1 | liu-2010-monotonic | Table I | 四種切換方式比較：正規化切換功率、開關數、電容數、單位電容數 |  |
| liu2010-fig08 | liu-2010-monotonic | Fig. 8 | 加了電流源的動態比較器，用來壓低共模變動造成的動態 offset |  |
| liu2010-fig13 | liu-2010-monotonic | Fig. 13 | 晶片照片與放大圖：ADC 核心 195 µm × 265 µm，電容陣列占大部分 |  |
| liu2010-fig14 | liu-2010-monotonic | Fig. 14 | 量測 DNL / INL，INL 在中間碼有跳動 |  |
| liu2010-fig05 | liu-2010-monotonic | Fig. 5 | monotonic 切換程序（3-bit）：每一步依比較結果只把一側往下切 |  |
| liu2010-fig15 | liu-2010-monotonic | Fig. 15 | 實測 FFT 頻譜：輸入 10 MHz、取樣 50 MS/s |  |
| m1-flash | percy-meeting1 | meeting 1 p59 | Flash ADC：電阻梯＋2^n−1 個比較器＋thermometer-to-binary | https://www.monolithicpower.com/en/learning/mpscholar/analog-to-digital-converters/detailed-analysis-of-adc-architectures/flash-adcs |
| m1-twostep | percy-meeting1 | meeting 1 p61 | Two-step：Coarse ADC → DAC → 相減 → G → Fine ADC | https://zhuanlan.zhihu.com/p/1975627091732096314 |
| m1-twostep-levels | percy-meeting1 | meeting 1 p61 | 4-bit Flash 對照 2-2 two-step：先 2 個 MSB，再對殘值 2 個 LSB | https://zhuanlan.zhihu.com/p/1975627091732096314 |
| m1-pipeline | percy-meeting1 | meeting 1 p62 | Pipeline：SHA → Stage 1…n，每級 ADC → DAC → 相減得殘值 | https://www.monolithicpower.com/en/learning/mpscholar/analog-to-digital-converters/detailed-analysis-of-adc-architectures/flash-adcs |
| m1-integrating | percy-meeting1 | meeting 1 p63 | Integrating：(a) 電路 (b) 電容先充電到 T1、再放電到 T2 | monolithicpower.com MPScholar ADC 架構系列（meeting 1 p63 上的網址被截斷） |
| m1-ti | percy-meeting1 | meeting 1 p64 | Time-interleaved：4 通道輪流取樣與時序 | https://zhuanlan.zhihu.com/p/1979902233165440803 |
| m1-sar-ti | percy-meeting1 | meeting 1 p65 | SAR + Time-interleaved 方塊圖：多顆 SAR 共用時脈、寫進 RAM | https://zhuanlan.zhihu.com/p/1979902233165440803 |
| m1-fft-params | percy-meeting1 | meeting 1 p45 | 頻譜上的 FS、輸入訊號、最大 spur：SFDR(dBc) vs SFDR(dBFS) | 知乎（圖上浮水印；meeting 1 參考資料 p/575589874） |
| m1-dnl-inl | percy-meeting1 | meeting 1 p78 | (a) DNL：每階寬度和 1 LSB 的差 (b) INL：和理想曲線的偏差 | meeting 1 參考資料：https://blog.csdn.net/qlexcel/article/details/144568435 、https://zhuanlan.zhihu.com/p/575589874 |
| m1-offset-gain | percy-meeting1 | meeting 1 p79 | (a) offset error：整條平移 (b) gain error：斜率不同 | meeting 1 參考資料：https://blog.csdn.net/qlexcel/article/details/144568435 、https://zhuanlan.zhihu.com/p/575589874 |
| m1-conv-annotated | percy-meeting1 | meeting 1 p11 | 傳統切換逐步推導（我的手寫註解） | Percy 手寫註解；底圖 Liu et al., JSSC 2010 |
| m1-power-derivation | percy-meeting1 | meeting 1 p13 | 功耗 = Vref × ΔQ 的手寫推導 | Percy 手寫註解；底圖 Liu et al., JSSC 2010 |
| m1-boot-idea | percy-meeting1 | meeting 1 p68 | Bootstrapped switch idea：OFF 時電容充到 VDD，ON 時接在 gate 與 source 之間 | https://zhuanlan.zhihu.com/p/564837987 |
| m1-boot-fix | percy-meeting1 | meeting 1 p69–75 | (a) Problem 1：上板 VDD~2VDD (b) Solution 1：M5a、M7 (c) Solution 2：bootstrap M3 gate | https://zhuanlan.zhihu.com/p/564837987 |
| m1-crosscouple | percy-meeting1 | meeting 1 p29 | 交叉耦合電容抵消 Cds 饋通 | Liu et al., JSSC 2010（meeting 1 整理） |
