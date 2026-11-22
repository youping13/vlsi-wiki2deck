---
node: mixed-signal/monotonic
title: 取樣開關：Bootstrapped Switch 與 Cross-coupled 電容
tags: [電路, S/H]
sources: [percy-meeting1, liu-2010-monotonic]
---
## 一句話
讓取樣開關的 Vgs 永遠等於 VDD，導通電阻就不隨訊號變；再用交叉耦合電容抵消關斷時的 Cds 饋通。

## 因果鏈
- 動機：取樣是 ADC 的第一關，開關不線性，後面再準也沒用。(src: percy-meeting1)
- 問題：一般 MOS 開關的 Vgs 會隨訊號變，Ron 跟訊號有關 → 非線性失真。(src: percy-meeting1)
- 解法：bootstrapped switch 讓 Vgs 固定在 VDD → 改善開關線性度。(src: percy-meeting1)
- 為什麼可以：要讓 Vgs 為定值，就在 gate 上接一個電壓源，用充好電的電容實現。(src: percy-meeting1)
- 代價：電容上板電壓是 VDD~2VDD，會造成 M1 漏電、M3 breakdown、M5 耐壓問題，要多加電晶體處理。(src: percy-meeting1)
- 第二個問題：開關 OFF 時寄生 Cds 造成訊號饋通，劣化高頻表現並造成 dynamic offset。(src: percy-meeting1)
- 第二個解法：兩顆交叉耦合 MOM 電容（約 5 fF）注入大小相等、方向相反的電荷 → 中和。(src: percy-meeting1)

## 原理
- 電容靠 gate 那端的電荷無處可去而守恆，Vg 被抬高，所以叫自舉（bootstrapped）。(src: percy-meeting1)
- 導通時 gate = VDD + Vin，source = Vin，Vgs = VDD。(src: percy-meeting1)
- Solution 1：M1、M4 的 gate 也自舉一個 Vin；多一個常開開關 M5a 限制 M5 drain 電壓（最高 VDD − Vth）。(src: percy-meeting1)
- Solution 2：hold 時 M3 gate 要被拉到 VDD 才能斷開 → bootstrap M3 gate / close M3。(src: percy-meeting1)
- 饋通：關斷時正端變成 $V_{ip} + v_i\frac{C_{ds}}{C_s}$，交叉電容補上 $-v_i\frac{C_{ds}}{C_s}$，結果回到 $V_{ip}$。(src: percy-meeting1)

## 關鍵數字
- 取樣電容 Cs = 2.5 pF (src: percy-meeting1)
- 寄生耦合約 5 fF，交叉耦合 MOM 電容也約 5 fF，抵消到 1/2 LSB（2.5 fF）以內 (src: liu-2010-monotonic)

## 常見誤解 / 衝突
- bootstrap 解的是「Ron 隨訊號變」，不是「Ron 太大」；Vgs 固定在 VDD 之後，Ron 是小且固定的常數。(src: liu-2010-monotonic)

## 相關
[[monotonic-sar-case-study]] [[comparator]] [[cdac-charge-redistribution]]
