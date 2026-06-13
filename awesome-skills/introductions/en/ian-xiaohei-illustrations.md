# Ian Xiaohei Illustrations

**Ian Xiaohei Illustrations** is a Codex skill for generating 16:9 white-background hand-drawn editorial illustrations for Chinese articles, blog posts, Notion documents, and methodology content. It turns key judgments, workflows, structures, states, or metaphors in an article into a clean, absurd, and memorable hand-drawn explanatory image.

## Tags

🎨 Design & Creativity | 🔍 Pending Verification

## Core Philosophy

- **Visualize cognitive anchors**: Prioritize the article's core judgments, turning points, loops, contrasts, paths, and state changes instead of adding images to every paragraph.
- **Xiaohei drives the action**: The default IP "Xiaohei" must participate in the core action of the image, not sit in the corner as decoration.
- **Absurd yet clean**: White background, black hand-drawn lines, and small red/orange/blue Chinese annotations. The style is light, absurd, and recognizable — never childish, PPT-like, or commercial illustration.

## Key Features & Workflow

1. **Digest the article**: Read the article, Markdown, Notion page, screenshot, or topic to extract core ideas, turning points, and visualizable sections.
2. **Output illustration strategy (shot list)**: Plan 4-8 images for the article, each with placement, theme, structure type, Xiaohei's action, and suggested Chinese annotations.
3. **Generate one image at a time**: Call the built-in `image_gen` tool per image; each image should express only one core structure.
4. **QA check and iterate**: Check against `qa-checklist.md` for white background, breathing room, Xiaohei's action, annotations, non-PPT feel, and avoiding reuse of old compositions.
5. **Save and deliver**: Save final PNGs to `assets/<article-slug>-illustrations/`, named sequentially like `01-topic-name.png`, and report usage and paths.

## Skills Library Overview

- **Core skill**: `SKILL.md` — core positioning, workflow, output style, and delivery standards.
- **Style DNA**: `references/style-dna.md` — colors, line style, typography, and taboos.
- **IP guide**: `references/xiaohei-ip.md` — Xiaohei's look, personality, action library, and taboos.
- **Composition patterns**: `references/composition-patterns.md` — structure types, original metaphor methods, and anti-cliché rules.
- **Prompt template**: `references/prompt-template.md` — single-image generation prompt template.
- **QA checklist**: `references/qa-checklist.md` — post-generation check and iteration rules.
- **Style examples**: `assets/examples/` — for low-frequency visual calibration only; do not use as default generation references or copy compositions.

## Installation & Support

Ian Xiaohei Illustrations currently supports the following AI editor and platform:
- [Codex](../../codex/ian-xiaohei-illustrations/INSTALL-en.md)

---
For more information, visit: [GitHub - helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)
