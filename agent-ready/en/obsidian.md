# Obsidian - Agent-Ready Certification

**Obsidian** has officially passed the **Agent-Ready** certification!

📺 **Demo Video**：[B 站观看 → Obsidian CLI × AI Agent 实战演示](https://www.bilibili.com/video/BV1ydA7zUE5A)

Obsidian 1.12 (released February 27, 2026) introduced an official CLI and TUI (Terminal User Interface), making it one of the first knowledge management applications natively optimized for AI Agent interaction.

## Certification Highlights

- **Native CLI Support**: Directly manipulate your vault via the `obsidian` command-line tool — no raw file parsing needed.
- **Semantic Search**: Leverages Obsidian's own search index for structured, tag-aware, link-aware queries.
- **Graph Queries**: Access the knowledge graph via `obsidian backlinks` and `obsidian orphans` without scanning every file.
- **Exceptional Performance**: Orphan detection is **60x faster** than grep; token consumption can be reduced by up to **70,000x**.
- **Ecosystem Integration**: Natively supported by Claude Code, MCP Servers, and REST API wrappers.

## Why is it Agent-Ready?

Obsidian successfully meets all the core criteria of the Agent-Ready certification:

- **Atomic Action Exposure**: Core features are fully exposed via CLI commands — `obsidian search`, `obsidian read`, `obsidian write`, `obsidian daily:prepend`, `obsidian backlinks`, `obsidian orphans` — requiring no UI interaction.
- **Structured Feedback**: Search results and graph queries are emitted as structured text to `stdout`, ready for Agent parsing and consumption, rather than being rendered visually.
- **Security Guardrails**: Requires the Obsidian desktop app to be running and users to explicitly enable and register the CLI via settings, keeping humans in full control.
- **Verified Integration**: Claude Code can natively invoke the CLI via Bash; the community has built MCP wrappers (`@joemugen/obsidian-cli-mcp`), Agent Client plugins, and REST API bridges.

## Core CLI Commands

| Command | Description |
|---------|-------------|
| `obsidian search <query>` | Search notes using Obsidian's semantic index |
| `obsidian read <path>` | Read the content of a specific note |
| `obsidian write <path>` | Create or update a note |
| `obsidian daily:prepend` | Prepend content to the daily note |
| `obsidian backlinks <path>` | Query backlinks for a given note |
| `obsidian orphans` | List all orphaned notes in the vault |

## Performance Benchmarks

| Task | Traditional (grep) | Obsidian CLI | Improvement |
|------|--------------------|--------------|-------------|
| Orphan note detection | 15.6s | 0.26s | **60x** |
| Vault full-text search | 1.95s | 0.32s | **6x** |
| Token usage (MCP vs CLI) | ~7M tokens | ~100 tokens | **70,000x** |

---

- [Obsidian CLI Official Docs](https://help.obsidian.md/cli)
- [Obsidian 1.12 Changelog](https://obsidian.md/changelog/2026-02-27-desktop-v1.12.4/)
- [Obsidian CLI: Why Your AI Agent Just Got 70,000x Cheaper to Run](https://prokopov.me/posts/obsidian-cli-changes-everything-for-ai-agents/)
