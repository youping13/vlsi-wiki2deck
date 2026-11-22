### [2026-11-21 21:41:17] retrieve — PASS
- g1 說得出 SAR ADC 由哪些方塊組成、為什麼叫 SAR → concepts/comparator(14), concepts/sar-adc-overview(8), sources/tang-2022-survey(6), sources/liu-2010-monotonic(6), sources/kester-mt021(4)
- g2 能用秤重比喻走一遍二元搜尋 → concepts/binary-search(18), sources/kester-mt021(5), sources/saxena-lecture(3), concepts/switching-schemes(3), sources/tang-2022-survey(2)
- g3 知道電容陣列怎麼同時取樣又當 DAC → concepts/cdac-charge-redistribution(11), sources/saxena-lecture(5), sources/razavi-2015(4), sources/hu-2024-hybrid(2), concepts/switching-schemes(2)
- g4 知道 SAR 的速度從哪裡來、被什麼限制 → concepts/conversion-speed(13), sources/saxena-lecture(4), sources/razavi-2015(3), sources/liu-2010-monotonic(3), concepts/monotonic-sar-case-study(3)
- g5 理解為什麼 SAR 省電、monotonic 切換省在哪 → concepts/switching-schemes(25), concepts/monotonic-sar-case-study(20), sources/liu-2010-monotonic(9), concepts/sar-vs-pipeline(6), concepts/figures-of-merit(4)
- g6 會看一顆真實晶片的規格與 FoM → concepts/figures-of-merit(22), sources/liu-2010-monotonic(13), concepts/monotonic-sar-case-study(7), sources/tang-2022-survey(3), sources/hu-2024-hybrid(1)

### [2026-11-21 21:41:17] coverage gate — PASS
- g1 OK：5 頁、5 個來源
- g2 OK：5 頁、6 個來源
- g3 OK：5 頁、6 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、5 個來源
- g6 OK：5 頁、3 個來源

### [2026-11-21 21:41:46] evidence gate — FAIL
- ❌ c35: wiki_text 不是 concepts/figures-of-merit 的原文子字串 → 回 evidence 重做這張卡
- ❌ c38: wiki_text 不是 concepts/cdac-charge-redistribution 的原文子字串 → 回 evidence 重做這張卡
- 38 張卡

### [2026-11-21 21:41:51] evidence gate — PASS
- 38 張卡

### [2026-11-21 21:41:59] evidence gate — PASS
- 38 張卡

### [2026-11-21 21:42:49] human approve gate — FAIL
- ❌ outline.md status = draft，需要人工改成 approved 才能往下

### [2026-11-21 21:42:53] human approve gate — PASS

### [2026-11-21 21:43:48] faithfulness gate — FAIL
- ❌ s3「答案：試 6 次，得到 101101」：bullets[0] 的數字 0 不在引用卡片 ['c5'] 中
- ❌ s3「答案：試 6 次，得到 101101」：svg 文字「X ≥ 48 ?」的數字 48 不在本頁卡片中
- ❌ s3「答案：試 6 次，得到 101101」：svg 文字「X ≥ 40 ?」的數字 40 不在本頁卡片中
- ❌ s3「答案：試 6 次，得到 101101」：svg 文字「X ≥ 44 ?」的數字 44 不在本頁卡片中
- ❌ s3「答案：試 6 次，得到 101101」：svg 文字「X ≥ 46 ?」的數字 46 不在本頁卡片中
- ❌ s6「電容陣列：同時取樣、又當 DAC」：svg 文字「8C」的數字 8 不在本頁卡片中
- ❌ s6「電容陣列：同時取樣、又當 DAC」：svg 文字「4C」的數字 4 不在本頁卡片中
- 16 頁；需要重寫：s3, s6

### [2026-11-21 21:44:08] evidence gate — PASS
- 39 張卡

### [2026-11-21 21:44:08] faithfulness gate — PASS
- 16 頁；需要重寫：無

### [2026-11-21 21:44:11] render + render gate — PASS
- 輸出 /mnt/attach/outputs/wiki2deck/decks/sar-adc/index.html（16 頁，38 張卡片被引用，33 KB）

### [2026-11-21 21:44:22] render + render gate — PASS
- 輸出 /mnt/attach/outputs/wiki2deck/decks/sar-adc/index.html（16 頁，38 張卡片被引用，33 KB）

### [2026-11-21 21:44:48] faithfulness gate — PASS
- 16 頁；需要重寫：無

### [2026-11-21 21:44:48] render + render gate — PASS
- 輸出 /mnt/attach/outputs/wiki2deck/decks/sar-adc/index.html（16 頁，38 張卡片被引用，31 KB）

### [2026-11-21 21:45:13] render + render gate — PASS
- 輸出 /mnt/attach/outputs/wiki2deck/decks/sar-adc/index.html（16 頁，38 張卡片被引用，32 KB）

### [2026-11-21 21:45:28] render + render gate — PASS
- 輸出 /mnt/attach/outputs/wiki2deck/decks/sar-adc/index.html（16 頁，38 張卡片被引用，32 KB）

### [2026-11-21 21:46:17] retrieve — PASS
- g1 說得出 SAR ADC 由哪些方塊組成、為什麼叫 SAR → concepts/comparator(14), concepts/sar-adc-overview(8), sources/tang-2022-survey(6), sources/liu-2010-monotonic(6), sources/kester-mt021(4)
- g2 能用秤重比喻走一遍二元搜尋 → concepts/binary-search(18), sources/kester-mt021(5), sources/saxena-lecture(3), concepts/switching-schemes(3), sources/tang-2022-survey(2)
- g3 知道電容陣列怎麼同時取樣又當 DAC → concepts/cdac-charge-redistribution(11), sources/saxena-lecture(5), sources/razavi-2015(4), sources/hu-2024-hybrid(2), concepts/switching-schemes(2)
- g4 知道 SAR 的速度從哪裡來、被什麼限制 → concepts/conversion-speed(13), sources/saxena-lecture(4), sources/razavi-2015(3), sources/liu-2010-monotonic(3), concepts/monotonic-sar-case-study(3)
- g5 理解為什麼 SAR 省電、monotonic 切換省在哪 → concepts/switching-schemes(25), concepts/monotonic-sar-case-study(20), sources/liu-2010-monotonic(9), concepts/sar-vs-pipeline(6), concepts/figures-of-merit(4)
- g6 會看一顆真實晶片的規格與 FoM → concepts/figures-of-merit(22), sources/liu-2010-monotonic(13), concepts/monotonic-sar-case-study(7), sources/tang-2022-survey(3), sources/hu-2024-hybrid(1)

### [2026-11-21 21:46:17] coverage gate — PASS
- g1 OK：5 頁、5 個來源
- g2 OK：5 頁、6 個來源
- g3 OK：5 頁、6 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、5 個來源
- g6 OK：5 頁、3 個來源

### [2026-11-21 21:46:17] evidence gate — PASS
- 39 張卡

### [2026-11-21 21:46:17] human approve gate — PASS

### [2026-11-21 21:46:17] faithfulness gate — PASS
- 16 頁；需要重寫：無

### [2026-11-21 21:46:17] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（16 頁，38 張卡片被引用，32 KB）

### [2026-11-21 21:47:03] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（16 頁，38 張卡片被引用，32 KB）

### [2026-11-21 13:47:43 +0000] retrieve — PASS
- g1 說得出 SAR ADC 由哪些方塊組成、為什麼叫 SAR → concepts/comparator(14), concepts/sar-adc-overview(8), sources/tang-2022-survey(6), sources/liu-2010-monotonic(6), sources/kester-mt021(4)
- g2 能用秤重比喻走一遍二元搜尋 → concepts/binary-search(18), sources/kester-mt021(5), sources/saxena-lecture(3), concepts/switching-schemes(3), sources/tang-2022-survey(2)
- g3 知道電容陣列怎麼同時取樣又當 DAC → concepts/cdac-charge-redistribution(11), sources/saxena-lecture(5), sources/razavi-2015(4), sources/hu-2024-hybrid(2), concepts/switching-schemes(2)
- g4 知道 SAR 的速度從哪裡來、被什麼限制 → concepts/conversion-speed(13), sources/saxena-lecture(4), sources/razavi-2015(3), sources/liu-2010-monotonic(3), concepts/monotonic-sar-case-study(3)
- g5 理解為什麼 SAR 省電、monotonic 切換省在哪 → concepts/switching-schemes(25), concepts/monotonic-sar-case-study(20), sources/liu-2010-monotonic(9), concepts/sar-vs-pipeline(6), concepts/figures-of-merit(4)
- g6 會看一顆真實晶片的規格與 FoM → concepts/figures-of-merit(22), sources/liu-2010-monotonic(13), concepts/monotonic-sar-case-study(7), sources/tang-2022-survey(3), sources/hu-2024-hybrid(1)

### [2026-11-21 13:47:43 +0000] coverage gate — PASS
- g1 OK：5 頁、5 個來源
- g2 OK：5 頁、6 個來源
- g3 OK：5 頁、6 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、5 個來源
- g6 OK：5 頁、3 個來源

### [2026-11-21 13:47:43 +0000] evidence gate — PASS
- 39 張卡

### [2026-11-21 13:47:43 +0000] human approve gate — PASS

### [2026-11-21 13:47:43 +0000] faithfulness gate — PASS
- 16 頁；需要重寫：無

### [2026-11-21 13:47:43 +0000] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（16 頁，38 張卡片被引用，32 KB）

### [2026-11-21 21:59:02 +0800] human approve gate — FAIL
- ❌ outline.md status = draft，需要人工改成 approved 才能往下

### [2026-11-21 21:59:05 +0800] human approve gate — PASS

### [2026-11-21 21:59:05 +0800] faithfulness gate — FAIL
- ❌ s7「一步一步算 $V_X$」：圖 liu2010-fig01 來自 liu-2010-monotonic，但本頁沒有引用該來源的卡片
- 17 頁；需要重寫：s7

### [2026-11-21 21:59:19 +0800] retrieve — PASS
- g1 說得出 SAR ADC 由哪些方塊組成、為什麼叫 SAR → concepts/comparator(14), concepts/sar-adc-overview(8), sources/tang-2022-survey(6), sources/liu-2010-monotonic(6), sources/kester-mt021(4)
- g2 能用秤重比喻走一遍二元搜尋 → concepts/binary-search(18), sources/kester-mt021(5), sources/saxena-lecture(3), concepts/switching-schemes(3), sources/tang-2022-survey(2)
- g3 知道電容陣列怎麼同時取樣又當 DAC → concepts/cdac-charge-redistribution(11), sources/saxena-lecture(5), sources/razavi-2015(4), sources/hu-2024-hybrid(2), concepts/switching-schemes(2)
- g4 知道 SAR 的速度從哪裡來、被什麼限制 → concepts/conversion-speed(13), sources/saxena-lecture(4), sources/razavi-2015(3), sources/liu-2010-monotonic(3), concepts/monotonic-sar-case-study(3)
- g5 理解為什麼 SAR 省電、monotonic 切換省在哪 → concepts/switching-schemes(27), concepts/monotonic-sar-case-study(20), sources/liu-2010-monotonic(9), concepts/sar-vs-pipeline(6), concepts/figures-of-merit(4)
- g6 會看一顆真實晶片的規格與 FoM → concepts/figures-of-merit(22), sources/liu-2010-monotonic(13), concepts/monotonic-sar-case-study(7), sources/tang-2022-survey(3), sources/hu-2024-hybrid(1)

### [2026-11-21 21:59:19 +0800] coverage gate — PASS
- g1 OK：5 頁、5 個來源
- g2 OK：5 頁、6 個來源
- g3 OK：5 頁、6 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、5 個來源
- g6 OK：5 頁、3 個來源

### [2026-11-21 21:59:19 +0800] evidence gate — PASS
- 40 張卡

### [2026-11-21 21:59:19 +0800] human approve gate — PASS

### [2026-11-21 21:59:19 +0800] faithfulness gate — PASS
- 17 頁；需要重寫：無

### [2026-11-21 21:59:19 +0800] render + render gate — FAIL
- ❌ 內容殘留 TODO / {{ }} / lorem
- 輸出 decks/sar-adc/index.html（17 頁，39 張卡片被引用，34 KB）

### [2026-11-21 21:59:24 +0800] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（17 頁，39 張卡片被引用，34 KB）

### [2026-11-21 22:02:03 +0800] retrieve — PASS
- g1 說得出 SAR ADC 由哪些方塊組成、為什麼叫 SAR → concepts/comparator(14), concepts/sar-adc-overview(8), sources/tang-2022-survey(6), sources/liu-2010-monotonic(6), sources/kester-mt021(4)
- g2 能用秤重比喻走一遍二元搜尋 → concepts/binary-search(18), sources/kester-mt021(5), sources/saxena-lecture(3), concepts/switching-schemes(3), sources/tang-2022-survey(2)
- g3 知道電容陣列怎麼同時取樣又當 DAC → concepts/cdac-charge-redistribution(11), sources/saxena-lecture(5), sources/razavi-2015(4), sources/hu-2024-hybrid(2), concepts/switching-schemes(2)
- g4 知道 SAR 的速度從哪裡來、被什麼限制 → concepts/conversion-speed(13), sources/saxena-lecture(4), sources/razavi-2015(3), sources/liu-2010-monotonic(3), concepts/monotonic-sar-case-study(3)
- g5 理解為什麼 SAR 省電、monotonic 切換省在哪 → concepts/switching-schemes(27), concepts/monotonic-sar-case-study(20), sources/liu-2010-monotonic(9), concepts/sar-vs-pipeline(6), concepts/figures-of-merit(4)
- g6 會看一顆真實晶片的規格與 FoM → concepts/figures-of-merit(22), sources/liu-2010-monotonic(13), concepts/monotonic-sar-case-study(7), sources/tang-2022-survey(3), sources/hu-2024-hybrid(1)

### [2026-11-21 22:02:03 +0800] coverage gate — PASS
- g1 OK：5 頁、5 個來源
- g2 OK：5 頁、6 個來源
- g3 OK：5 頁、6 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、5 個來源
- g6 OK：5 頁、3 個來源

### [2026-11-21 22:02:03 +0800] evidence gate — PASS
- 40 張卡

### [2026-11-21 22:02:03 +0800] human approve gate — PASS

### [2026-11-21 22:02:03 +0800] faithfulness gate — PASS
- 17 頁；需要重寫：無

### [2026-11-21 22:02:03 +0800] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（17 頁，39 張卡片被引用，34 KB）

### [2026-11-21 22:51:08 +0800] retrieve — PASS
- g1 想起取樣為什麼會混疊、要怎麼限頻 → concepts/sampling-aliasing(23), sources/percy-ms-notes(16), concepts/comparator(14), sources/percy-meeting1(11), sources/liu-2010-monotonic(10)
- g2 想起量化雜訊怎麼決定 SNR 上限、沒滿 code 會掉多少 → concepts/quantization-noise-snr(45), sources/percy-ms-notes(26), concepts/adc-static-parameters(8), concepts/adc-dynamic-parameters(8), sources/liu-2010-monotonic(4)
- g3 會從頻譜讀動態參數、會算 ENOB 與 FoM、知道 INL 跳的原因 → concepts/adc-dynamic-parameters(22), concepts/adc-static-parameters(16), concepts/figures-of-merit(12), sources/liu-2010-monotonic(11), sources/percy-meeting1(8)
- g4 想起為什麼用 SAR、它怎麼運作 → concepts/sar-vs-pipeline(8), sources/razavi-2015(7), sources/saxena-lecture(5), concepts/binary-search(5), sources/liu-2010-monotonic(4)
- g5 想起 monotonic 解決什麼、怎麼算出省 81%、代價是什麼 → concepts/switching-schemes(40), concepts/monotonic-sar-case-study(19), sources/percy-meeting1(17), concepts/comparator(12), sources/liu-2010-monotonic(7)
- g6 想起代價帶來的電路對策：比較器、bootstrap、cross-coupled → sources/percy-meeting1(13), sources/liu-2010-monotonic(7), concepts/bootstrapped-switch(7), concepts/comparator(5), concepts/monotonic-sar-case-study(2)

### [2026-11-21 22:51:08 +0800] coverage gate — PASS
- g1 OK：5 頁、6 個來源
- g2 OK：5 頁、4 個來源
- g3 OK：5 頁、3 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、6 個來源
- g6 OK：5 頁、5 個來源

### [2026-11-21 22:51:08 +0800] evidence gate — PASS
- 74 張卡

### [2026-11-21 22:51:21 +0800] human approve gate — FAIL
- ❌ outline.md status = draft，需要人工改成 approved 才能往下

### [2026-11-21 22:52:33 +0800] human approve gate — PASS

### [2026-11-21 22:52:33 +0800] faithfulness gate — PASS
- 21 頁；需要重寫：無

### [2026-11-21 22:52:39 +0800] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（21 頁，71 張卡片被引用，50 KB）

### [2026-11-21 22:53:20 +0800] faithfulness gate — PASS
- 21 頁；需要重寫：無

### [2026-11-21 22:53:20 +0800] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（21 頁，71 張卡片被引用，50 KB）

### [2026-11-21 22:54:00 +0800] retrieve — PASS
- g1 想起取樣為什麼會混疊、要怎麼限頻 → concepts/sampling-aliasing(23), sources/percy-ms-notes(16), concepts/comparator(14), sources/percy-meeting1(11), sources/liu-2010-monotonic(10)
- g2 想起量化雜訊怎麼決定 SNR 上限、沒滿 code 會掉多少 → concepts/quantization-noise-snr(45), sources/percy-ms-notes(26), concepts/adc-static-parameters(8), concepts/adc-dynamic-parameters(8), sources/liu-2010-monotonic(4)
- g3 會從頻譜讀動態參數、會算 ENOB 與 FoM、知道 INL 跳的原因 → concepts/adc-dynamic-parameters(22), concepts/adc-static-parameters(16), concepts/figures-of-merit(12), sources/liu-2010-monotonic(11), sources/percy-meeting1(8)
- g4 想起為什麼用 SAR、它怎麼運作 → concepts/sar-vs-pipeline(8), sources/razavi-2015(7), sources/saxena-lecture(5), concepts/binary-search(5), sources/liu-2010-monotonic(4)
- g5 想起 monotonic 解決什麼、怎麼算出省 81%、代價是什麼 → concepts/switching-schemes(40), concepts/monotonic-sar-case-study(19), sources/percy-meeting1(17), concepts/comparator(12), sources/liu-2010-monotonic(7)
- g6 想起代價帶來的電路對策：比較器、bootstrap、cross-coupled → sources/percy-meeting1(13), sources/liu-2010-monotonic(7), concepts/bootstrapped-switch(7), concepts/comparator(5), concepts/monotonic-sar-case-study(2)

### [2026-11-21 22:54:00 +0800] coverage gate — PASS
- g1 OK：5 頁、6 個來源
- g2 OK：5 頁、4 個來源
- g3 OK：5 頁、3 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、6 個來源
- g6 OK：5 頁、5 個來源

### [2026-11-21 22:54:00 +0800] evidence gate — PASS
- 74 張卡

### [2026-11-21 22:54:00 +0800] human approve gate — PASS

### [2026-11-21 22:54:01 +0800] faithfulness gate — PASS
- 21 頁；需要重寫：無

### [2026-11-21 22:54:01 +0800] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（21 頁，71 張卡片被引用，49 KB）

### [2026-11-21 22:54:52 +0800] retrieve — PASS
- g1 想起取樣為什麼會混疊、要怎麼限頻 → concepts/sampling-aliasing(23), sources/percy-ms-notes(16), concepts/comparator(14), sources/percy-meeting1(11), sources/liu-2010-monotonic(10)
- g2 想起量化雜訊怎麼決定 SNR 上限、沒滿 code 會掉多少 → concepts/quantization-noise-snr(45), sources/percy-ms-notes(26), concepts/adc-static-parameters(8), concepts/adc-dynamic-parameters(8), sources/liu-2010-monotonic(4)
- g3 會從頻譜讀動態參數、會算 ENOB 與 FoM、知道 INL 跳的原因 → concepts/adc-dynamic-parameters(22), concepts/adc-static-parameters(16), concepts/figures-of-merit(12), sources/liu-2010-monotonic(11), sources/percy-meeting1(8)
- g4 想起為什麼用 SAR、它怎麼運作 → concepts/sar-vs-pipeline(8), sources/razavi-2015(7), sources/saxena-lecture(5), concepts/binary-search(5), sources/liu-2010-monotonic(4)
- g5 想起 monotonic 解決什麼、怎麼算出省 81%、代價是什麼 → concepts/switching-schemes(40), concepts/monotonic-sar-case-study(19), sources/percy-meeting1(17), concepts/comparator(12), sources/liu-2010-monotonic(7)
- g6 想起代價帶來的電路對策：比較器、bootstrap、cross-coupled → sources/percy-meeting1(13), sources/liu-2010-monotonic(7), concepts/bootstrapped-switch(7), concepts/comparator(5), concepts/monotonic-sar-case-study(2)

### [2026-11-21 22:54:52 +0800] coverage gate — PASS
- g1 OK：5 頁、6 個來源
- g2 OK：5 頁、4 個來源
- g3 OK：5 頁、3 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、6 個來源
- g6 OK：5 頁、5 個來源

### [2026-11-21 22:54:52 +0800] evidence gate — PASS
- 74 張卡

### [2026-11-21 22:54:52 +0800] human approve gate — PASS

### [2026-11-21 22:54:52 +0800] faithfulness gate — PASS
- 21 頁；需要重寫：無

### [2026-11-21 22:54:52 +0800] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（21 頁，71 張卡片被引用，49 KB）

### [2026-11-21 22:59:33 +0800] retrieve — PASS
- g1 想起取樣為什麼會混疊、要怎麼限頻 → concepts/sampling-aliasing(23), sources/percy-ms-notes(16), concepts/comparator(14), sources/percy-meeting1(11), sources/liu-2010-monotonic(10)
- g2 想起量化雜訊怎麼決定 SNR 上限、沒滿 code 會掉多少 → concepts/quantization-noise-snr(45), sources/percy-ms-notes(26), concepts/adc-static-parameters(8), concepts/adc-dynamic-parameters(8), sources/liu-2010-monotonic(4)
- g3 會從頻譜讀動態參數、會算 ENOB 與 FoM、知道 INL 跳的原因 → concepts/adc-dynamic-parameters(22), concepts/adc-static-parameters(16), concepts/figures-of-merit(12), sources/liu-2010-monotonic(11), sources/percy-meeting1(8)
- g4 想起為什麼用 SAR、它怎麼運作 → concepts/sar-vs-pipeline(8), sources/razavi-2015(7), sources/saxena-lecture(5), concepts/binary-search(5), sources/liu-2010-monotonic(4)
- g5 想起 monotonic 解決什麼、怎麼算出省 81%、代價是什麼 → concepts/switching-schemes(40), concepts/monotonic-sar-case-study(19), sources/percy-meeting1(17), concepts/comparator(12), sources/liu-2010-monotonic(7)
- g6 想起代價帶來的電路對策：比較器、bootstrap、cross-coupled → sources/percy-meeting1(13), sources/liu-2010-monotonic(7), concepts/bootstrapped-switch(7), concepts/comparator(5), concepts/monotonic-sar-case-study(2)

### [2026-11-21 22:59:33 +0800] coverage gate — PASS
- g1 OK：5 頁、6 個來源
- g2 OK：5 頁、4 個來源
- g3 OK：5 頁、3 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、6 個來源
- g6 OK：5 頁、5 個來源

### [2026-11-21 22:59:33 +0800] evidence gate — PASS
- 74 張卡

### [2026-11-21 22:59:33 +0800] human approve gate — PASS

### [2026-11-21 22:59:33 +0800] faithfulness gate — PASS
- 21 頁；需要重寫：無

### [2026-11-21 22:59:33 +0800] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（21 頁，71 張卡片被引用，50 KB）

### [2026-11-21 23:00:06 +0800] retrieve — PASS
- g1 想起取樣為什麼會混疊、要怎麼限頻 → concepts/sampling-aliasing(23), sources/percy-ms-notes(16), concepts/comparator(14), sources/percy-meeting1(11), sources/liu-2010-monotonic(10)
- g2 想起量化雜訊怎麼決定 SNR 上限、沒滿 code 會掉多少 → concepts/quantization-noise-snr(45), sources/percy-ms-notes(26), concepts/adc-static-parameters(8), concepts/adc-dynamic-parameters(8), sources/liu-2010-monotonic(4)
- g3 會從頻譜讀動態參數、會算 ENOB 與 FoM、知道 INL 跳的原因 → concepts/adc-dynamic-parameters(22), concepts/adc-static-parameters(16), concepts/figures-of-merit(12), sources/liu-2010-monotonic(11), sources/percy-meeting1(8)
- g4 想起為什麼用 SAR、它怎麼運作 → concepts/sar-vs-pipeline(8), sources/razavi-2015(7), sources/saxena-lecture(5), concepts/binary-search(5), sources/liu-2010-monotonic(4)
- g5 想起 monotonic 解決什麼、怎麼算出省 81%、代價是什麼 → concepts/switching-schemes(40), concepts/monotonic-sar-case-study(19), sources/percy-meeting1(17), concepts/comparator(12), sources/liu-2010-monotonic(7)
- g6 想起代價帶來的電路對策：比較器、bootstrap、cross-coupled → sources/percy-meeting1(13), sources/liu-2010-monotonic(7), concepts/bootstrapped-switch(7), concepts/comparator(5), concepts/monotonic-sar-case-study(2)

### [2026-11-21 23:00:06 +0800] coverage gate — PASS
- g1 OK：5 頁、6 個來源
- g2 OK：5 頁、4 個來源
- g3 OK：5 頁、3 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、6 個來源
- g6 OK：5 頁、5 個來源

### [2026-11-21 23:00:06 +0800] evidence gate — PASS
- 74 張卡

### [2026-11-21 23:00:06 +0800] human approve gate — PASS

### [2026-11-21 23:00:06 +0800] faithfulness gate — PASS
- 21 頁；需要重寫：無

### [2026-11-21 23:00:06 +0800] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（21 頁，71 張卡片被引用，50 KB）

### [2026-11-21 15:00:46 +0000] retrieve — PASS
- g1 想起取樣為什麼會混疊、要怎麼限頻 → concepts/sampling-aliasing(23), sources/percy-ms-notes(16), concepts/comparator(14), sources/percy-meeting1(11), sources/liu-2010-monotonic(10)
- g2 想起量化雜訊怎麼決定 SNR 上限、沒滿 code 會掉多少 → concepts/quantization-noise-snr(45), sources/percy-ms-notes(26), concepts/adc-static-parameters(8), concepts/adc-dynamic-parameters(8), sources/liu-2010-monotonic(4)
- g3 會從頻譜讀動態參數、會算 ENOB 與 FoM、知道 INL 跳的原因 → concepts/adc-dynamic-parameters(22), concepts/adc-static-parameters(16), concepts/figures-of-merit(12), sources/liu-2010-monotonic(11), sources/percy-meeting1(8)
- g4 想起為什麼用 SAR、它怎麼運作 → concepts/sar-vs-pipeline(8), sources/razavi-2015(7), sources/saxena-lecture(5), concepts/binary-search(5), sources/liu-2010-monotonic(4)
- g5 想起 monotonic 解決什麼、怎麼算出省 81%、代價是什麼 → concepts/switching-schemes(40), concepts/monotonic-sar-case-study(19), sources/percy-meeting1(17), concepts/comparator(12), sources/liu-2010-monotonic(7)
- g6 想起代價帶來的電路對策：比較器、bootstrap、cross-coupled → sources/percy-meeting1(13), sources/liu-2010-monotonic(7), concepts/bootstrapped-switch(7), concepts/comparator(5), concepts/monotonic-sar-case-study(2)

### [2026-11-21 15:00:46 +0000] coverage gate — PASS
- g1 OK：5 頁、6 個來源
- g2 OK：5 頁、4 個來源
- g3 OK：5 頁、3 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、6 個來源
- g6 OK：5 頁、5 個來源

### [2026-11-21 15:00:46 +0000] evidence gate — PASS
- 74 張卡

### [2026-11-21 15:00:46 +0000] human approve gate — PASS

### [2026-11-21 15:00:56 +0000] faithfulness gate — PASS
- 21 頁；需要重寫：無

### [2026-11-21 15:00:57 +0000] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（21 頁，71 張卡片被引用，50 KB）

### [2026-11-22 13:50:43 +0000] retrieve — PASS
- g1 想起取樣為什麼會混疊、要怎麼限頻 → concepts/sampling-aliasing(23), sources/percy-ms-notes(16), concepts/comparator(14), sources/percy-meeting1(11), sources/liu-2010-monotonic(10)
- g2 想起量化雜訊怎麼決定 SNR 上限、沒滿 code 會掉多少 → concepts/quantization-noise-snr(45), sources/percy-ms-notes(26), concepts/adc-static-parameters(8), concepts/adc-dynamic-parameters(8), sources/liu-2010-monotonic(4)
- g3 會從頻譜讀動態參數、會算 ENOB 與 FoM、知道 INL 跳的原因 → concepts/adc-dynamic-parameters(22), concepts/adc-static-parameters(16), concepts/figures-of-merit(12), sources/liu-2010-monotonic(11), sources/percy-meeting1(8)
- g4 想起為什麼用 SAR、它怎麼運作 → concepts/sar-vs-pipeline(8), sources/razavi-2015(7), sources/saxena-lecture(5), concepts/binary-search(5), sources/liu-2010-monotonic(4)
- g5 想起 monotonic 解決什麼、怎麼算出省 81%、代價是什麼 → concepts/switching-schemes(40), concepts/monotonic-sar-case-study(19), sources/percy-meeting1(17), concepts/comparator(12), sources/liu-2010-monotonic(8)
- g6 想起代價帶來的電路對策：比較器、bootstrap、cross-coupled → sources/percy-meeting1(13), sources/liu-2010-monotonic(7), concepts/bootstrapped-switch(7), concepts/comparator(5), concepts/monotonic-sar-case-study(2)

### [2026-11-22 13:50:43 +0000] coverage gate — PASS
- g1 OK：5 頁、6 個來源
- g2 OK：5 頁、4 個來源
- g3 OK：5 頁、3 個來源
- g4 OK：5 頁、5 個來源
- g5 OK：5 頁、6 個來源
- g6 OK：5 頁、5 個來源

### [2026-11-22 13:50:43 +0000] evidence gate — PASS
- 74 張卡

### [2026-11-22 13:50:43 +0000] human approve gate — PASS

### [2026-11-22 13:50:44 +0000] faithfulness gate — PASS
- 21 頁；需要重寫：無

### [2026-11-22 13:50:44 +0000] render + render gate — PASS
- 輸出 decks/sar-adc/index.html（21 頁，71 張卡片被引用，50 KB）

