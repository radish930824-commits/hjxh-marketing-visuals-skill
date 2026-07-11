# 皇家小虎周报模板

Use this reference when creating or revising 皇家小虎 HTML/PDF 周报、经营周报、工作周报。This template is derived from a week-26 report layout, but it is fully desensitized: never copy real week numbers, dates, amounts, customer names, city details, activity names, or source image filenames into the skill output unless the user provides them for the current report.

## Data safety

- MUST treat bundled template content as layout guidance only.
- MUST replace all business content with user-provided current-week data or placeholders.
- MUST NOT preserve historical values from any sample report.
- Use placeholders such as `{{week_label}}`, `{{region_name}}`, `{{date_range}}`, `{{province_a}}`, `{{province_b}}`, `{{page_number}}`, `{{module_name}}`, `{{footer_context}}`.
- If source data is incomplete, mark the missing section as pending instead of inventing numbers.

## 模板选择

| 模板 | 资产路径 | 使用场景 |
|---|---|---|
| 周报横屏版 | `assets/templates/周报横屏版.html` | 16:9 演示、大屏、会议汇报；固定 1600×900、10 页、单文件 HTML |
| 周报竖屏版 | `assets/templates/周报竖屏版.html` | A4 打印、PDF、长文档阅读；固定 210mm×297mm、10 页 |

- 用户明确要求 16:9、宽屏、横屏、演示稿或大屏时，MUST 使用周报横屏版。
- 用户明确要求 A4、打印、竖屏、纵向 PDF 时，MUST 使用周报竖屏版。
- 渠道或方向未说明时，先确认横屏或竖屏；不得静默混用两套版式。
- 横屏版封面左下 Logo 使用 `logo-weekly-report-cover-horizontal`，路径为 `assets/logos/周报横屏版封面Logo.png`；保持完整比例，不得裁切、拉伸或重新排字。

## Fixed report structure

两套模板都保持相同的 10 页信息结构：

| Page | Purpose |
|---|---|
| P1 | Cover |
| P2 | Province A performance overview |
| P3 | Province A customer / city detail |
| P4 | Province B performance overview |
| P5 | Province B customer / city detail |
| P6 | Regional work summary, issues, next plan |
| P7 | Province A issues and next plan |
| P8 | Province B issues and next plan |
| P9 | Weekly activity photo record |
| P10 | Thanks / closing |

Do not add, remove, or reorder pages unless the user explicitly asks.

## Cover layout logic

The cover is the strongest fixed template element.

Layout:

1. Full-page A4 portrait yellow background `#FFCC00`.
2. Add one large rounded-rectangle border inset from all page edges. Border uses `#632C16` with low opacity; no decorative colors.
3. Center a vertical stack, both horizontally and vertically.
4. Top: official vertical logo lockup from packaged assets. Keep original ratio and do not crop.
5. Below logo: pill-shaped week tag, brown fill `#632C16`, white text `#FFFFFF`.
6. Main title: region name, large W9 Chinese font, brown `#632C16`.
7. Subtitle: report title, W9 Chinese font, brown.
8. Divider: short horizontal red line `#D93924`.
9. Date: `{{date_range}}`, Gotham Rounded for numbers and separators, brown.
10. Province pills: centered row; yellow fill, brown border, brown text.

Cover content order:

```text
{{vertical_logo}}
{{week_label}}
{{region_name}}
{{report_title}}
{{red_divider}}
{{date_range}}
{{province_a}}  {{province_b}}
```

Cover constraints:

- MUST NOT place business metrics on the cover.
- MUST NOT use activity photos, product photos, or extra illustrations on the cover unless the user explicitly asks.
- MUST keep the cover visually quiet: large yellow field, centered logo/title stack, strong whitespace.
- MUST keep all text and border colors within the four brand colors.

## Header layout logic

Every non-cover content page uses the same header bar.

Layout:

1. Header spans full page width at the top.
2. Header background is brand yellow `#FFCC00`.
3. Header height is visually thick enough to feel like a brand band; use about `16mm` for A4 print.
4. Left side: official horizontal logo, height about `12mm`, original ratio.
5. Right side: page meta, for example `第{{page_number}}页 · {{module_name}}`.
6. Header uses horizontal padding about `14mm`.
7. Page meta uses brown `#632C16`, W9 / bold weight, letter spacing.

Header HTML pattern:

```html
<div class="page-header">
  <img src="{{logo_horizontal_path}}" alt="皇家小虎">
  <span class="meta">第{{page_number}}页 · {{module_name}}</span>
</div>
```

Header constraints:

- MUST use the packaged horizontal logo. Do not recreate the logo with text.
- MUST keep page meta on the right with `margin-left: auto`.
- MUST NOT translate the page meta into English.
- MUST NOT put charts, KPI numbers, or decorations in the header.

## Footer layout logic

Every non-cover content page uses the same footer bar.

Layout:

1. Footer spans full page width at the bottom.
2. Footer background is brand yellow `#FFCC00`.
3. Footer height is thinner than the header; use about `8mm` for A4 print.
4. Left side: brand mark text `皇家小虎 · 全球美食私厨`.
5. Right side: report context, for example `{{module_context}} · 周报 · {{date_range}}`.
6. Footer text uses brown `#632C16`, bold, small size, controlled letter spacing.
7. Use `justify-content: space-between`.

Footer HTML pattern:

```html
<div class="page-footer">
  <span class="brand-mark">皇家小虎 · 全球美食私厨</span>
  <span>{{footer_context}} · 周报 · {{date_range}}</span>
</div>
```

Footer constraints:

- MUST NOT remove the footer from content pages.
- MUST NOT add English translation.
- MUST keep the date range consistent with the cover.
- MUST use only brand yellow background and brown text.

## Page frame and body

- Page size: A4 portrait, `210mm × 297mm`.
- Each `.page` is a flex column so header and footer stay fixed at top and bottom.
- `.page-inner` owns the page body and should use generous padding.
- Body content must not overlap header or footer.
- For PDF export, verify every page is complete and no content crosses page boundaries.

Recommended page skeleton:

```html
<div class="page">
  {{page_header}}
  <div class="page-inner">
    {{page_body}}
  </div>
  {{page_footer}}
</div>
```

## Brand rules for weekly reports

- MUST use only brand colors: `#FFCC00`, `#632C16`, `#D93924`, `#FFFFFF`.
- MUST NOT use blue, green, purple, gray, or extra cream backgrounds in charts, cards, page backgrounds, or decorations.
- Chinese text must use 华康圆体; Chinese titles must not exceed W9.
- English and numbers must use GOTHAMRND; never use 华康圆体 for English or numbers.
- Logo must come from packaged assets and must not be cropped, stretched, recolored, shadowed, outlined, or redrawn.

## Template assets

按输出方向复制对应模板：

```text
assets/templates/周报横屏版.html
assets/templates/周报竖屏版.html
```

两套 HTML 均使用脱敏占位符。横屏版已经内嵌字体、Logo、封面/结束图片，可作为单文件直接打开；竖屏版保留 A4 封面、页头、页尾基础结构。
