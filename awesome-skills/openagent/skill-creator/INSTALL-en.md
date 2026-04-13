# Installing Skill Creator for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- Python installed

## Installation Steps

### 1. Clone Anthropic Skills

```bash
git clone https://github.com/anthropics/skills.git ~/.openagent/anthropic-skills
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/skill-creator
ln -s ~/.openagent/anthropic-skills/skills/skill-creator ~/.openagent/skills/skill-creator
```

### 3. Verify Installation

Restart OpenAgent and try asking:
- "Help me create a new skill"
- "do you have skill-creator?"

If successful, OpenAgent will automatically recognize and invoke the Skill Creator skill workflow.

## Updating

```bash
cd ~/.openagent/anthropic-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/skill-creator
```

## Getting Help

- GitHub: https://github.com/anthropics/skills