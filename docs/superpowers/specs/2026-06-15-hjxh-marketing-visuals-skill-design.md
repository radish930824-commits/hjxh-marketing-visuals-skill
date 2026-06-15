# HJXH Marketing Visuals Skill Design

## 1. Objective

Create a reusable Codex Skill named `hjxh-marketing-visuals` for producing and auditing 皇家小虎 marketing visuals. The Skill must apply the existing `HJXH Design.md` brand rules, automatically select approved assets where appropriate, and protect high-risk brand and commercial information.

The initial release focuses on marketing images, including posters, social-media graphics, ecommerce promotional images, and campaign graphics.

## 2. Triggering And Language

- Folder and Skill name: `hjxh-marketing-visuals`
- Display name: `皇家小虎营销视觉`
- Default language: Chinese; switch to English when requested.
- Trigger automatically when a request mentions 皇家小虎 or HJXH and involves marketing-image creation, promotional visual planning, or visual compliance review.
- Do not trigger for unrelated brand discussion.

## 3. Supported Tasks

The Skill supports four task types:

1. Produce a finished marketing image.
2. Produce a detailed visual-production plan without generating an image.
3. Audit an existing marketing image.
4. Audit and modify an existing marketing image.

It supports both direct production and design-tool-ready plans.

## 4. Interaction Model

### 4.1 Required Brief

Determine or request:

- use channel;
- canvas size;
- target audience;
- marketing objective;
- required copy;
- featured product;
- required Logo, IP action, or product asset;
- allowed processing, such as cropping, cutout, background extension, or new-scene generation.

When a channel or size is missing, recommend one to three suitable sizes and obtain confirmation.

### 4.2 Copy Handling

- Preserve user-provided copy by default.
- When copy is too long, unclear, or unsuitable for the layout, propose a shortened version.
- Do not change prices, offers, product claims, or other commercial facts without confirmation.

### 4.3 Visual Directions

- For straightforward daily requests, produce one recommended direction directly.
- For important campaigns or unclear requests, present two or three differentiated directions before production.
- Important campaigns, multi-direction tasks, and high-risk changes require approval before production.

## 5. Asset Selection And Tool Routing

### 5.1 Asset Selection

Use a mixed selection model:

- Automatically choose the appropriate approved Logo, IP action, and product image for routine requests.
- Ask for confirmation when assets are ambiguous, a new IP action is required, or product authenticity may be affected.
- Stop when an approved Logo asset is unavailable.
- When product or standard IP assets are unavailable, report the limitation and, after confirmation, use a placeholder or create a clearly labeled `待审核草案`.

### 5.2 Tool Routing

- Use Canva when accurate text layout, editable design, and direct use of approved brand assets are primary requirements.
- Use ImageGen when creative backgrounds or new scenes are required.
- Combine Canva and ImageGen when generated scenes and precise brand layout are both required.
- Never use ImageGen to recreate or imitate the Logo.

## 6. Risk Model

The following are high-risk and always require approval before modification:

- Logo;
- standard brand colors;
- brand fonts;
- standard IP identity or structure;
- new IP actions or viewpoints;
- product facts, ingredients, structure, amount, maturity, color, or texture;
- promotional prices and offer terms.

Low-risk layout and spacing corrections may be applied automatically when requested.

## 7. Audit Model

Audit existing and newly produced images using these categories:

- Logo;
- colors;
- typography;
- IP;
- product authenticity;
- information hierarchy and readability.

Audit results must include:

- pass or fail result;
- MUST-rule violations;
- risk level;
- category-level observations;
- recommended corrections;
- identification of changes that require approval.

Any violation of a `MUST` or `MUST NOT` rule causes the audit to fail. Non-mandatory items may receive improvement recommendations but do not independently cause failure.

## 8. Deliverables

- Canva production: editable Canva design plus exported image.
- ImageGen production: generated image, production notes, and audit result.
- Plan-only task: layout, asset selection, copy hierarchy, dimensions, tool recommendation, and generation or production prompts.
- Audit task: structured audit report; apply only approved high-risk corrections.

## 9. Skill Architecture

Use a compact core Skill with progressively loaded references:

```text
hjxh-marketing-visuals/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── brand-guidelines.md
│   ├── creation-workflow.md
│   ├── review-workflow.md
│   ├── channel-sizes.md
│   └── audit-report-template.md
└── assets/
    ├── logos/
    ├── ip/
    ├── products/
    └── fonts/
```

Responsibilities:

- `SKILL.md`: triggering behavior, task classification, core decision flow, hard constraints, and reference routing.
- `brand-guidelines.md`: detailed rules derived from `HJXH Design.md`.
- `creation-workflow.md`: briefing, direction selection, tool routing, production, and final checks.
- `review-workflow.md`: audit procedure, risk classification, correction rules, and approval gates.
- `channel-sizes.md`: recommended channel and canvas dimensions.
- `audit-report-template.md`: consistent structured audit output.
- `assets/`: approved Logo, IP, product, and font files.

Do not include a README inside the installable Skill folder.

## 10. Source Assets And Versioning

- Develop and validate the Skill in the current project first.
- Package Logo, IP, product, and font assets into the Skill.
- Brand asset and rule updates require explicit owner confirmation.
- Preserve old versions and publish validated updates as new versions.
- Install the validated Skill into the global Codex Skill directory.

## 11. Public GitHub Repository

Create a public repository named `hjxh-marketing-visuals-skill`.

Repository contents:

- installable Skill;
- all approved Logo, IP, product, and font assets;
- repository-level licensing files;
- no unrelated project or temporary files.

Licensing:

- Use MIT License for Skill instructions, workflows, and scripts.
- Use a separate `ASSET-LICENSE.md` for Logo, IP, product images, and fonts.
- Preserve 皇家小虎 ownership of brand assets and prohibit impersonation, unauthorized resale, and uses outside the stated asset license.
- Font files are approved by the user for public distribution.

Release the first validated version as `v1.0.0`.

## 12. Validation And Acceptance

Before release:

1. Validate Skill structure, naming, frontmatter, trigger description, and reference paths.
2. Validate that every packaged asset path resolves.
3. Confirm font files are included and readable.
4. Test four representative workflows:
   - routine marketing-image production;
   - plan-only output;
   - existing-image audit;
   - audit with a high-risk requested modification.
5. Confirm automatic asset selection works for routine requests.
6. Confirm ambiguous or high-risk situations request approval.
7. Confirm Logo absence stops production.
8. Confirm every MUST-rule violation causes audit failure.
9. Confirm final outputs include the required deliverables and audit result.
10. Install the validated Skill globally.
11. Create the public GitHub repository, publish the files, and tag `v1.0.0`.

## 13. Known Preconditions

- Git is currently unavailable from the workspace shell and must be installed or made available before commit, repository creation, push, and release tagging.
- GitHub authentication and repository ownership must be verified before publication.
