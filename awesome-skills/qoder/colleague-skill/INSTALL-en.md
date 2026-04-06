# Installing Colleague Skill for Qoder

## Prerequisites

- [Qoder](https://github.com/) installed
- Git installed

## Installation Steps

### 1. Clone colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.qoder/colleague-skill
```

### 2. Symlink Skills

Create symlinks so Qoder discovers the skills:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/create-colleague
ln -s ~/.qoder/colleague-skill ~/.qoder/skills/create-colleague
```

### 3. Verify Installation

Restart Qoder, then try asking:
- "do you have create-colleague?"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/colleague-skill
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.qoder/skills/create-colleague
```

## Getting Help

- GitHub: https://github.com/titanwings/colleague-skill
- Report issues: https://github.com/titanwings/colleague-skill/issues
