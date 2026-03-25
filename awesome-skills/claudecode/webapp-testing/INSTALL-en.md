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

rm -rf ~/.claude/skills/webapp-testing
ln -s ~/.claude/anthropics-skills/skills/webapp-testing ~/.claude/skills/webapp-testing
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
