# Installing Skill Creator for Codex

## Prerequisites

- [Codex](https://github.com/openai/codex) installed
- Git installed
- Python 3.8+

## Installation Steps

### 1. Clone anthropics/skills Repository

```bash
git clone https://github.com/anthropics/skills.git ~/.codex/anthropics-skills
```

### 2. Create Symlink

Create a symlink so Codex discovers the skill-creator skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/skill-creator
ln -s ~/.codex/anthropics-skills/skills/skill-creator ~/.codex/skills/skill-creator
```

### 3. Verify Installation

Restart Codex, then try asking:
- "I need to create a new skill, please help me use skill-creator"
- "do you have skill-creator?"

If successful, Codex will automatically recognize and invoke the Skill Creator skill workflow.

## Updating

```bash
cd ~/.codex/anthropics-skills
git pull
```

## Getting Help

- GitHub Repository: https://github.com/anthropics/skills
- Report Issues: https://github.com/anthropics/skills/issues