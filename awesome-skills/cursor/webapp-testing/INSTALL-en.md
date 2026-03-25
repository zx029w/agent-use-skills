# Installing webapp-testing for Cursor

## Prerequisites

- Cursor installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/anthropics/skills.git ~/.cursor/anthropics-skills
```

### 2. Symlink Skills

Create symlinks so Cursor discovers the skills:

```bash
mkdir -p ~/.cursor/skills

for skill in $(ls ~/.cursor/anthropics-skills/skills); do
  rm -rf ~/.cursor/skills/$skill
  ln -s ~/.cursor/anthropics-skills/skills/$skill ~/.cursor/skills/$skill
done
```

### 3. Verify Installation

Restart Cursor, then try asking:
- "do you have webapp-testing?"

If successful, Cursor will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.cursor/anthropics-skills
git pull
```

## Getting Help

- GitHub: https://github.com/anthropics/skills
- Report issues: https://github.com/anthropics/skills/issues
