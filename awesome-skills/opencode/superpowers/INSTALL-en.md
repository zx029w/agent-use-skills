# Installing Superpowers for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone Superpowers

```bash
git clone https://github.com/obra/superpowers.git ~/.config/opencode/superpowers
```

### 2. Symlink Skills

Create symlinks so OpenCode's native skill tool discovers Superpowers skills:

```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/superpowers/skills ~/.config/opencode/skills/superpowers
```

### 3. Verify Installation

Restart OpenCode, then try asking the following to verify the installation:

- "Help me plan this feature" (triggers `brainstorming`)
- "Let's debug this issue" (triggers `systematic-debugging`)
- "do you have brainstorming?"

If successful, OpenCode will automatically recognize and invoke the relevant Superpowers workflow.

## Updating

```bash
cd ~/.config/opencode/superpowers
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.config/opencode/skills/superpowers
```

## Getting Help

- GitHub: https://github.com/obra/superpowers
- Report issues: https://github.com/obra/superpowers/issues
