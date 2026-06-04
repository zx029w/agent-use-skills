# Installing Guizang PPT Skill for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.openagent/guizang-ppt-skill
```

### 2. Symlink Skill

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/guizang-ppt-skill
ln -s ~/.openagent/guizang-ppt-skill ~/.openagent/skills/guizang-ppt-skill
```

### 3. Verify Installation

Restart OpenAgent, then try asking:
- "Make me a magazine-style deck"
- "Make me a Swiss-style deck"

If successful, OpenAgent will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openagent/guizang-ppt-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.openagent/skills/guizang-ppt-skill
```

## Getting Help

- GitHub: https://github.com/op7418/guizang-ppt-skill
- Report issues: https://github.com/op7418/guizang-ppt-skill/issues
