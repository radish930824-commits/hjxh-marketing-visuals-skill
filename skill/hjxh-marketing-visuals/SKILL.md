---
name: hjxh-marketing-visuals
description: Use when a request mentions 皇家小虎 or HJXH and involves creating, planning, auditing, revising, approving, or converting marketing visuals, Canva canvases, HTML/PDF reports, branded interfaces, or reusing the approved pixel Tiger pet assets.
---

# 皇家小虎营销视觉

默认使用中文；用户明确要求时切换为英文。制作和审核必须以现有品牌资产真实性为最高优先级。

## 开始任务

1. 每次任务都读取 `references/brand-guidelines.md`。
2. 制作成品或输出制作方案时，读取 `references/creation-workflow.md`。
3. 制作 HTML/PDF 周报、周报模板、经营周报或工作周报时，读取 `references/weekly-report-template.md`；16:9 演示与大屏使用 `assets/templates/周报横屏版.html`，A4 打印与长文档使用 `assets/templates/周报竖屏版.html`。
4. 审核或修改已有图片时，读取 `references/review-workflow.md` 和 `references/audit-report-template.md`。
5. 涉及 Canva 可编辑画布、审批改图、按批准修改、导出图片时，读取 `references/canva-approval-workflow.md`。
6. 渠道或尺寸缺失时，读取 `references/channel-sizes.md`，推荐 1-3 个尺寸并确认。
7. 从 `assets/manifest.json` 选择素材，不得静默替换缺失资产。
8. 使用像素小虎、动画宠物或精灵图时，读取 `references/pixel-pet.md`，优先复用已确认素材。
9. 涉及品牌 App、桌面界面或交互原型的设计审核时，读取 `references/apple-design-integration.md`；按场景选用同仓库的 `apple-design`，普通海报和宠物位图不套用平台控件规则。

## 任务分类

- 制作营销图片成品
- 制作 Canva 可编辑画布并导出图片
- 制作 HTML/PDF 周报模板或成品
- 制作数据PPT模版或完整横屏年中分析报告
- 输出详细制作方案
- 审核已有营销图片
- 审核并修改已有营销图片
- 按严格审批流程修改营销图片
- 复用已确认的像素小虎形象与动画宠物素材
- 皇家小虎品牌界面的视觉与可访问性审核

## 硬性边界

- MUST 直接使用打包的 Logo；Logo 缺失时停止制作。
- MUST NOT 重绘、仿制、变形、裁切或生成 Logo。
- MUST 只能使用皇家小虎品牌色：小虎黄 `#FFCC00`、小虎咖 `#632C16`、小虎红 `#D93924`、白色 `#FFFFFF`；禁止使用品牌色以外的颜色。
- MUST 使用指定字体和真实产品素材。
- MUST 强制按文字类型用字体：中文必须使用华康圆体系列，中文标题最粗只能使用华康圆体 W9；英文和数字必须使用 GOTHAMRND 系列，禁止对英文或数字使用华康圆体。
- MUST 在交付任何成品前执行规范审核。
- 任一 MUST 或 MUST NOT 违规，审核结论必须为“不通过”。
- Logo、品牌色、字体、IP 身份或新动作、产品事实、促销价格与条款的修改必须先获得用户确认。
- 产品或标准 IP 素材不足时，先报告限制；经确认后才可使用占位方案或制作明确标记的“待审核草案”。
- 已确认的像素宠物是限定用途的 IP 衍生资产，适用范围与已知色阶限制见 `references/pixel-pet.md`；不得将其视为对其他 Logo、品牌色、字体或 3D 标准 IP 规则的全面修改。

## 工具路由

- 精准文字排版、可编辑设计、真实素材组合：优先 Canva。
- 创意背景或新场景：优先 ImageGen。
- 同时需要创意场景和准确品牌排版：组合使用 ImageGen 与 Canva。
- ImageGen 绝不能用于生成或仿制 Logo。
- 审批改图默认使用 Canva 承载可编辑画布，Codex 管理审核、批准项和修改说明。
- 已有像素宠物优先直接取用打包 PNG/GIF/MP4；创建、更新或启用 ChatGPT 宠物时使用可用的 Pets 工具及对应宠物技能，保留验证和激活权限边界。

## 交付

- Canva：可编辑设计与导出图片。
- ImageGen：图片、制作说明与审核结果。
- 方案任务：构图、素材选择、文案层级、尺寸、工具建议和制作提示词。
- 审核任务：结构化审核报告；高风险修改仅在确认后执行。
- 审批改图任务：默认交付 Canva 可编辑画布、导出图片、审核/修改说明。
- 周报任务：根据输出场景选择周报横屏版或周报竖屏版，交付脱敏模板或已填充 HTML/PDF 周报，并说明封面、页头、页尾是否符合固定排版逻辑。
- 数据PPT任务：需要完整横屏年中/半年经营分析时，使用 `assets/templates/数据PPT模版.html`；必须填充当前数据，且不得保留任何样例报告的省区、客户、门店、人员、经营数值、日期或现场照片。
