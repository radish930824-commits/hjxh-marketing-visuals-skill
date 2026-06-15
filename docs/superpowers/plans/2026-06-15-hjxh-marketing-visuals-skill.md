# HJXH Marketing Visuals Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, globally install, and publicly release the `hjxh-marketing-visuals` Codex Skill with the approved 皇家小虎 brand assets.

**Architecture:** Keep repository-level licensing and release files at the project root, while placing the installable Skill under `skill/hjxh-marketing-visuals/`. Keep `SKILL.md` concise and route detailed creation, audit, channel-size, and brand-rule guidance through focused reference files. Package all 26 approved Logo, IP, product, and font files, and validate their exact relative paths with a deterministic manifest script.

**Tech Stack:** Markdown, YAML, Python 3, Codex Skill Creator scripts, PowerShell, Git, GitHub.

---

## File Structure

Create the following release structure in the current workspace:

```text
LICENSE
ASSET-LICENSE.md
skill/
└── hjxh-marketing-visuals/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── brand-guidelines.md
    │   ├── creation-workflow.md
    │   ├── review-workflow.md
    │   ├── channel-sizes.md
    │   └── audit-report-template.md
    ├── scripts/
    │   └── validate_assets.py
    └── assets/
        ├── manifest.json
        ├── logos/
        ├── ip/
        ├── products/
        └── fonts/
```

File responsibilities:

- `LICENSE`: MIT license applying only to Skill instructions, workflows, and scripts.
- `ASSET-LICENSE.md`: separate terms for Logo, IP, product images, and fonts.
- `skill/hjxh-marketing-visuals/SKILL.md`: trigger description, task routing, hard constraints, approval gates, and reference-loading instructions.
- `agents/openai.yaml`: UI display name, description, and default prompt.
- `references/brand-guidelines.md`: approved brand rules and exact packaged asset aliases.
- `references/creation-workflow.md`: brief collection, direction selection, Canva/ImageGen routing, production, and final audit.
- `references/review-workflow.md`: structured review, MUST-rule failure logic, risk classification, and modification gates.
- `references/channel-sizes.md`: recommended marketing-image dimensions and confirmation behavior.
- `references/audit-report-template.md`: required Chinese audit-report format.
- `assets/manifest.json`: exact inventory, aliases, categories, source paths, and packaged paths for all 26 assets.
- `scripts/validate_assets.py`: deterministic checks for manifest completeness, file existence, duplicate aliases, and allowed extensions.

### Task 1: Establish Repository And Tooling Preconditions

**Files:**
- Verify: `E:\Desktop\Codex\HJXH Design.md`
- Create later: `.git/`

- [ ] **Step 1: Confirm the bundled Python runtime works**

Run:

```powershell
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' --version
```

Expected: a successful `Python 3.x.x` response.

- [ ] **Step 2: Recheck Git and GitHub CLI availability**

Run:

```powershell
Get-Command git,gh -ErrorAction SilentlyContinue | Select-Object Name,Source
```

Expected: both commands resolve. If either command is absent, stop only the Git/GitHub publication steps and use an approved installation or available GitHub connector workflow before continuing those steps.

- [ ] **Step 3: Initialize the local repository when Git is available**

Run:

```powershell
git init
git branch -M main
git status --short --branch
```

Expected: branch is `main`, with existing workspace files shown as untracked.

- [ ] **Step 4: Create a release-focused ignore file**

Create `.gitignore` with:

```gitignore
.DS_Store
Thumbs.db
*.tmp
*.log
__pycache__/
```

- [ ] **Step 5: Commit the approved design and implementation plan**

Run:

```powershell
git add .gitignore docs/superpowers/specs/2026-06-15-hjxh-marketing-visuals-skill-design.md docs/superpowers/plans/2026-06-15-hjxh-marketing-visuals-skill.md
git commit -m "docs: define HJXH marketing visuals skill"
```

Expected: one documentation commit.

### Task 2: Initialize The Installable Skill

**Files:**
- Create: `skill/hjxh-marketing-visuals/SKILL.md`
- Create: `skill/hjxh-marketing-visuals/agents/openai.yaml`
- Create: `skill/hjxh-marketing-visuals/references/`
- Create: `skill/hjxh-marketing-visuals/scripts/`
- Create: `skill/hjxh-marketing-visuals/assets/`

- [ ] **Step 1: Initialize the Skill using the official Skill Creator script**

Run:

```powershell
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Users\47289\.codex\skills\.system\skill-creator\scripts\init_skill.py' `
  hjxh-marketing-visuals `
  --path 'E:\Desktop\Codex\HJXH Design.md\skill' `
  --resources scripts,references,assets `
  --interface 'display_name=皇家小虎营销视觉' `
  --interface 'short_description=制作与审核皇家小虎营销视觉' `
  --interface 'default_prompt=为皇家小虎制作或审核营销图片，并严格执行品牌视觉规范。'
```

Expected: the Skill directory and required metadata files are created.

- [ ] **Step 2: Remove generated placeholder resource files**

Delete only placeholder files created by `init_skill.py`; preserve the required directories and generated `agents/openai.yaml`.

- [ ] **Step 3: Verify the initialized skeleton**

Run:

```powershell
Get-ChildItem -Recurse -LiteralPath 'skill\hjxh-marketing-visuals' | Select-Object FullName
```

Expected: `SKILL.md`, `agents/openai.yaml`, and the three resource directories exist.

- [ ] **Step 4: Commit the initialized Skill skeleton**

Run:

```powershell
git add skill/hjxh-marketing-visuals
git commit -m "chore: initialize HJXH marketing visuals skill"
```

Expected: one Skill initialization commit.

### Task 3: Package Assets And Add Deterministic Validation

**Files:**
- Create: `skill/hjxh-marketing-visuals/assets/manifest.json`
- Create: `skill/hjxh-marketing-visuals/scripts/validate_assets.py`
- Copy: `logo-png/*` to `skill/hjxh-marketing-visuals/assets/logos/`
- Copy: `皇家小虎IP规范/*` to `skill/hjxh-marketing-visuals/assets/ip/`
- Copy: `皇家小虎主产品摄影图/*` to `skill/hjxh-marketing-visuals/assets/products/`
- Copy: `皇家小虎品牌标准字体/*` to `skill/hjxh-marketing-visuals/assets/fonts/`

- [ ] **Step 1: Write the failing asset-manifest validator**

Create `scripts/validate_assets.py` with checks that:

```python
EXPECTED_COUNTS = {
    "logo": 6,
    "ip": 6,
    "product": 4,
    "font": 10,
}
ALLOWED_EXTENSIONS = {
    "logo": {".png"},
    "ip": {".png"},
    "product": {".png", ".jpg", ".jpeg"},
    "font": {".ttf", ".otf"},
}
```

The script must load `assets/manifest.json`, fail for missing files, duplicate aliases, invalid categories, invalid extensions, absolute packaged paths, or category-count mismatches, and print `Validated 26 HJXH assets.` on success.

- [ ] **Step 2: Run the validator to verify it fails before the manifest exists**

Run:

```powershell
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'skill\hjxh-marketing-visuals\scripts\validate_assets.py'
```

Expected: FAIL because `assets/manifest.json` does not exist.

- [ ] **Step 3: Copy all approved assets without renaming source filenames**

Copy the four source directories into their matching packaged directories. Preserve file contents and filenames exactly.

- [ ] **Step 4: Create the complete asset manifest**

For each asset, record:

```json
{
  "alias": "logo-horizontal-with-tagline",
  "category": "logo",
  "source": "logo-png/皇家小虎logo组合-主0.png",
  "path": "assets/logos/皇家小虎logo组合-主0.png",
  "purpose": "横向空间、页面页眉、网站导航、横版物料"
}
```

Use the aliases already defined in `HJXH Design.md`; add stable aliases for each font by weight and language. The manifest must contain exactly 26 entries.

- [ ] **Step 5: Run asset validation**

Run:

```powershell
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'skill\hjxh-marketing-visuals\scripts\validate_assets.py'
```

Expected: `Validated 26 HJXH assets.`

- [ ] **Step 6: Compare packaged files against source files**

Run:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath (Get-ChildItem -Recurse -File 'logo-png','皇家小虎IP规范','皇家小虎主产品摄影图','皇家小虎品牌标准字体').FullName
Get-FileHash -Algorithm SHA256 -LiteralPath (Get-ChildItem -Recurse -File 'skill\hjxh-marketing-visuals\assets\logos','skill\hjxh-marketing-visuals\assets\ip','skill\hjxh-marketing-visuals\assets\products','skill\hjxh-marketing-visuals\assets\fonts').FullName
```

Expected: each source asset hash appears once in the packaged asset hashes.

- [ ] **Step 7: Commit packaged assets and validator**

Run:

```powershell
git add skill/hjxh-marketing-visuals/assets skill/hjxh-marketing-visuals/scripts/validate_assets.py
git commit -m "feat: package approved HJXH brand assets"
```

Expected: one asset packaging commit.

### Task 4: Write Brand And Channel References

**Files:**
- Create: `skill/hjxh-marketing-visuals/references/brand-guidelines.md`
- Create: `skill/hjxh-marketing-visuals/references/channel-sizes.md`

- [ ] **Step 1: Write the brand-guidelines reference**

Include:

- exact brand name, tagline, colors, typography mappings, and asset aliases;
- Logo selection and integrity rules;
- IP structure, color, proportion, and approved-action rules;
- product-authenticity rules;
- recommended and prohibited visual directions;
- distinction between confirmed rules and `待确认` defaults;
- hard rule that missing Logo assets stop production.

Keep the detailed rules in this reference rather than duplicating them in `SKILL.md`.

- [ ] **Step 2: Write channel-size guidance**

Define recommended dimensions and confirmation behavior for:

- WeChat and Moments;
- Xiaohongshu;
- ecommerce main images and promotional banners;
- general square, portrait, and landscape social graphics.

State that user-specified dimensions always take priority, and missing dimensions require recommending one to three options for confirmation.

- [ ] **Step 3: Verify every packaged asset alias is discoverable**

Run:

```powershell
Select-String -Path 'skill\hjxh-marketing-visuals\references\brand-guidelines.md' -Pattern 'logo-horizontal-with-tagline|ip-action-thumbs-up|product-pizza|heading-primary'
```

Expected: all representative aliases are present.

- [ ] **Step 4: Commit brand and channel references**

Run:

```powershell
git add skill/hjxh-marketing-visuals/references/brand-guidelines.md skill/hjxh-marketing-visuals/references/channel-sizes.md
git commit -m "docs: add HJXH brand and channel guidance"
```

Expected: one reference documentation commit.

### Task 5: Write Creation And Audit Workflows

**Files:**
- Create: `skill/hjxh-marketing-visuals/references/creation-workflow.md`
- Create: `skill/hjxh-marketing-visuals/references/review-workflow.md`
- Create: `skill/hjxh-marketing-visuals/references/audit-report-template.md`

- [ ] **Step 1: Write the creation workflow**

Define the exact sequence:

1. classify task;
2. gather or infer brief;
3. recommend channel sizes when absent;
4. preserve copy or propose a confirmed shortened version;
5. select approved assets;
6. determine whether the task is routine, important, ambiguous, or high-risk;
7. route to Canva, ImageGen, or both;
8. produce the requested deliverable;
9. run the audit workflow before delivery.

State that routine requests may proceed directly, while important campaigns, multi-direction work, and high-risk changes require confirmation.

- [ ] **Step 2: Write the review workflow**

Define audit categories, evidence requirements, risk levels, and correction gates. State explicitly:

- every `MUST` or `MUST NOT` violation makes the result fail;
- Logo, brand colors, fonts, IP identity/new actions, product facts, and promotional prices require approval before modification;
- low-risk spacing and layout corrections may be applied automatically when requested.

- [ ] **Step 3: Write the audit-report template**

Use this required Chinese structure:

```markdown
# 皇家小虎视觉审核报告

结论：通过 / 不通过
风险等级：低 / 中 / 高

## MUST 违规
- 无 / [违规项、证据、影响]

## 分类审核
| 分类 | 状态 | 发现 | 建议 |
|---|---|---|---|
| Logo | 通过/不通过 | ... | ... |
| 颜色 | 通过/不通过 | ... | ... |
| 字体 | 通过/不通过 | ... | ... |
| IP | 通过/不通过 | ... | ... |
| 产品真实性 | 通过/不通过 | ... | ... |
| 信息层级与可读性 | 通过/不通过 | ... | ... |

## 需确认的高风险修改
- 无 / [修改项]
```

- [ ] **Step 4: Check workflow requirements for contradictions**

Run:

```powershell
Select-String -Path 'skill\hjxh-marketing-visuals\references\*.md' -Pattern 'MUST|高风险|Canva|ImageGen|待审核草案'
```

Expected: creation, audit, tool routing, and high-risk gates are all represented.

- [ ] **Step 5: Commit workflow references**

Run:

```powershell
git add skill/hjxh-marketing-visuals/references/creation-workflow.md skill/hjxh-marketing-visuals/references/review-workflow.md skill/hjxh-marketing-visuals/references/audit-report-template.md
git commit -m "docs: add HJXH creation and audit workflows"
```

Expected: one workflow documentation commit.

### Task 6: Implement The Core Skill And UI Metadata

**Files:**
- Modify: `skill/hjxh-marketing-visuals/SKILL.md`
- Regenerate: `skill/hjxh-marketing-visuals/agents/openai.yaml`

- [ ] **Step 1: Replace the generated SKILL.md template**

Use this frontmatter:

```yaml
---
name: hjxh-marketing-visuals
description: Create, plan, audit, and safely revise 皇家小虎 or HJXH marketing visuals, including posters, social-media graphics, ecommerce promotional images, and campaign graphics. Use when a request mentions 皇家小虎 or HJXH and asks for marketing-image creation, promotional visual planning, brand-compliance review, or correction of an existing marketing visual.
---
```

The body must:

- default to Chinese and allow requested English;
- classify the four supported task types;
- load only the references required for the current task;
- require `brand-guidelines.md` for every task;
- require `creation-workflow.md` for creation or plan tasks;
- require `review-workflow.md` and `audit-report-template.md` for audit or modification tasks;
- load `channel-sizes.md` only when dimensions or channels need recommendation;
- identify Canva/ImageGen routing;
- enforce high-risk approval gates;
- require a final audit for every produced image;
- prohibit Logo recreation and silent asset substitution.

- [ ] **Step 2: Regenerate UI metadata**

Run:

```powershell
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Users\47289\.codex\skills\.system\skill-creator\scripts\generate_openai_yaml.py' `
  'skill\hjxh-marketing-visuals' `
  --interface 'display_name=皇家小虎营销视觉' `
  --interface 'short_description=制作与审核皇家小虎营销视觉' `
  --interface 'default_prompt=为皇家小虎制作或审核营销图片，并严格执行品牌视觉规范。'
```

Expected: `agents/openai.yaml` matches the completed Skill.

- [ ] **Step 3: Run official Skill validation**

Run:

```powershell
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Users\47289\.codex\skills\.system\skill-creator\scripts\quick_validate.py' `
  'skill\hjxh-marketing-visuals'
```

Expected: validation succeeds.

- [ ] **Step 4: Check for template placeholders and forbidden auxiliary files**

Run:

```powershell
Select-String -Path 'skill\hjxh-marketing-visuals\**\*' -Pattern 'TODO|TBD|placeholder' -CaseSensitive:$false
Get-ChildItem -Recurse -File 'skill\hjxh-marketing-visuals' | Where-Object Name -In 'README.md','CHANGELOG.md','INSTALLATION_GUIDE.md'
```

Expected: no template placeholders and no forbidden auxiliary documents.

- [ ] **Step 5: Commit the completed Skill**

Run:

```powershell
git add skill/hjxh-marketing-visuals/SKILL.md skill/hjxh-marketing-visuals/agents/openai.yaml
git commit -m "feat: implement HJXH marketing visuals skill"
```

Expected: one core Skill commit.

### Task 7: Add Repository Licensing

**Files:**
- Create: `LICENSE`
- Create: `ASSET-LICENSE.md`

- [ ] **Step 1: Add the standard MIT license**

Create `LICENSE` using the standard MIT text and the current copyright holder and year.

- [ ] **Step 2: Add the separate brand-asset license**

State clearly that:

- 皇家小虎 retains ownership of Logo, IP, product images, and fonts;
- the files may be used by the Skill and for authorized 皇家小虎 design production;
- impersonation, unauthorized resale, sublicensing, and use outside the stated permission are prohibited;
- the user has confirmed that the packaged fonts may be publicly distributed;
- the MIT license does not apply to files under `skill/hjxh-marketing-visuals/assets/`.

- [ ] **Step 3: Check the license boundary**

Run:

```powershell
Select-String -Path 'LICENSE','ASSET-LICENSE.md' -Pattern 'MIT|assets|fonts|皇家小虎|resale'
```

Expected: the code-versus-asset boundary and public font-distribution statement are explicit.

- [ ] **Step 4: Commit licensing files**

Run:

```powershell
git add LICENSE ASSET-LICENSE.md
git commit -m "docs: add code and brand asset licenses"
```

Expected: one licensing commit.

### Task 8: Validate Behavior With Representative Scenarios

**Files:**
- Verify: `skill/hjxh-marketing-visuals/`

- [ ] **Step 1: Re-run structural and asset validation**

Run:

```powershell
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'C:\Users\47289\.codex\skills\.system\skill-creator\scripts\quick_validate.py' 'skill\hjxh-marketing-visuals'
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'skill\hjxh-marketing-visuals\scripts\validate_assets.py'
```

Expected: Skill validation succeeds and asset validation prints `Validated 26 HJXH assets.`

- [ ] **Step 2: Forward-test routine creation**

Use a fresh agent with:

```text
Use $hjxh-marketing-visuals at E:\Desktop\Codex\HJXH Design.md\skill\hjxh-marketing-visuals to plan a routine 皇家小虎披萨朋友圈宣传图. The user supplied the title "今晚吃披萨" but no size.
```

Expected: recommends suitable size options, auto-selects approved assets, preserves copy, routes tools, and includes a final audit requirement.

- [ ] **Step 3: Forward-test plan-only output**

Use a fresh agent with:

```text
Use $hjxh-marketing-visuals at E:\Desktop\Codex\HJXH Design.md\skill\hjxh-marketing-visuals to provide a plan only for a 皇家小虎蛋挞促销海报. Do not generate an image.
```

Expected: returns layout, assets, copy hierarchy, dimensions, tool recommendation, and production prompts without generating an image.

- [ ] **Step 4: Forward-test audit failure**

Use a fresh agent with:

```text
Use $hjxh-marketing-visuals at E:\Desktop\Codex\HJXH Design.md\skill\hjxh-marketing-visuals to audit a hypothetical visual where the Logo is stretched and the red brand color fills the entire background.
```

Expected: result is `不通过`, with the stretched Logo listed as a MUST violation and the red background identified as a violation unless explicitly approved.

- [ ] **Step 5: Forward-test high-risk modification gate**

Use a fresh agent with:

```text
Use $hjxh-marketing-visuals at E:\Desktop\Codex\HJXH Design.md\skill\hjxh-marketing-visuals to revise a 皇家小虎 product visual by changing the promotional price and adding a new IP action.
```

Expected: asks for confirmation before changing price or creating a new IP action and labels any approved new action as `待审核草案`.

- [ ] **Step 6: Fix any behavior gaps and rerun affected tests**

Update only the relevant Skill or reference file. Re-run official validation, asset validation, and the failed forward-test until the expected behavior is met.

- [ ] **Step 7: Commit validation-driven refinements**

Run:

```powershell
git add skill/hjxh-marketing-visuals
git commit -m "test: refine HJXH skill from scenario validation"
```

Expected: a commit exists only if validation required changes.

### Task 9: Install The Validated Skill Globally

**Files:**
- Copy to: `C:\Users\47289\.codex\skills\hjxh-marketing-visuals\`

- [ ] **Step 1: Confirm the global destination does not contain an unrelated Skill**

Run:

```powershell
Get-ChildItem -Force -LiteralPath 'C:\Users\47289\.codex\skills\hjxh-marketing-visuals' -ErrorAction SilentlyContinue
```

Expected: destination is absent, or contains only an older confirmed version of this same Skill.

- [ ] **Step 2: Copy the validated Skill to the global directory**

Copy `skill/hjxh-marketing-visuals/` to `C:\Users\47289\.codex\skills\hjxh-marketing-visuals/`. This write is outside the current workspace and requires approval.

- [ ] **Step 3: Validate the installed copy**

Run:

```powershell
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Users\47289\.codex\skills\.system\skill-creator\scripts\quick_validate.py' `
  'C:\Users\47289\.codex\skills\hjxh-marketing-visuals'
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Users\47289\.codex\skills\hjxh-marketing-visuals\scripts\validate_assets.py'
```

Expected: installed Skill validation succeeds and all 26 assets validate.

### Task 10: Publish The Public GitHub Repository And v1.0.0

**Files:**
- Publish repository: `hjxh-marketing-visuals-skill`

- [ ] **Step 1: Verify GitHub authentication and account ownership**

Use the GitHub connector first. If needed, run:

```powershell
gh auth status
```

Expected: authenticated GitHub account is identified and authorized to create a public repository.

- [ ] **Step 2: Create the public repository**

Create `hjxh-marketing-visuals-skill` as a public repository under the authenticated user account. Do not auto-create a remote README, license, or `.gitignore`, because local versions already define the release.

- [ ] **Step 3: Confirm the final publication scope**

Run:

```powershell
git status --short
git ls-files
```

Expected: tracked files include the release Skill, approved assets, licenses, design/spec documents, and no temporary files.

- [ ] **Step 4: Add the remote and push `main`**

Run:

```powershell
git remote add origin https://github.com/<authenticated-user>/hjxh-marketing-visuals-skill.git
git push -u origin main
```

Expected: `main` is pushed successfully.

- [ ] **Step 5: Create and push the first release tag**

Run:

```powershell
git tag -a v1.0.0 -m "Release hjxh-marketing-visuals v1.0.0"
git push origin v1.0.0
```

Expected: tag `v1.0.0` is visible on GitHub.

- [ ] **Step 6: Verify public repository contents**

Use the GitHub connector to verify:

- repository visibility is public;
- `skill/hjxh-marketing-visuals/SKILL.md` is present;
- all 26 assets are present;
- `LICENSE` and `ASSET-LICENSE.md` are present;
- tag `v1.0.0` exists.

- [ ] **Step 7: Report the install path**

Provide the public repository URL and the installable Skill subpath:

```text
skill/hjxh-marketing-visuals
```

## Final Verification

Run:

```powershell
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'C:\Users\47289\.codex\skills\.system\skill-creator\scripts\quick_validate.py' 'skill\hjxh-marketing-visuals'
& 'C:\Users\47289\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'skill\hjxh-marketing-visuals\scripts\validate_assets.py'
git status --short --branch
git log --oneline --decorate -5
git tag --list
```

Expected:

- Skill validation succeeds;
- `Validated 26 HJXH assets.` is printed;
- working tree is clean;
- recent commits cover design, initialization, assets, references, workflows, core Skill, licenses, and validation;
- `v1.0.0` exists.
