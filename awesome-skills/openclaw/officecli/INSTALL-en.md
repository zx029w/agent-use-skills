# Installing OfficeCLI for OpenClaw

## Prerequisites

- OpenClaw installed
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

OfficeCLI automatically detects OpenClaw during installation and deploys the skill file to `~/.openclaw/skills/officecli/`.

If OpenClaw was not detected, manually install the skill file:

```bash
mkdir -p ~/.openclaw/skills/officecli
curl -fsSL https://officecli.ai/SKILL.md -o ~/.openclaw/skills/officecli/SKILL.md
```

### 3. Verify Installation

Restart OpenClaw, then try asking:
- "do you have officecli?"
- "create a PowerPoint presentation"

If successful, OpenClaw will automatically recognize and invoke the OfficeCLI skill.

## Updating

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
```

OfficeCLI checks for updates automatically. Disable with `officecli config autoUpdate false`.

## Uninstallation

```bash
rm -rf ~/.openclaw/skills/officecli
```

## Getting Help

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- Report issues: https://github.com/iOfficeAI/OfficeCLI/issues
