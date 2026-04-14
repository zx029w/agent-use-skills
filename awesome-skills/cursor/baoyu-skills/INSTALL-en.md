# Installing Baoyu Skills for Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
- Git installed

## Installation Steps

### 1. Clone Baoyu Skills

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.cursor/baoyu-skills
```

### 2. Symlink Skills

Create symlinks so Cursor discovers the Baoyu skills:

```bash
mkdir -p ~/.cursor/skills
for skill in $(ls ~/.cursor/baoyu-skills/skills); do
  rm -rf ~/.cursor/skills/$skill
  ln -s ~/.cursor/baoyu-skills/skills/$skill ~/.cursor/skills/$skill
done
```

### 3. Verify Installation

Restart Cursor, then try asking:

- "do you have baoyu-imagine?"

If successful, Cursor will automatically recognize and invoke the relevant Baoyu skill.

## Updating

```bash
cd ~/.cursor/baoyu-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.cursor/baoyu-skills/skills); do
  rm -rf ~/.cursor/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues
