# Installing OfficeCLI for Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
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

OfficeCLI automatically detects Cursor during installation and deploys the skill file to `~/.cursor/skills/officecli/`.

If Cursor was not detected, run:

```bash
officecli install cursor
```

### 3. Verify Installation

Restart Cursor, then try asking in Agent mode:
- "do you have officecli?"
- "create a PowerPoint presentation"

If successful, Cursor will automatically recognize and invoke the OfficeCLI skill.

### Manual Installation (Optional)

If auto-install doesn't work, you can manually install the skill file:

```bash
mkdir -p ~/.cursor/skills/officecli
curl -fsSL https://officecli.ai/SKILL.md -o ~/.cursor/skills/officecli/SKILL.md
```

### MCP Server (Optional)

Register OfficeCLI as an MCP server for Cursor:

```bash
officecli mcp cursor
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
rm -rf ~/.cursor/skills/officecli
```

## Getting Help

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- Report issues: https://github.com/iOfficeAI/OfficeCLI/issues
