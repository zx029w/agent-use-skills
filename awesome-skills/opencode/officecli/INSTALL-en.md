# Installing OfficeCLI for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Install OfficeCLI Binary

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```

### 2. Install Skill

Download the OfficeCLI skill file to OpenCode's skills directory:

```bash
mkdir -p ~/.config/opencode/skills/officecli
curl -fsSL https://officecli.ai/SKILL.md -o ~/.config/opencode/skills/officecli/SKILL.md
```

### 3. Verify Installation

Restart OpenCode, then try asking:
- "do you have officecli?"
- "create a PowerPoint presentation"

If successful, OpenCode will automatically recognize and invoke the OfficeCLI skill.

## Updating

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
curl -fsSL https://officecli.ai/SKILL.md -o ~/.config/opencode/skills/officecli/SKILL.md
```

OfficeCLI checks for updates automatically. Disable with `officecli config autoUpdate false`.

## Uninstallation

```bash
rm -rf ~/.config/opencode/skills/officecli
```

## Getting Help

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- Report issues: https://github.com/iOfficeAI/OfficeCLI/issues
