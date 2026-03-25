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

for skill in $(ls ~/.config/opencode/slidevjs-slidev/skills); do
  rm -rf ~/.config/opencode/skills/$skill
  ln -s ~/.config/opencode/slidevjs-slidev/skills/$skill ~/.config/opencode/skills/$skill
done
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

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
