# OpenCLI - Agent-Ready 认证

**OpenCLI** 已经正式通过了 **Agent-Ready** 认证！

OpenCLI 将网站、浏览器会话、Electron 应用和本地工具转化为确定性的 CLI 接口，使其成为 AI Agent 与更广泛软件生态系统之间的理想桥梁。

## 认证亮点

- **账号安全操作**：复用 Chrome/Chromium 登录状态，凭证从不离开浏览器
- **确定性输出**：相同命令每次都产生相同的输出结构，适合管道处理、脚本化和 CI 环境
- **零 LLM 运行时成本**：执行时不消耗 token，运行 10000 次也不付费
- **87+ 预构建适配器**：覆盖 Bilibili、知乎、小红书、Reddit、Twitter/X、HackerNews 等平台
- **浏览器直控**：`opencli browser` 让 AI Agent 直接控制浏览器 —— 导航、点击、输入、提取、截图
- **CLI Hub 集成**：统一发现、自动安装、透传外部 CLI 工具（gh、docker、obsidian 等）
- **桌面应用控制**：通过 CDP 驱动 Electron 应用（Cursor、Codex、ChatGPT、Notion 等）

## 为什么它是 Agent-Ready 的？

OpenCLI 成功满足了 Agent-Ready 认证的所有核心标准：

- **原子化动作开放**：核心功能通过 CLI 命令全面暴露 —— 浏览器自动化、适配器生成、API 探索 —— 无需 UI 交互
- **结构化反馈**：所有命令输出遵循一致的可解析结构；执行结果以结构化数据输出到 stdout，Agent 可直接消费
- **安全护栏**：浏览器凭证始终保留在浏览器上下文中；无凭证提取或存储；敏感操作需人工在环确认
- **经过验证的集成**：在 Claude Code、Cursor、Codex、OpenCode 等主流 AI Agent 平台上经过广泛测试

## 核心 CLI 能力

| 能力 | 功能 |
|------|------|
| `opencli browser` | 浏览器直控 —— 导航、点击、输入、提取、截图 |
| `opencli explore` | API 发现和认证策略探索 |
| `opencli generate` | 从真实浏览器行为生成适配器 |
| `opencli list` | 发现可用适配器和 CLI 工具 |
| 外部 CLI 透传 | gh、docker、obsidian 等工具的统一接口 |

## 成本效率

| 指标 | 传统方式 | OpenCLI | 提升 |
|------|----------|---------|------|
| 运行时 LLM 成本 | 每次动作消耗 token | **零** | **∞**（成本消除）|
| 浏览器自动化 | 复杂的 MCP 设置 | 内置支持 | **原生** |
| 适配器覆盖 | 手动集成 | 87+ 适配器 | **开箱即用** |

---

- [OpenCLI GitHub 仓库](https://github.com/jackwener/OpenCLI)
- [查看 OpenCLI 完整文档](../../awesome-skills/introductions/zh/opencli.md)
