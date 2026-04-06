# Installing Colleague Skill for Cursor

## Prerequisites

- [Cursor](https://cursor.sh/) installed
- Git installed

## Installation Steps

### 1. Clone colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.cursor/colleague-skill
```

### 2. Symlink Skills

Create symlinks so Cursor discovers the skills:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/create-colleague
ln -s ~/.cursor/colleague-skill ~/.cursor/skills/create-colleague
```

### 3. Verify Installation

Restart Cursor, then try asking:
- "do you have create-colleague?"

If successful, Cursor will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.cursor/colleague-skill
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/create-colleague
```

## Getting Help

- GitHub: https://github.com/titanwings/colleague-skill
- Report issues: https://github.com/titanwings/colleague-skill/issues
