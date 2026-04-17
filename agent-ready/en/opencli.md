# OpenCLI - Agent-Ready Certification

**OpenCLI** has officially passed the **Agent-Ready** certification!

OpenCLI transforms websites, browser sessions, Electron apps, and local tools into deterministic CLI interfaces — making it an ideal bridge between AI Agents and the broader software ecosystem.

## Certification Highlights

- **Account-Safe Operations**: Reuses Chrome/Chromium login state; credentials never leave the browser
- **Deterministic Output**: Same command produces identical output schema every time — pipeable, scriptable, CI-friendly
- **Zero LLM Runtime Cost**: No tokens consumed during execution; run 10,000 times and pay nothing
- **87+ Pre-built Adapters**: Covers Bilibili, Zhihu, Xiaohongshu, Reddit, Twitter/X, HackerNews, and more
- **Direct Browser Control**: `opencli browser` gives AI Agents direct control — navigate, click, type, extract, screenshot
- **CLI Hub Integration**: Unified discovery, auto-install, and passthrough for external CLI tools (gh, docker, obsidian, etc.)
- **Desktop App Control**: Drive Electron apps via CDP (Cursor, Codex, ChatGPT, Notion, etc.)

## Why is it Agent-Ready?

OpenCLI successfully meets all the core criteria of the Agent-Ready certification:

- **Atomic Action Exposure**: Core features fully exposed via CLI commands — browser automation, adapter generation, API exploration — no UI interaction required
- **Structured Feedback**: All command outputs follow consistent, parseable schemas; execution results are emitted as structured data to stdout, ready for Agent consumption
- **Security Guardrails**: Browser credentials remain within the browser context; no credential extraction or storage; human-in-the-loop for sensitive operations
- **Verified Integration**: Extensively tested across Claude Code, Cursor, Codex, OpenCode, and other major AI Agent platforms

## Core CLI Capabilities

| Capability | Description |
|------------|-------------|
| `opencli browser` | Direct browser control — navigate, click, type, extract, screenshot |
| `opencli explore` | API discovery and auth strategy exploration |
| `opencli generate` | Adapter generation from real browser behavior |
| `opencli list` | Discover available adapters and CLI tools |
| External CLI passthrough | Unified interface for gh, docker, obsidian, and more |

## Cost Efficiency

| Metric | Traditional Approach | OpenCLI | Improvement |
|--------|---------------------|---------|-------------|
| Runtime LLM cost | Tokens consumed per action | **Zero** | **∞** (cost eliminated) |
| Browser automation | Complex MCP setups | Built-in | **Native** |
| Adapter coverage | Manual integration | 87+ adapters | **Out-of-box** |

---

- [OpenCLI GitHub Repository](https://github.com/jackwener/OpenCLI)
- [View OpenCLI Full Documentation](../../awesome-skills/introductions/en/opencli.md)
