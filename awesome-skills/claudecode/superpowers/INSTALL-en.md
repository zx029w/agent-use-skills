# Installing Superpowers for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone Superpowers

```bash
git clone https://github.com/obra/superpowers.git ~/.claude/superpowers
```

### 2. Symlink Skills

Create symlinks so Claude Code discovers the Superpowers skills:

```bash
mkdir -p ~/.claude/skills
ln -s ~/.claude/superpowers ~/.claude/skills/superpowers
```

### 3. Verify Installation

Restart Claude Code, then try asking the following to verify the installation:

- "Help me plan this feature" (triggers `brainstorming`)
- "Let's debug this issue" (triggers `systematic-debugging`)
- "do you have brainstorming?"

If successful, Claude Code will automatically recognize and invoke the relevant Superpowers workflow.

## Updating

```bash
cd ~/.claude/superpowers
git pull
```

## Getting Help

- GitHub: https://github.com/obra/superpowers
- Report issues: https://github.com/obra/superpowers/issues