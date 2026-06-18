# 皇家小虎 AI 品牌视觉规范

> 文档标识：HJXH Design  
> 品牌名称：皇家小虎  
> 品牌口号：全球美食私厨  
> 适用对象：AI 设计工具、内容生成模型、设计师、开发人员及外部制作团队  
> 规范级别：基础视觉规范 v1.1  

## 1. 使用原则

本文件用于指导 AI 生成、修改或审核皇家小虎品牌相关视觉内容。

规则关键词含义：

- **MUST**：必须遵守，不得自行变更。
- **MUST NOT**：禁止执行。
- **SHOULD**：无特殊原因时应遵守。
- **MAY**：可根据场景选择。
- **待确认**：根据现有资产补充的默认规则，并非原始品牌规范中的明确规定。

规则冲突时，优先级依次为：

1. Logo 完整性与品牌资产真实性
2. 品牌色准确性
3. 品牌字体与文字层级
4. 信息可读性和对比度
5. 构图与装饰风格

## 2. 品牌识别

### 2.1 品牌核心

- 品牌名称：`皇家小虎`
- 品牌口号：`全球美食私厨`
- 品牌识别主体：头戴皇冠的黄色小虎形象
- 主要视觉印象：鲜明、亲和、活力、美食感、圆润、具有识别度

### 2.2 品牌资产目录

所有 AI 任务 MUST 优先引用现有资产，不得重新绘制 Logo 或用文字模拟 Logo。

| 资产标识 | 文件路径 | 推荐用途 |
|---|---|---|
| `logo-horizontal-with-tagline` | `logo-png/皇家小虎logo组合-主0.png` | 横向空间、页面页眉、网站导航、横版物料 |
| `logo-vertical-with-tagline` | `logo-png/皇家小虎logo组合-主1.png` | 接近方形或纵向空间、封面、品牌主视觉 |
| `logo-yellow-panel-no-tagline` | `logo-png/皇家小虎logo组合-0316-RGB_画板 1 副本 22.png` | 黄色品牌条、横向标签、不需要口号的场景 |
| `logo-yellow-panel-with-tagline` | `logo-png/皇家小虎logo组合-0316-RGB_画板 1 副本 23.png` | 黄色品牌条、横向标签、需要完整品牌信息的场景 |
| `avatar-yellow-background` | `logo-png/皇家小虎logo组合-0316-RGB_画板 1 副本 25.png` | 固定黄色背景头像、方形品牌卡片 |
| `avatar-transparent` | `logo-png/皇家小虎logo组合-0316-RGB_画板 1 副本 26.png` | 默认头像、App 图标、社交媒体头像、独立品牌符号 |

### 2.3 IP 与产品资产目录

| 资产标识 | 文件路径 | 推荐用途 |
|---|---|---|
| `ip-specification` | `皇家小虎IP规范/皇家小虎IP介绍.png` | IP 建模、形象审核、衍生设计的首要参考 |
| `ip-action-clap` | `皇家小虎IP规范/动作 (1).png` | 鼓掌、欢迎、庆祝类画面 |
| `ip-action-thumbs-up` | `皇家小虎IP规范/动作 (2).png` | 推荐、认可、品质背书类画面 |
| `ip-action-confident` | `皇家小虎IP规范/动作 (3).png` | 自信站立、鼓励、品牌宣言类画面 |
| `ip-action-wave` | `皇家小虎IP规范/动作 (4).png` | 挥手、问候、服务引导类画面 |
| `ip-action-run` | `皇家小虎IP规范/动作 (5).png` | 奔跑、活力、行动号召类画面 |
| `product-pizza` | `皇家小虎主产品摄影图/披萨.png` | 披萨产品真实摄影参考 |
| `product-sausage` | `皇家小虎主产品摄影图/烤肠.png` | 烤肠产品真实摄影参考 |
| `product-egg-tart` | `皇家小虎主产品摄影图/蛋挞.png` | 蛋挞产品真实摄影参考 |
| `product-cheese-bake` | `皇家小虎主产品摄影图/芝士焗.png` | 芝士焗产品真实摄影参考 |
| `product-fries` | `皇家小虎主产品摄影图/薯条.png` | 薯条产品真实摄影参考 |

动作名称根据现有画面含义建立，属于便于 AI 调用的语义别名；原始文件名保持不变。

## 3. Logo 使用规则

### 3.1 Logo 选择

- 横向版面或宽高比明显大于 `1:1` 时，SHOULD 使用 `logo-horizontal-with-tagline`。
- 封面、海报中心或接近方形版面时，SHOULD 使用 `logo-vertical-with-tagline`。
- 头像、App 图标及小尺寸品牌符号 MUST 使用 `avatar-transparent` 或 `avatar-yellow-background`。
- 当品牌首次出现或需要完整品牌识别时，SHOULD 使用带口号版本。
- 当空间不足以清晰显示口号时，MAY 使用不带口号版本或独立头像。

### 3.2 Logo 完整性

- MUST 直接使用指定 Logo 文件。
- MUST 保持原始宽高比。
- MUST 保持 Logo 中头像、品牌名称、口号及注册标志的原始关系。
- MUST NOT 重绘、描摹、重新排字或用生成式 AI 仿制 Logo。
- MUST NOT 拉伸、压缩、旋转、倾斜或透视变形。
- MUST NOT 裁切 Logo 主体、品牌名称、口号或注册标志。
- MUST NOT 修改 Logo 颜色、透明度或内部元素。
- MUST NOT 添加描边、阴影、发光、渐变、纹理、滤镜或三维效果。
- MUST NOT 将其他图形覆盖在 Logo 上。

### 3.3 安全区域与最小尺寸

以下为 AI 执行默认规则，状态为 **待确认**：

- Logo 周围最小净空 SHOULD 不低于头像圆形直径的 `12.5%`。
- Logo 与画布边缘的距离 SHOULD 不低于 Logo 整体高度的 `10%`。
- 当品牌口号无法清晰阅读时，MUST 改用不带口号版本，不得继续缩小完整 Logo。
- 独立头像在数字界面中的显示尺寸 SHOULD 不小于 `32 × 32 px`。
- 带品牌名称的组合 Logo 在数字界面中的显示宽度 SHOULD 不小于 `160 px`。

## 4. 品牌色

### 4.1 标准颜色

| Token | 名称 | HEX | RGB | CMYK | Pantone | 主要用途 |
|---|---|---|---|---|---|---|
| `brand.yellow` | 小虎黄 | `#FFCC00` | `255, 204, 0` | `0, 30, 100, 0` | `7549 C` | 主背景、品牌识别、重点色块 |
| `brand.brown` | 小虎咖 | `#632C16` | `99, 44, 22` | `55, 85, 100, 40` | `4695 C` | 标题、正文、Logo 文字、深色元素 |
| `brand.red` | 小虎红 | `#D93924` | `217, 57, 36` | `0, 100, 100, 0` | `2347 C` | 小面积强调、促销信息、关键提示 |
| `neutral.white` | 白色 | `#FFFFFF` | `255, 255, 255` | - | - | 留白、卡片、浅色背景 |

### 4.2 颜色使用规则

- MUST 使用上述准确色值，不得凭视觉近似替换。
- 小虎黄 SHOULD 作为最主要的品牌识别色。
- 小虎咖 SHOULD 用于标题、正文和小虎黄背景上的主要文字。
- 小虎红 MUST 作为小面积强调色，不得替代小虎黄成为大面积主背景。
- SHOULD 优先使用小虎黄、小虎咖与白色构成主要画面。
- MUST NOT 未经确认引入与品牌主色冲突的高饱和主色。
- MUST NOT 对品牌标准色应用会明显改变颜色识别的透明度、滤镜或渐变。
- 正文文字与背景 MUST 保持清晰可读；若品牌色组合无法满足可读性，优先使用小虎咖或白色作为文字色。

### 4.3 默认颜色比例

以下为 AI 执行默认规则，状态为 **待确认**：

- 小虎黄：`50%–70%`
- 白色或浅色留白：`20%–40%`
- 小虎咖：`10%–25%`
- 小虎红：不超过 `10%`

## 5. 品牌字体

### 5.1 中文字体映射

| 用途 | MUST 使用字体 | 文件路径 |
|---|---|---|
| 中文主标题 | 华康圆体 W9 | `皇家小虎品牌标准字体/44华康圆体W9.TTF` |
| 中文副标题 | 华康圆体 W8 | `皇家小虎品牌标准字体/43华康圆体W8.TTF` |
| 中文重点正文 | 华康圆体 W7 | `皇家小虎品牌标准字体/42华康圆体W7.TTF` |
| 中文普通正文 | 华康圆体 W5 | `皇家小虎品牌标准字体/41华康圆体W5.TTF` |
| 中文轻量辅助文字 | 华康圆体 W3 | `皇家小虎品牌标准字体/40华康圆体W3.TTF` |
| 中文超重强调标题 | 华康圆体 W12 | `皇家小虎品牌标准字体/45华康圆体W12.TTF` |

### 5.2 英文字体映射

| 用途 | MUST 使用字体 | 文件路径 |
|---|---|---|
| 英文主标题 | Gotham Rounded Bold | `皇家小虎品牌标准字体/GOTHAMRND-BOLD.OTF` |
| 英文副标题与强调 | Gotham Rounded Medium | `皇家小虎品牌标准字体/GOTHAMRND-MEDIUM.OTF` |
| 英文正文 | Gotham Rounded Book | `皇家小虎品牌标准字体/GOTHAMRND-BOOK.OTF` |
| 英文辅助文字 | Gotham Rounded Light | `皇家小虎品牌标准字体/GOTHAMRND-LIGHT.OTF` |

### 5.3 字体规则

- MUST 优先使用指定字体文件，不得用外观相似字体替换。
- MUST NOT 使用字体软件模拟加粗、倾斜或拉伸。
- MUST NOT 在同一页面中无目的地混用多个中文字族。
- SHOULD 使用小虎咖作为品牌标题和主要正文颜色。
- 中文正文 SHOULD 使用 W5；重点信息 SHOULD 使用 W7。
- 中文主标题 SHOULD 使用 W9；仅极强强调时 MAY 使用 W12。
- 英文文字 MUST 使用 Gotham Rounded 字族。

## 6. 默认文字层级

以下为 AI 执行默认规则，状态为 **待确认**。字号可按画布等比例缩放，但层级关系 MUST 保持。

| 层级 | 字体 | 相对字号 | 建议行高 |
|---|---|---:|---:|
| H1 主标题 | 华康圆体 W9 / Gotham Rounded Bold | `1.00` | `1.15–1.25` |
| H2 副标题 | 华康圆体 W8 / Gotham Rounded Medium | `0.65–0.75` | `1.20–1.30` |
| H3 小标题 | 华康圆体 W7 / Gotham Rounded Medium | `0.45–0.55` | `1.25–1.35` |
| 正文 | 华康圆体 W5 / Gotham Rounded Book | `0.30–0.40` | `1.45–1.70` |
| 辅助文字 | 华康圆体 W3 / Gotham Rounded Light | `0.22–0.28` | `1.40–1.60` |

## 7. 视觉语言

### 7.1 推荐方向

- SHOULD 使用圆润、清晰、亲和的视觉形态。
- SHOULD 使用充足留白，避免画面拥挤。
- SHOULD 以大面积小虎黄、白色留白和小虎咖文字建立品牌识别。
- MAY 使用圆角卡片、圆形容器和柔和几何形状呼应 Logo。
- MAY 小面积使用小虎红突出促销、价格、行动按钮或关键提示。
- 食品图片 SHOULD 明亮、清晰、有食欲，并保持自然色彩。

### 7.2 禁止方向

- MUST NOT 使用阴暗、冷酷、金属感或赛博朋克风格作为品牌主视觉。
- MUST NOT 使用尖锐、攻击性强或过度复杂的几何装饰。
- MUST NOT 使用大面积低对比文字。
- MUST NOT 让装饰元素抢占 Logo 或核心产品信息的视觉优先级。
- MUST NOT 将小虎红作为整页主背景，除非用户明确批准。

## 8. 场景规则

### 8.1 皇家小虎 IP 形象规范

- IP 标准风格 MUST 为 `Q版 / 潮玩感 / 3D公仔`，性格表达 SHOULD 体现王者、勇敢、自信与可爱。
- 身体比例 MUST 保持大头小身体，头部约占整体高度的 `60%–65%`。
- 表面材质 SHOULD 呈现光滑塑料质感；皇冠内部使用局部红色绒面感。
- IP 的正面、背面、左侧、右侧及补充视角 MUST 以 `皇家小虎IP规范/皇家小虎IP介绍.png` 为结构依据。
- 皇冠 MUST 保持 8 颗均匀分布的球形金色珠饰，正面通常可见 5 颗；珠饰直径与皇冠整体高度约为 `1:3`。
- 手臂虎纹每侧 2 条、腿部虎纹每侧 2 条，左右对称；尾部末端保留 1 条虎纹。
- 眼睛 MUST 保持上扬杏仁形或略尖倒三角感、深色外轮廓与红棕至琥珀渐变。
- 腹部白色区域 MUST 保持上窄下宽、边缘圆润的纵向椭圆或水滴形，并从下巴延伸至腹部中段。
- 额头“王”字 MUST 保持三横结构，中间一横更长且最突出，内部转角圆润。
- IP 标准色使用小虎黄 `#FFCC00`、白色 `#FFFFFF`、小虎咖 `#632C16`、小虎红 `#D93924`、皇冠金色与皇冠红色绒面。
- AI MUST 优先直接使用现有动作素材。未经批准，MUST NOT 改变脸部、皇冠、虎纹、尾巴、身体比例、标准色或角色气质。
- 新动作或新视角仅可作为待审核草案，MUST 明确标记为“非标准动作”。

### 8.2 主产品摄影规范

皇家小虎主产品包括披萨、烤肠、蛋挞、芝士焗和薯条。AI MUST 优先使用目录内真实产品图，不得凭空重绘或改变产品事实。

| 产品 | 标准参考 | 视觉重点 |
|---|---|---|
| 披萨 | `皇家小虎主产品摄影图/披萨.png` | 透明背景、整饼与拉丝切片、真实配料及木质托盘 |
| 烤肠 | `皇家小虎主产品摄影图/烤肠.png` | 白底或抠图展示、烤制光泽、切面与肉质 |
| 蛋挞 | `皇家小虎主产品摄影图/蛋挞.png` | 透明背景近景、酥皮层次、焦糖化蛋液表面 |
| 芝士焗 | `皇家小虎主产品摄影图/芝士焗.png` | 黄色品牌场景、焗烤焦斑、芝士拉丝与 IP 互动 |
| 薯条 | `皇家小虎主产品摄影图/薯条.png` | 透明背景、金黄薯条、红色纸盒与清晰边缘 |

- MAY 对产品图进行保持真实性的裁切、缩放、抠图和背景延展。
- MUST 保持原始宽高比，不得拉伸、压扁或改变产品结构。
- MUST NOT 虚构未出现的配料、夸大份量、改变成熟度、颜色或质感。
- MUST NOT 使用过度滤镜、失真液化或会造成产品误导的生成式修改。
- 产品与 IP 同画面时，产品 SHOULD 是核心信息，IP 用于引导、推荐或增强品牌情绪，不得遮挡产品关键细节。
- 需要生成新产品场景时，现有产品照片 MUST 作为图像参考，生成结果 MUST 经过产品真实性审核。

### 8.3 社交媒体与头像

- MUST 使用 `avatar-transparent` 作为默认头像资产。
- 当平台强制使用有色背景或需要稳定黄色底时，使用 `avatar-yellow-background`。
- MUST 保证皇冠、眼睛、鼻子和嘴部清晰可辨。
- MUST NOT 在头像上叠加文字或促销标签。

### 8.4 海报与宣传图

- SHOULD 使用小虎黄或白色作为主要背景。
- SHOULD 在顶部、底部或视觉中心使用完整 Logo。
- 促销信息 MAY 使用小虎红强调，但面积 MUST 小于主色区域。
- MUST 保持标题、产品图、价格或行动信息之间的清晰层级。

### 8.5 网页与数字界面

- 页眉 SHOULD 使用横版 Logo。
- 主按钮 MAY 使用小虎咖底配白字，或小虎黄底配小虎咖字。
- 小虎红 SHOULD 仅用于警示、促销或高优先级强调。
- 内容卡片 SHOULD 使用白色或浅色背景，以保证内容可读性。

### 8.6 演示文稿

- 封面 SHOULD 使用竖版组合 Logo 或横版完整 Logo。
- 内容页 SHOULD 使用横版 Logo 或独立头像作为轻量品牌标识。
- 每页 SHOULD 仅有一个主要视觉焦点。

## 9. AI 执行指令

AI 在开始任务前 MUST：

1. 确认输出场景、画布尺寸和使用渠道。
2. 从资产目录中选择正确 Logo，不得生成新 Logo。
3. 涉及 IP 或产品时，从对应资产目录选择真实参考素材。
4. 使用标准品牌色和指定字体。
5. 明确哪些规则来自原始规范，哪些属于待确认默认规则。
6. 若指定字体、Logo、IP 或产品素材无法直接使用，MUST 报告限制，不得静默替换。

AI 在输出前 MUST 检查：

- [ ] Logo 是否来自指定文件
- [ ] Logo 是否保持比例、完整且未被修改
- [ ] Logo 类型是否适合当前版面
- [ ] 主色是否为准确的小虎黄 `#FFCC00`
- [ ] 主要文字是否优先使用小虎咖 `#632C16`
- [ ] 小虎红是否仅作小面积强调
- [ ] 中文字体和英文字体是否符合映射
- [ ] IP 是否保持标准结构、比例、颜色和角色气质
- [ ] 动作素材是否与当前表达场景匹配
- [ ] 产品是否引用真实素材并保持产品事实
- [ ] 产品图是否避免拉伸、虚构配料或误导性修改
- [ ] 文字是否清晰可读
- [ ] 是否避免了禁止视觉方向
- [ ] 是否说明了任何无法满足的规则或资产限制

## 10. Machine-Readable Tokens

```yaml
brand:
  id: HJXH
  name_zh: 皇家小虎
  tagline_zh: 全球美食私厨

colors:
  brand_yellow:
    hex: "#FFCC00"
    rgb: [255, 204, 0]
    cmyk: [0, 30, 100, 0]
    pantone: "7549 C"
  brand_brown:
    hex: "#632C16"
    rgb: [99, 44, 22]
    cmyk: [55, 85, 100, 40]
    pantone: "4695 C"
  brand_red:
    hex: "#D93924"
    rgb: [217, 57, 36]
    cmyk: [0, 100, 100, 0]
    pantone: "2347 C"
  white:
    hex: "#FFFFFF"

logo_assets:
  horizontal_with_tagline: "logo-png/皇家小虎logo组合-主0.png"
  vertical_with_tagline: "logo-png/皇家小虎logo组合-主1.png"
  yellow_panel_no_tagline: "logo-png/皇家小虎logo组合-0316-RGB_画板 1 副本 22.png"
  yellow_panel_with_tagline: "logo-png/皇家小虎logo组合-0316-RGB_画板 1 副本 23.png"
  avatar_yellow_background: "logo-png/皇家小虎logo组合-0316-RGB_画板 1 副本 25.png"
  avatar_transparent: "logo-png/皇家小虎logo组合-0316-RGB_画板 1 副本 26.png"

ip_assets:
  specification: "皇家小虎IP规范/皇家小虎IP介绍.png"
  actions:
    clap: "皇家小虎IP规范/动作 (1).png"
    thumbs_up: "皇家小虎IP规范/动作 (2).png"
    confident: "皇家小虎IP规范/动作 (3).png"
    wave: "皇家小虎IP规范/动作 (4).png"
    run: "皇家小虎IP规范/动作 (5).png"

product_assets:
  pizza: "皇家小虎主产品摄影图/披萨.png"
  sausage: "皇家小虎主产品摄影图/烤肠.png"
  egg_tart: "皇家小虎主产品摄影图/蛋挞.png"
  cheese_bake: "皇家小虎主产品摄影图/芝士焗.png"
  fries: "皇家小虎主产品摄影图/薯条.png"

fonts:
  zh:
    heading_primary: "皇家小虎品牌标准字体/44华康圆体W9.TTF"
    heading_secondary: "皇家小虎品牌标准字体/43华康圆体W8.TTF"
    body_emphasis: "皇家小虎品牌标准字体/42华康圆体W7.TTF"
    body: "皇家小虎品牌标准字体/41华康圆体W5.TTF"
    auxiliary: "皇家小虎品牌标准字体/40华康圆体W3.TTF"
    display_heavy: "皇家小虎品牌标准字体/45华康圆体W12.TTF"
  en:
    heading_primary: "皇家小虎品牌标准字体/GOTHAMRND-BOLD.OTF"
    heading_secondary: "皇家小虎品牌标准字体/GOTHAMRND-MEDIUM.OTF"
    body: "皇家小虎品牌标准字体/GOTHAMRND-BOOK.OTF"
    auxiliary: "皇家小虎品牌标准字体/GOTHAMRND-LIGHT.OTF"

hard_constraints:
  - use_existing_logo_assets_only
  - preserve_logo_aspect_ratio
  - do_not_modify_logo
  - use_exact_brand_colors
  - use_mapped_brand_fonts
  - preserve_ip_identity_and_proportions
  - use_existing_ip_actions_before_generating_new_actions
  - preserve_product_truthfulness
  - do_not_fabricate_product_ingredients_or_structure
  - report_unavailable_assets_before_substitution
```
