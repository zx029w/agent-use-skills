# Obsidian - Agent-Ready 认证

**Obsidian** 已经正式通过了 **Agent-Ready** 认证！

📺 **演示视频**：[B 站观看 → Obsidian CLI × AI Agent 实战演示](https://www.bilibili.com/video/BV1ydA7zUE5A)

Obsidian 1.12（2026 年 2 月 27 日发布）正式引入了官方 CLI 命令行工具与 TUI（终端用户界面），使其成为首个面向 AI Agent 原生优化的知识库管理软件之一。

## 认证亮点

- **原生 CLI 支持**：通过 `obsidian` 命令行工具直接操作知识库，无需解析原始文件。
- **语义搜索能力**：调用 Obsidian 自身的搜索索引，支持标签、属性、反向链接等结构化查询。
- **图谱查询**：通过 `obsidian backlinks`、`obsidian orphans` 等命令查询知识图谱关系。
- **极致性能**：孤立笔记检测速度比 grep 快 **60 倍**，Token 消耗减少高达 **70,000 倍**。
- **生态集成**：Claude Code、MCP Server、REST API 等主流 Agent 平台均已支持。

## 为什么它是 Agent-Ready 的？

Obsidian 成功满足了 Agent-Ready 认证的所有核心标准：

- **原子化动作开放**：核心功能通过 CLI 命令全面暴露：`obsidian search`、`obsidian read`、`obsidian write`、`obsidian daily:prepend`、`obsidian backlinks`、`obsidian orphans` 等，无需 UI 交互。
- **结构化反馈**：搜索结果、图查询结果以结构化文本输出到 `stdout`，Agent 可直接解析和消费，而非 UI 渲染。
- **安全护栏**：需要 Obsidian 桌面应用运行、需要用户主动在设置中启用 CLI 并进行权限注册，确保用户始终处于控制之中。
- **经过验证的集成**：Claude Code 可原生通过 Bash 调用；社区已出现 MCP 封装（`@joemugen/obsidian-cli-mcp`）、Agent Client 插件及 REST API 封装等多种集成方案。

## 核心 CLI 命令

| 命令 | 功能 |
|------|------|
| `obsidian search <query>` | 使用 Obsidian 语义索引搜索笔记 |
| `obsidian read <path>` | 读取指定笔记内容 |
| `obsidian write <path>` | 创建或更新笔记 |
| `obsidian daily:prepend` | 向日记追加内容 |
| `obsidian backlinks <path>` | 查询笔记的反向链接 |
| `obsidian orphans` | 列出所有孤立笔记 |

## 性能数据

| 任务 | 传统方式 (grep) | Obsidian CLI | 提升幅度 |
|------|-----------------|--------------|----------|
| 孤立笔记检测 | 15.6s | 0.26s | **60x** |
| Vault 全文搜索 | 1.95s | 0.32s | **6x** |
| Token 消耗（MCP vs CLI）| ~700 万 tokens | ~100 tokens | **70,000x** |

---

- [Obsidian CLI 官方文档](https://help.obsidian.md/cli)
- [Obsidian 1.12 Changelog](https://obsidian.md/changelog/2026-02-27-desktop-v1.12.4/)
- [Obsidian CLI: Why Your AI Agent Just Got 70,000x Cheaper to Run](https://prokopov.me/posts/obsidian-cli-changes-everything-for-ai-agents/)
