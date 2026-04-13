# Obsidian Skills

**Obsidian Skills** is a collection of Agent Skills designed specifically for the Obsidian knowledge management tool. It follows the [Agent Skills specification](https://agentskills.io/specification) and works with Claude Code, Codex CLI, and other Skills-compatible AI coding agents.

## Tags

🛠️ Productivity Tools | ✅ Verified

## Core Philosophy

- **Standardization**: Strictly adheres to the Agent Skills specification for cross-platform compatibility
- **Modularity**: Each Skill is independent and can be used on-demand, providing flexibility and efficiency
- **Native Experience**: Deeply integrated with Obsidian's unique features for a native-level user experience
- **Developer-Friendly**: Supports Obsidian plugin and theme development with a complete development toolchain

## Key Features & Workflow

### 1. Obsidian Markdown Editing
Create and edit Obsidian Flavored Markdown with support for:
- **Wikilinks**: Internal linking using `[[Note Name]]`
- **Embeds**: Inline embedding with `![[embed]]` for notes, images, and PDFs
- **Callouts**: Highlighted information displays with types like `note`, `warning`, `tip`
- **Properties**: YAML frontmatter management supporting tags, aliases, and custom properties
- **Comments & Highlights**: `%%hidden comments%%` and `==highlighted text==`

### 2. Obsidian Bases Database
Create and edit `.base` files for Notion-like database functionality:
- **Multiple Views**: Table, cards, list, and map views
- **Filters**: Filter by tags, folders, properties, or dates
- **Formulas**: Support arithmetic operations, conditional logic, and date calculations
- **Summaries**: Statistical functions like average, sum, min/max

### 3. JSON Canvas Visualization
Create and edit `.canvas` files with infinite canvas support:
- **Node Types**: Text, file, link, and group nodes
- **Edge Connections**: Labeled connectors with directional arrows
- **Free Layout**: Negative coordinate support for infinitely expandable canvas
- **Color Presets**: 6 brand colors + custom HEX values

### 4. Obsidian CLI Integration
Interact with Obsidian Vault via command line:
- **Note Management**: Create, read, search, and append content
- **Task Management**: Todo list operations
- **Property Operations**: Set and modify frontmatter properties
- **Development Tools**: Plugin reload, error capture, screenshots, DOM inspection

### 5. Defuddle Web Extraction
Extract clean Markdown from web pages using Defuddle CLI:
- **Noise Removal**: Automatically strips navigation, ads, and clutter
- **Token Saving**: Extracts core content, reducing unnecessary data transfer
- **Metadata Extraction**: Supports title, description, domain, and other fields

## Skills Library Overview

| Skill | Description |
|-------|-------------|
| **obsidian-markdown** | Create and edit Obsidian Flavored Markdown (.md) with wikilinks, embeds, callouts, properties |
| **obsidian-bases** | Create and edit Obsidian Bases (.base) with views, filters, formulas, summaries |
| **json-canvas** | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, connections |
| **obsidian-cli** | Interact with Obsidian vaults via CLI including plugin and theme development |
| **defuddle** | Extract clean markdown from web pages using Defuddle, removing clutter to save tokens |

## Installation & Support

Obsidian Skills supports the following AI editors and platforms:

- [Claude Code](../../claudecode/obsidian/INSTALL-en.md)
- [Cursor](../../cursor/obsidian/INSTALL-en.md)
- [Codex CLI](../../codex/obsidian/INSTALL-en.md)
- [OpenCode](../../opencode/obsidian/INSTALL-en.md)
- [OpenClaw](../../openclaw/obsidian/INSTALL-en.md)
- [OpenAgent](../../openagent/obsidian/INSTALL-en.md)
- [Qoder](../../qoder/obsidian/INSTALL-en.md)

---

For more information, visit: [GitHub - kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)
