# Installing Colleague Skill for Codex

## Prerequisites

- [Codex](https://github.com/) installed
- Git installed

## Installation Steps

### 1. Clone colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.codex/colleague-skill
```

### 2. Symlink Skills

Create symlinks so Codex discovers the skills:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/create-colleague
ln -s ~/.codex/colleague-skill ~/.codex/skills/create-colleague
```

### 3. Verify Installation

Restart Codex, then try asking:
- "do you have create-colleague?"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/colleague-skill
git pull
```

## Getting Help

- GitHub: https://github.com/titanwings/colleague-skill
- Report issues: https://github.com/titanwings/colleague-skill/issues
