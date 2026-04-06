# Installing Anti-Distill for Cursor

## Prerequisites

- [Cursor](https://cursor.sh/) installed
- Git installed

## Installation Steps

### 1. Clone anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.cursor/anti-distill
```

### 2. Symlink Skills

Create symlinks so Cursor discovers the skills:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/anti-distill
ln -s ~/.cursor/anti-distill ~/.cursor/skills/anti-distill
```

### 3. Verify Installation

Restart Cursor, then try asking:
- "do you have anti-distill?"

If successful, Cursor will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.cursor/anti-distill
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/anti-distill
```

## Getting Help

- GitHub: https://github.com/leilei926524-tech/anti-distill
- Report issues: https://github.com/leilei926524-tech/anti-distill/issues
