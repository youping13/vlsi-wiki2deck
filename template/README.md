# deck.json schema（template/deck.html 用）

```json
{
  "title": "簡報標題", "author": "作者", "date": "2026-11-21",
  "wiki_base": "../../wiki/",
  "slides": [
    {"id":"s1","layout":"title","kicker":"…","title":"…","subtitle":"…","notes":"…"},
    {"id":"s2","layout":"bullets","kicker":"…","title":"…","en":"English","bullets":["… [c1]"],"notes":"…"},
    {"id":"s3","layout":"two-col","title":"…","left_title":"…","left":["… [c2]"],"right_title":"…","right":["… [c3]"]},
    {"id":"s4","layout":"diagram","title":"…","bullets":["… [c4]"],"svg":"<svg viewBox='0 0 600 400'>…</svg>"},
    {"id":"s4b","layout":"diagram","title":"…","bullets":["$V_X = V_i - \\frac{V_R}{2}$ [c4]"],"figure":"liu2010-fig04"},
    {"id":"s5","layout":"quiz","title":"…","question":"…","options":["A","B","C","D"],"answer":1,"explain":"… [c5]"},
    {"id":"s6","layout":"summary","title":"…","bullets":["… [c6]"]}
  ]
}
```
快捷鍵：← → 換頁、N 講稿、O 總覽、P 列印成 PDF。滑鼠移到引用標記 `c#` 上會顯示 wiki 原文。

- `$…$` 行內公式、`$$…$$` 置中公式（KaTeX，離線）
- `figure` 填 `wiki/figures.md` 的 id，會自動附上圖說與出處；沒有 `figure` 時用 `svg`
