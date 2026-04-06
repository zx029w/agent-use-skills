# Installing slidev for Codex

## Prerequisites

- Codex installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/slidevjs/slidev.git ~/.codex/slidevjs-slidev
```

### 2. Symlink Skills

Create symlinks so Codex discovers the skills:

```bash
mkdir -p ~/.codex/skills
ln -s ~/.codex/slidevjs-slidev/skills ~/.codex/skills/slidev
```

### 3. Verify Installation

Restart Codex, then try asking:
- "do you have slidev?"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/slidevjs-slidev
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.codex/skills/slidev
```

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
