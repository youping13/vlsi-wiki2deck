# 節點 8：逐頁稿（AI）

輸入：outline.md（approved）、evidence.json、`template/README` 中的 deck.json schema
輸出：deck.json

```
依大綱把每一頁寫成 deck.json 的一個 slide。
- 讀者完全沒學過；每頁一個觀念；bullets ≤ 5；每個 bullet ≤ 60 字
- 每個 bullet / left / right / explain 結尾都要有 [c?] 引用，而且只能用大綱裡這頁列出的卡片
- 所有數字必須「原樣」出現在被引用卡片的 wiki_text 裡（例：卡片寫 1,024 就寫 1,024）
- 圖（svg）裡的數字也一樣，必須出現在本頁引用的卡片中
- 公式用 LaTeX（$…$），分數寫成 \frac{a}{b}
- 需要論文原圖時，從 wiki/figures.md 挑 id 填到 "figure"，並確認本頁有引用該論文的卡片
- notes 寫 2–3 句講稿，口語
重寫模式：只輸出 check-report 指定的 slide id，其餘頁不要動。
```
