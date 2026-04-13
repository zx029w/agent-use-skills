# Installing Colleague Skill for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.openagent/colleague-skill
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/colleague-skill
ln -s ~/.openagent/colleague-skill/skills/colleague-skill ~/.openagent/skills/colleague-skill
```

### 3. Verify Installation

Restart OpenAgent and try asking:
- "Help me create a digital colleague"
- "do you have colleague-skill?"

If successful, OpenAgent will automatically recognize and invoke the Colleague Skill workflow.

## Updating

```bash
cd ~/.openagent/colleague-skill
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/colleague-skill
```

## Getting Help

- GitHub: https://github.com/titanwings/colleague-skill