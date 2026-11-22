# 節點 4：證據卡（AI）

輸入：`decks/<d>/brief.md`、`decks/<d>/retrieval.json`、retrieval 命中的 wiki 頁
輸出：`decks/<d>/evidence.json`

```
你是教學簡報的研究助理。只能使用下列 wiki 頁面。
對 brief 裡的每個學習目標，挑出 2–6 段「能直接支持教學」的句子做成證據卡。
規則：
1. wiki_text 必須從頁面「逐字複製」，可以只取一個完整 bullet 或一句話，不准改寫、不准合併兩段。
2. 優先挑：比喻、定義、帶數字的句子、衝突說明。
3. 每張卡：{"id":"c<n>","goal":"g<k>","page":"<節點>/<slug>"（例：mixed-signal/monotonic/switching-schemes）,"wiki_text":"…","why":"這張卡支持什麼"}
4. 數字句請連同 (src: …) 一起複製。
只輸出 JSON：{"cards":[…]}
```
失敗處理：evidence gate 列出的卡片編號重新挑，其他卡不動。
