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

### 2. Clone OfficeCLI Repository

```bash
git clone https://github.com/iOfficeAI/OfficeCLI.git ~/.cursor/officecli
```

### 3. Symlink Skills

Create symlinks so Cursor discovers all OfficeCLI skills:

```bash
mkdir -p ~/.cursor/skills
for skill in $(ls ~/.cursor/officecli/skills); do
  rm -rf ~/.cursor/skills/$skill
  ln -s ~/.cursor/officecli/skills/$skill ~/.cursor/skills/$skill
done
```

This installs all 11 skills: `officecli`, `officecli-docx`, `officecli-pptx`, `officecli-xlsx`, `officecli-academic-paper`, `officecli-pitch-deck`, `officecli-data-dashboard`, `officecli-financial-model`, `officecli-word-form`, `morph-ppt`, `morph-ppt-3d`.

### 4. Verify Installation

Restart Cursor, then try asking in Agent mode:
- "do you have officecli?"
- "create a PowerPoint presentation"

If successful, Cursor will automatically recognize and invoke the OfficeCLI skill.

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
cd ~/.cursor/officecli
git pull
```

OfficeCLI checks for binary updates automatically. Disable with `officecli config autoUpdate false`.

## Uninstallation

```bash
for skill in $(ls ~/.cursor/officecli/skills); do
  rm -rf ~/.cursor/skills/$skill
done
rm -rf ~/.cursor/officecli
```

## Getting Help

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- Report issues: https://github.com/iOfficeAI/OfficeCLI/issues
