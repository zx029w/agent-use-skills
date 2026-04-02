# Installing Superpowers for Codex

## Prerequisites

- [Codex](https://openai.com/index/codex/) installed
- Git installed

## Installation Steps

### 1. Clone Superpowers

```bash
git clone https://github.com/obra/superpowers.git ~/.codex/superpowers
```

### 2. Symlink Skills

Create symlinks so Codex discovers the Superpowers skills:

```bash
mkdir -p ~/.codex/skills
ln -s ~/.codex/superpowers/skills ~/.codex/skills/superpowers
```

### 3. Verify Installation

Restart Codex, then try asking the following to verify the installation:

- "Help me plan this feature" (triggers `brainstorming`)
- "Let's debug this issue" (triggers `systematic-debugging`)
- "do you have brainstorming?"

If successful, Codex will automatically recognize and invoke the relevant Superpowers workflow.

## Updating

```bash
cd ~/.codex/superpowers
git pull
```

## Getting Help

- GitHub: https://github.com/obra/superpowers
- Report issues: https://github.com/obra/superpowers/issues