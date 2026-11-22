# Wiki log（append only）

## 2026-11-21
- 21:30 討論：決定兩層結構（sources/＋concepts/），數字必須標出處、衝突兩個都留（見 docs/discussion.md）
- 21:35 ingest kester-mt021、razavi-2015、saxena-lecture、tang-2022-survey（全文 PDF）、liu-2010-monotonic（摘要）、hu-2024-hybrid（摘要）
- 21:35 建立 11 個 concept 頁
- 21:40 Percy 提供 Liu 2010 全文 → 升級 liu-2010-monotonic；改寫 switching-schemes（補上 1365.3 → 255.5 CVref² 的推導來源）；新增 monotonic-sar-case-study；comparator、sar-adc-overview 補上案例連結
- 21:40 新增衝突：SAR 功耗分配（綜述 vs 成大晶片）
- 21:42 [下游回報] 做證據卡時發現 figures-of-merit 的 ENOB 例子還是舊的 8.48（博士論文頁、可能是第一版原型），改成期刊全文的 9.18。原因：全文升級時只改了 switching-schemes 和 case-study，沒有全文搜尋舊數字
- 22:00 Percy 要求簡報直接放論文原圖：從 Liu 2010 PDF 取出 9 張圖表，放在 assets/figures/，登錄在 wiki/figures.md；Table I 的數字補進來源卡與 switching-schemes（含 0.63 的推論）
- 22:01 新增 docs/loops.md（loop 專用流程圖）；figures 規則寫進 AGENTS.md
- 22:50 Percy 提供兩份自己的文件：Mixed-Signal 手寫筆記（3 頁）、專題 meeting 1 簡報（78 頁）→ ingest 成 percy-ms-notes、percy-meeting1，以筆記為骨架；新增 sampling-aliasing、quantization-noise-snr、adc-dynamic-parameters、adc-static-parameters、bootstrapped-switch；改寫 switching-schemes（ΔQ 能量推導＋因果鏈）、comparator（式 3＋因果鏈）；發現式 (1) 代入算出 1363.3 而不是 1365.3
- 22:55 v3 簡報完成（21 頁，causal/calc 版型）
- 22:59 拆成三份小簡報＋自動產生大目錄（index.html）
- 2026-11-22 22:00 依 Percy 的 VLSI 分類樹重排：wiki/<節點>/、wiki/<節點>/sources/；每篇來源加「## 論述」

- 2026-11-22 22:15 Percy：meeting 1 附錄 A 的各種 ADC 介紹放到 mixed-signal/basic → 補進 percy-meeting1 來源卡，新增 adc-architectures；比較器確定留在 sar-basics
