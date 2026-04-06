# Installing slidev for Cursor

## Prerequisites

- Cursor installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/slidevjs/slidev.git ~/.cursor/slidevjs-slidev
```

### 2. Symlink Skills

Create symlinks so Cursor discovers the skills:

```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/slidevjs-slidev/skills ~/.cursor/skills/slidev
```

### 3. Verify Installation

Restart Cursor, then try asking:
- "do you have slidev?"

If successful, Cursor will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.cursor/slidevjs-slidev
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/slidev
```

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
