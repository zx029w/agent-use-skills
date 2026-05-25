# Installing OfficeCLI for OpenAgent

## Prerequisites

- OpenAgent installed
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
git clone https://github.com/iOfficeAI/OfficeCLI.git ~/.openagent/officecli
```

### 3. Symlink Skills

Create symlinks so OpenAgent discovers all OfficeCLI skills:

```bash
mkdir -p ~/.openagent/skills
for skill in $(ls ~/.openagent/officecli/skills); do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/officecli/skills/$skill ~/.openagent/skills/$skill
done
```

This installs all 11 skills: `officecli`, `officecli-docx`, `officecli-pptx`, `officecli-xlsx`, `officecli-academic-paper`, `officecli-pitch-deck`, `officecli-data-dashboard`, `officecli-financial-model`, `officecli-word-form`, `morph-ppt`, `morph-ppt-3d`.

### 4. Verify Installation

Restart OpenAgent, then try asking:
- "do you have officecli?"
- "create a PowerPoint presentation"

If successful, OpenAgent will automatically recognize and invoke the OfficeCLI skill.

## Updating

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
cd ~/.openagent/officecli
git pull
```

OfficeCLI checks for binary updates automatically. Disable with `officecli config autoUpdate false`.

## Uninstallation

```bash
for skill in $(ls ~/.openagent/officecli/skills); do
  rm -rf ~/.openagent/skills/$skill
done
rm -rf ~/.openagent/officecli
```

## Getting Help

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- Report issues: https://github.com/iOfficeAI/OfficeCLI/issues
