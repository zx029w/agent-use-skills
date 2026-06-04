# Installing Guizang PPT Skill for Qoder

## Prerequisites

- Qoder installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.qoder/guizang-ppt-skill
```

### 2. Symlink Skill

Create a symlink so Qoder discovers the skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/guizang-ppt-skill
ln -s ~/.qoder/guizang-ppt-skill ~/.qoder/skills/guizang-ppt-skill
```

### 3. Verify Installation

Restart Qoder, then try asking:
- "Make me a magazine-style deck"
- "Make me a Swiss-style deck"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/guizang-ppt-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.qoder/skills/guizang-ppt-skill
```

## Getting Help

- GitHub: https://github.com/op7418/guizang-ppt-skill
- Report issues: https://github.com/op7418/guizang-ppt-skill/issues
