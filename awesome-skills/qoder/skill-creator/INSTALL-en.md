# Installing Skill Creator for Qoder

## Prerequisites

- Qoder installed
- Git installed
- Python 3.8+

## Installation Steps

### 1. Clone anthropics/skills Repository

```bash
git clone https://github.com/anthropics/skills.git ~/.qoder/skills-repo
```

### 2. Create Symlink

Create a symlink so Qoder discovers the skill-creator skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/skill-creator
ln -s ~/.qoder/skills-repo/skills/skill-creator ~/.qoder/skills/skill-creator
```

### 3. Verify Installation

Restart Qoder, then try asking:
- "I need to create a new skill, please help me use skill-creator"
- "do you have skill-creator?"

If successful, Qoder will automatically recognize and invoke the Skill Creator skill workflow.

## Updating

```bash
cd ~/.qoder/skills-repo
git pull
```

## Getting Help

- GitHub Repository: https://github.com/anthropics/skills
- Report Issues: https://github.com/anthropics/skills/issues