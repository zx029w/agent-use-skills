# Installing OfficeCLI for Codex

## Prerequisites

- Codex CLI installed
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

OfficeCLI automatically detects Codex CLI during installation and deploys the skill file to `~/.agents/skills/officecli/`.

If Codex was not detected, manually install the skill file:

```bash
mkdir -p ~/.codex/skills/officecli
curl -fsSL https://officecli.ai/SKILL.md -o ~/.codex/skills/officecli/SKILL.md
```

### 3. Verify Installation

Restart Codex, then try asking:
- "do you have officecli?"
- "create a PowerPoint presentation"

If successful, Codex will automatically recognize and invoke the OfficeCLI skill.

## Updating

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
```

OfficeCLI checks for updates automatically. Disable with `officecli config autoUpdate false`.

## Uninstallation

```bash
rm -rf ~/.codex/skills/officecli
```

## Getting Help

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- Report issues: https://github.com/iOfficeAI/OfficeCLI/issues
