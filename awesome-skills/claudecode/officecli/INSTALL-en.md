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

### 2. Clone OfficeCLI Repository

```bash
git clone https://github.com/iOfficeAI/OfficeCLI.git ~/.claude/officecli
```

### 3. Symlink Skills

Create symlinks so Claude Code discovers all OfficeCLI skills:

```bash
mkdir -p ~/.claude/skills
for skill in $(ls ~/.claude/officecli/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/officecli/skills/$skill ~/.claude/skills/$skill
done
```

This installs all 11 skills: `officecli`, `officecli-docx`, `officecli-pptx`, `officecli-xlsx`, `officecli-academic-paper`, `officecli-pitch-deck`, `officecli-data-dashboard`, `officecli-financial-model`, `officecli-word-form`, `morph-ppt`, `morph-ppt-3d`.

### 4. Verify Installation

Restart Claude Code, then try asking:
- "do you have officecli?"
- "create a PowerPoint presentation"

If successful, Claude Code will automatically recognize and invoke the OfficeCLI skill.

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
cd ~/.claude/officecli
git pull
```

OfficeCLI checks for binary updates automatically. Disable with `officecli config autoUpdate false`.

## Uninstallation

```bash
for skill in $(ls ~/.claude/officecli/skills); do
  rm -rf ~/.claude/skills/$skill
done
rm -rf ~/.claude/officecli
```

## Getting Help

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- Report issues: https://github.com/iOfficeAI/OfficeCLI/issues
