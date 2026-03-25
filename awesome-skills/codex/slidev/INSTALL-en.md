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

for skill in $(ls ~/.codex/slidevjs-slidev/skills); do
  rm -rf ~/.codex/skills/$skill
  ln -s ~/.codex/slidevjs-slidev/skills/$skill ~/.codex/skills/$skill
done
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

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
