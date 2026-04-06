# Installing Colleague Skill for OpenCode

## Prerequisites

- [OpenCode](https://github.com/) installed
- Git installed

## Installation Steps

### 1. Clone colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.config/opencode/colleague-skill
```

### 2. Symlink Skills

Create symlinks so OpenCode discovers the skills:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/create-colleague
ln -s ~/.config/opencode/colleague-skill ~/.config/opencode/skills/create-colleague
```

### 3. Verify Installation

Restart OpenCode, then try asking:
- "do you have create-colleague?"

If successful, OpenCode will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.config/opencode/colleague-skill
git pull
```

## Getting Help

- GitHub: https://github.com/titanwings/colleague-skill
- Report issues: https://github.com/titanwings/colleague-skill/issues
