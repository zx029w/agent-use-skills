# Academic Research Skills

**Academic Research Skills (ARS)** 是一套面向学术研究全流程的 AI 协作工具集，覆盖从深度研究、论文撰写、同行评审到修订定稿的完整研究管线。由 40+ 个专业智能体协同工作，以"人在回路"为核心理念，帮助研究者专注于真正需要思考的部分。

## 标签

🗂️ 文档与办公 | 🔍 待验证

## 核心理念

- **AI 是副驾驶，不是驾驶员**：ARS 不代写论文，而是承担文献检索、引用格式化、数据验证、逻辑一致性检查等苦力活，让研究者专注于问题定义、方法选择、数据解读和核心论证。
- **人在回路，拒绝全自动**：基于 Lu et al. (2026, *Nature*) 对全自主 AI 研究系统失败模式的分析，ARS 在多个阶段设置完整性检查门，确保每一步都经人类确认。10 阶段流水线中每个阶段都需要用户确认检查点，完整性验证（Stage 2.5 + 4.5）不可跳过。
- **反谄媚与反框架锁定**：内置让步阈值协议（DA 对每个反驳必须先打分才能让步）、意图检测层（区分探索性 vs 目标导向对话）、对话健康监测器等机制，对抗 AI 固有的谄媚倾向和框架锁定问题。
- **引用真实性保障**：基于 Zhao et al. (2026) 对 2.5M 篇论文、111M 条引用的审计发现，ARS v3.8+ 实现了三层引用锚定、可选声明审计（`ARS_CLAIM_AUDIT=1`）、确定性引用存在性验证门（四索引交叉验证：Semantic Scholar + OpenAlex + Crossref + arXiv）。

## 主要功能与工作流

1. **深度研究（Deep Research）**：13 个智能体组成的研究团队，支持 7 种模式 — 全面研究、快速简报、系统性综述（PRISMA）、苏格拉底引导式、事实核查、文献综述、研究质量评审。支持 Semantic Scholar API 验证、可选跨模型校验。
2. **学术论文撰写（Academic Paper）**：12 个智能体的写作流水线，支持 10 种模式 — 全面写作、规划引导、大纲生成、修订、修订教练、摘要生成、文献综述论文、格式转换（APA 7.0/Chicago/MLA/IEEE/Vancouver）、引用检查、AI 声明生成。支持风格校准和写作质量检查。
3. **同行评审（Paper Reviewer）**：7 个智能体多视角评审系统，包含编辑（EIC）+ 3 位动态审稿人 + 魔鬼代言人，采用 0-100 评分体系（≥80 接收、65-79 小修、50-64 大修、<50 拒稿）。支持 6 种模式 — 全面评审、快速评估、引导式改进、方法论聚焦、复审、校准。
4. **学术流水线（Pipeline）**：10 阶段编排器，从 Stage 0 意图分类到 Stage 6 过程总结，包含自适应检查点、声明验证、Material Passport、可选跨模型完整性验证、评分轨迹追踪、协作深度观察器。完整性检查门（Stage 2.5/4.5）为硬性门控，不可跳过。

## 技能库概览

- **研究类**：Deep Research — 全面研究、快速简报、PRISMA 系统性综述、苏格拉底引导、事实核查、文献综述、研究评审
- **写作类**：Academic Paper — 全面写作、规划、大纲、修订、修订教练、摘要、文献综述论文、格式转换、引用检查、AI 声明
- **评审类**：Paper Reviewer — 全面评审、快速评估、引导改进、方法论聚焦、复审、校准
- **编排类**：Pipeline — 10 阶段端到端流水线，支持中途入场（已有论文从 Stage 2.5 开始，收到审稿意见从 Stage 4 开始）

## 支持的语言与格式

- **写作语言**：繁体中文（默认中文输入时）、英语（默认英文输入时）、双语摘要
- **引用格式**：APA 7.0（默认）、Chicago、MLA、IEEE、Vancouver
- **论文结构**：IMRaD、主题文献综述、理论分析、案例研究、政策简报、会议论文
- **输出格式**：Markdown + DOCX（通过 Pandoc）+ LaTeX（APA 7.0 `apa7` class）→ PDF

## 成本与性能

| 指标 | 数值 |
|------|------|
| 全流水线（15k 词论文） | 约 $4-6 |
| 建议设置 | Skip Permissions 模式，Agent Team 可选 |

## 安装与支持

Academic Research Skills 以 Claude Code 插件形式分发，同时提供 Codex CLI 适配版本：

- [Claude Code](../../claudecode/academic-research-skills/INSTALL-zh.md)（插件安装，推荐）
- [Codex](../../codex/academic-research-skills/INSTALL-zh.md)（技能包安装）

---
了解更多信息，请访问：[GitHub - Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)
