# Installing OfficeCLI for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Install OfficeCLI Binary

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```

### 2. Auto-Install Skill

OfficeCLI automatically detects Claude Code during installation and deploys the skill file to `~/.claude/skills/officecli/`.

If Claude Code was not detected, run:

```bash
officecli install claude
```

### 3. Verify Installation

Restart Claude Code, then try asking:
- "do you have officecli?"
- "create a PowerPoint presentation"

If successful, Claude Code will automatically recognize and invoke the OfficeCLI skill.

### Manual Installation (Optional)

If auto-install doesn't work, you can manually install the skill file:

```bash
mkdir -p ~/.claude/skills/officecli
curl -fsSL https://officecli.ai/SKILL.md -o ~/.claude/skills/officecli/SKILL.md
```

### MCP Server (Optional)

Register OfficeCLI as an MCP server for Claude Code:

```bash
officecli mcp claude
```

Check registration status:

```bash
officecli mcp list
```

## Updating

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
```

OfficeCLI checks for updates automatically. Disable with `officecli config autoUpdate false`.

## Uninstallation

```bash
rm -rf ~/.claude/skills/officecli
```

## Getting Help

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- Report issues: https://github.com/iOfficeAI/OfficeCLI/issues
