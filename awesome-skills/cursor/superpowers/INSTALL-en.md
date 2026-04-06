# Installing Superpowers in Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
- Git installed

## Installation Steps

### 1. Clone Superpowers

```bash
git clone https://github.com/obra/superpowers.git ~/.cursor/superpowers
```

### 2. Symlink Skills

Create symlinks so Cursor discovers the Superpowers skills:

```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/superpowers/skills ~/.cursor/skills/superpowers
```

### 3. Verify Installation

Restart Cursor, then try asking the following to verify the installation:

- "Help me plan this feature" (triggers `brainstorming`)
- "Let's debug this issue" (triggers `systematic-debugging`)
- "do you have brainstorming?"

If successful, Cursor will automatically recognize and invoke the relevant Superpowers workflow.

## Updating

```bash
cd ~/.cursor/superpowers
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/superpowers
```

## Getting Help

- GitHub: https://github.com/obra/superpowers
- Report issues: https://github.com/obra/superpowers/issues
