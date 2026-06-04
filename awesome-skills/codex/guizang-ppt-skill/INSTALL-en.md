# Installing Guizang PPT Skill for Codex

## Prerequisites

- [Codex](https://github.com/openai/codex) installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.codex/guizang-ppt-skill
```

### 2. Symlink Skill

Create a symlink so Codex discovers the skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/guizang-ppt-skill
ln -s ~/.codex/guizang-ppt-skill ~/.codex/skills/guizang-ppt-skill
```

### 3. Verify Installation

Restart Codex, then try asking:
- "Make me a magazine-style deck"
- "Make me a Swiss-style deck"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/guizang-ppt-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/guizang-ppt-skill
```

## Getting Help

- GitHub: https://github.com/op7418/guizang-ppt-skill
- Report issues: https://github.com/op7418/guizang-ppt-skill/issues
