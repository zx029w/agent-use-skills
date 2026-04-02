# Installing Superpowers for Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed

## Installation Steps

### 1. Clone Superpowers

```bash
git clone https://github.com/obra/superpowers.git ~/.qoder/superpowers
```

### 2. Symlink Skills

Create symlinks so Qoder discovers the Superpowers skills:

```bash
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/superpowers/skills ~/.qoder/skills/superpowers
```

### 3. Verify Installation

Restart Qoder, then try asking the following to verify the installation:

- "Help me plan this feature" (triggers `brainstorming`)
- "Let's debug this issue" (triggers `systematic-debugging`)
- "do you have brainstorming?"

If successful, Qoder will automatically recognize and invoke the relevant Superpowers workflow.

## Updating

```bash
cd ~/.qoder/superpowers
git pull
```

## Getting Help

- GitHub: https://github.com/obra/superpowers
- Report issues: https://github.com/obra/superpowers/issues
