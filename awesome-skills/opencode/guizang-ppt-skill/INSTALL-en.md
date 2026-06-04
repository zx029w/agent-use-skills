# Installing Guizang PPT Skill for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.config/opencode/guizang-ppt-skill
```

### 2. Symlink Skill

Create a symlink so OpenCode discovers the skill:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/guizang-ppt-skill
ln -s ~/.config/opencode/guizang-ppt-skill ~/.config/opencode/skills/guizang-ppt-skill
```

### 3. Verify Installation

Restart OpenCode, then try asking:
- "Make me a magazine-style deck"
- "Make me a Swiss-style deck"

If successful, OpenCode will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.config/opencode/guizang-ppt-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.config/opencode/skills/guizang-ppt-skill
```

## Getting Help

- GitHub: https://github.com/op7418/guizang-ppt-skill
- Report issues: https://github.com/op7418/guizang-ppt-skill/issues
