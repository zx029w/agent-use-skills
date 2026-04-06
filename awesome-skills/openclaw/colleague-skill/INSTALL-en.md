# Installing Colleague Skill for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/openclaw/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.openclaw/colleague-skill
```

### 2. Symlink Skills

Create symlinks so OpenClaw discovers the skills:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/create-colleague
ln -s ~/.openclaw/colleague-skill ~/.openclaw/skills/create-colleague
```

### 3. Verify Installation

Restart OpenClaw, then try asking:
- "do you have create-colleague?"

If successful, OpenClaw will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openclaw/colleague-skill
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/create-colleague
```

## Getting Help

- GitHub: https://github.com/titanwings/colleague-skill
- Report issues: https://github.com/titanwings/colleague-skill/issues
