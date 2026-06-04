# Installing Guizang PPT Skill for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.claude/guizang-ppt-skill
```

### 2. Symlink Skill

Create a symlink so Claude Code discovers the skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/guizang-ppt-skill
ln -s ~/.claude/guizang-ppt-skill ~/.claude/skills/guizang-ppt-skill
```

### 3. Verify Installation

Restart Claude Code, then try asking:
- "Make me a magazine-style deck"
- "Make me a Swiss-style deck"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/guizang-ppt-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.claude/skills/guizang-ppt-skill
```

## Getting Help

- GitHub: https://github.com/op7418/guizang-ppt-skill
- Report issues: https://github.com/op7418/guizang-ppt-skill/issues
