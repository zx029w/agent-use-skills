# Installing slidev for Qoder

## Prerequisites

- Qoder installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/slidevjs/slidev.git ~/.qoder/slidevjs-slidev
```

### 2. Symlink Skills

Create symlinks so Qoder discovers the skills:

```bash
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/slidevjs-slidev/skills ~/.qoder/skills/slidev
```

### 3. Verify Installation

Restart Qoder, then try asking:
- "do you have slidev?"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/slidevjs-slidev
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.qoder/skills/slidev
```

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
