# Installing Colleague Skill for Claude Code

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code) installed
- Git installed

## Installation Steps

### 1. Clone colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.claude/colleague-skill
```

### 2. Symlink Skills

Create symlinks so Claude Code discovers the skills:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/create-colleague
ln -s ~/.claude/colleague-skill ~/.claude/skills/create-colleague
```

### 3. Verify Installation

Restart Claude Code, then try asking:
- "do you have create-colleague?"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/colleague-skill
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.claude/skills/create-colleague
```

## Getting Help

- GitHub: https://github.com/titanwings/colleague-skill
- Report issues: https://github.com/titanwings/colleague-skill/issues
