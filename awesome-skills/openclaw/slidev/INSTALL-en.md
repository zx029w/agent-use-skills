# Installing slidev for OpenClaw

## Prerequisites

- OpenClaw installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/slidevjs/slidev.git ~/.openclaw/slidevjs-slidev
```

### 2. Symlink Skills

Create symlinks so OpenClaw discovers the skills:

```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/slidevjs-slidev/skills ~/.openclaw/skills/slidev
```

### 3. Verify Installation

Restart OpenClaw, then try asking:
- "do you have slidev?"

If successful, OpenClaw will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openclaw/slidevjs-slidev
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/slidev
```

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
