# Installing Superpowers for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone Superpowers

```bash
git clone https://github.com/obra/superpowers.git ~/.openclaw/superpowers
```

### 2. Symlink Skills

Create symlinks so OpenClaw discovers the Superpowers skills:

```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/superpowers/skills ~/.openclaw/skills/superpowers
```

### 3. Verify Installation

Restart OpenClaw, then try asking the following to verify the installation:

- "Help me plan this feature" (triggers `brainstorming`)
- "Let's debug this issue" (triggers `systematic-debugging`)
- "do you have brainstorming?"

If successful, OpenClaw will automatically recognize and invoke the relevant Superpowers workflow.

## Updating

```bash
cd ~/.openclaw/superpowers
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/superpowers
```

## Getting Help

- GitHub: https://github.com/obra/superpowers
- Report issues: https://github.com/obra/superpowers/issues
