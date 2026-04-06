# Installing slidev for OpenCode

## Prerequisites

- OpenCode installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/slidevjs/slidev.git ~/.config/opencode/slidevjs-slidev
```

### 2. Symlink Skills

Create symlinks so OpenCode discovers the skills:

```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/slidevjs-slidev/skills ~/.config/opencode/skills/slidev
```

### 3. Verify Installation

Restart OpenCode, then try asking:
- "do you have slidev?"

If successful, OpenCode will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.config/opencode/slidevjs-slidev
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.config/opencode/skills/slidev
```

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
