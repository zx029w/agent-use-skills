# Installing slidev for Claude Code

## Prerequisites

- Claude Code installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/slidevjs/slidev.git ~/.claude/slidevjs-slidev
```

### 2. Symlink Skills

Create symlinks so Claude Code discovers the skills:

```bash
mkdir -p ~/.claude/skills

for skill in $(ls ~/.claude/slidevjs-slidev/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/slidevjs-slidev/skills/$skill ~/.claude/skills/$skill
done
```

### 3. Verify Installation

Restart Claude Code, then try asking:
- "do you have slidev?"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/slidevjs-slidev
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
for skill in $(ls ~/.claude/slidevjs-slidev/skills); do
  rm -rf ~/.claude/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/slidevjs/slidev
- Report issues: https://github.com/slidevjs/slidev/issues
