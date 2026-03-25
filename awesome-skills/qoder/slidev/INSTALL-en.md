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

for skill in $(ls ~/.qoder/slidevjs-slidev/skills); do
  rm -rf ~/.qoder/skills/$skill
  ln -s ~/.qoder/slidevjs-slidev/skills/$skill ~/.qoder/skills/$skill
done
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

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
