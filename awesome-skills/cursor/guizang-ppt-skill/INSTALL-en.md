# Installing Guizang PPT Skill for Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.cursor/guizang-ppt-skill
```

### 2. Symlink Skill

Create a symlink so Cursor discovers the skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/guizang-ppt-skill
ln -s ~/.cursor/guizang-ppt-skill ~/.cursor/skills/guizang-ppt-skill
```

### 3. Verify Installation

Restart Cursor, then try asking:
- "Make me a magazine-style deck"
- "Make me a Swiss-style deck"

If successful, Cursor will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.cursor/guizang-ppt-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.cursor/skills/guizang-ppt-skill
```

## Getting Help

- GitHub: https://github.com/op7418/guizang-ppt-skill
- Report issues: https://github.com/op7418/guizang-ppt-skill/issues
