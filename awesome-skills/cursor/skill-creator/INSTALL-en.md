# Installing Skill Creator for Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
- Git installed
- Python 3.8+

## Installation Steps

### 1. Clone anthropics/skills Repository

```bash
git clone https://github.com/anthropics/skills.git ~/.cursor/skills-repo
```

### 2. Create Symlink

Create a symlink so Cursor discovers the skill-creator skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/skill-creator
ln -s ~/.cursor/skills-repo/skills/skill-creator ~/.cursor/skills/skill-creator
```

### 3. Verify Installation

Restart Cursor, then try asking:
- "I need to create a new skill, please help me use skill-creator"
- "do you have skill-creator?"

If successful, Cursor will automatically recognize and invoke the Skill Creator skill workflow.

## Updating

```bash
cd ~/.cursor/skills-repo
git pull
```

## Getting Help

- GitHub Repository: https://github.com/anthropics/skills
- Report Issues: https://github.com/anthropics/skills/issues