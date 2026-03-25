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

for skill in $(ls ~/.cursor/slidevjs-slidev/skills); do
  rm -rf ~/.cursor/skills/$skill
  ln -s ~/.cursor/slidevjs-slidev/skills/$skill ~/.cursor/skills/$skill
done
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

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
