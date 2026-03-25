# Installing webapp-testing for Claude Code

## Prerequisites

- Claude Code installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/anthropics/skills.git ~/.claude/anthropics-skills
```

### 2. Symlink Skills

Create symlinks so Claude Code discovers the skills:

```bash
mkdir -p ~/.claude/skills

for skill in $(ls ~/.claude/anthropics-skills/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/anthropics-skills/skills/$skill ~/.claude/skills/$skill
done
```

### 3. Verify Installation

Restart Claude Code, then try asking:
- "do you have webapp-testing?"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/anthropics-skills
git pull
```

## Getting Help

- GitHub: https://github.com/anthropics/skills
- Report issues: https://github.com/anthropics/skills/issues
