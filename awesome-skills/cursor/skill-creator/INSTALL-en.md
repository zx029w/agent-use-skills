# Installing Skill Creator for Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
- Git installed
- Python 3.8+

## Installation Steps

### 1. Clone agent-use-skills Repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create Symlink

Create a symlink so Cursor discovers the skill-creator skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/skill-creator
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/skill-creator ~/.cursor/skills/skill-creator
```

### 3. Verify Installation

Restart Cursor, then try asking:
- "I need to create a new skill, please help me use skill-creator"
- "do you have skill-creator?"

If successful, Cursor will automatically recognize and invoke the Skill Creator skill workflow.

## Updating

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/skill-creator
```

## Getting Help

- GitHub Repository: https://github.com/Zerone-Agent/agent-use-skills
- Report Issues: https://github.com/Zerone-Agent/agent-use-skills/issues
