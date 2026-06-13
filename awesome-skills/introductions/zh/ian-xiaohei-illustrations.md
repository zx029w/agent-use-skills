# Ian 小黑怪诞正文配图

**Ian 小黑怪诞正文配图**是一个为中文文章、博客、Notion 文档和方法论内容生成 16:9 白底手绘正文配图的 Codex Skill。它会把文章里的判断、流程、结构、状态或隐喻，变成一张清爽、怪诞、有记忆点的手绘解释图。

## 标签

🎨 设计与创意 | 🔍 待验证

## 核心理念

- **把认知锚点画出来**：优先选择文章中的核心判断、转折、闭环、对比、路径、状态变化等认知锚点，而不是给每个段落平均配图。
- **小黑承担核心动作**：默认 IP“小黑”必须参与画面的核心动作，而不是作为边角装饰。
- **怪诞但清爽**：纯白背景、黑色手绘线稿、少量红橙蓝中文批注，风格轻、怪、有个人识别度，但不幼稚、不 PPT、不商业插画。

## 关键能力与工作流

1. **消化正文**：读取文章、Markdown、Notion 页面、截图或主题，提炼核心观点、认知转折和适合视觉化的段落。
2. **输出配图策略（shot list）**：为文章规划 4-8 张图，写清楚每张图的位置、主题、结构类型、小黑动作和中文标注建议。
3. **单张生成**：每张图单独调用图像模型，使用内置 `image_gen` 工具；每张图只讲一个核心结构。
4. **QA 检查与迭代**：按 `qa-checklist.md` 检查白底、留白、小黑动作、中文标注、非 PPT 感、非旧案例复刻等问题。
5. **保存交付**：将最终 PNG 保存到 `assets/<article-slug>-illustrations/`，按 `01-topic-name.png` 顺序命名，并报告用途和路径。

## 技能库概览

- **核心心法**：`SKILL.md` — 核心定位、工作流、输出口径与交付规范。
- **风格 DNA**：`references/style-dna.md` — 颜色、线条、文字、禁忌。
- **IP 规范**：`references/xiaohei-ip.md` — 小黑形象、性格、动作库与禁忌。
- **构图模式**：`references/composition-patterns.md` — 结构类型、原创隐喻方法和反刻规则。
- **生图模板**：`references/prompt-template.md` — 单张生图提示词模板。
- **质检清单**：`references/qa-checklist.md` — 生成后检查和迭代规则。
- **风格样例**：`assets/examples/` — 仅作低频视觉校准，不作为默认生成参考，禁止照抄构图。

## 安装与支持

Ian 小黑怪诞正文配图目前支持以下 AI 编辑器与平台：
- [Codex](../../codex/ian-xiaohei-illustrations/INSTALL-zh.md)

---
更多信息，请访问：[GitHub - helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)
