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

rm -rf ~/.cursor/skills/webapp-testing
ln -s ~/.cursor/anthropics-skills/skills/webapp-testing ~/.cursor/skills/webapp-testing
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

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/webapp-testing
```

## Getting Help

- GitHub: https://github.com/anthropics/skills
- Report issues: https://github.com/anthropics/skills/issues
