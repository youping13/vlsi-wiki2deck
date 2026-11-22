# 節點 6：大綱（AI）→ 節點 7 人工確認

輸入：brief.md、evidence.json　輸出：outline.md

```
依 brief 的學習目標排出 12–16 頁的教學順序：
比喻引入 → 方塊圖 → 原理 → 數字 → 真實案例 → 小測驗 → 總結。
每頁一行：`<n>. [layout] 標題 — goals: g? — cards: c?,c?`
layout 只能是 title / bullets / two-col / diagram / quiz / summary。
每個 goal 至少出現在一頁；每頁至少 1 張卡（title 頁除外）。
檔案開頭寫 `status: draft`。
```
人工確認：讀過大綱後，把 `status: draft` 改成 `status: approved`。要修改的話直接改大綱，或在 brief 補關鍵字後重跑 retrieve。
