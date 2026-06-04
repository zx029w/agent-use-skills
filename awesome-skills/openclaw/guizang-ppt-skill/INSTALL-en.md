# Installing Guizang PPT Skill for OpenClaw

## Prerequisites

- OpenClaw installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.openclaw/guizang-ppt-skill
```

### 2. Symlink Skill

Create a symlink so OpenClaw discovers the skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/guizang-ppt-skill
ln -s ~/.openclaw/guizang-ppt-skill ~/.openclaw/skills/guizang-ppt-skill
```

### 3. Verify Installation

Restart OpenClaw, then try asking:
- "Make me a magazine-style deck"
- "Make me a Swiss-style deck"

If successful, OpenClaw will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openclaw/guizang-ppt-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.openclaw/skills/guizang-ppt-skill
```

## Getting Help

- GitHub: https://github.com/op7418/guizang-ppt-skill
- Report issues: https://github.com/op7418/guizang-ppt-skill/issues
