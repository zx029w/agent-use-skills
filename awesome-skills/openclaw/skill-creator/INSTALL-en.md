# Installing Skill Creator for OpenClaw

## Prerequisites

- OpenClaw installed
- Git installed
- Python 3.8+

## Installation Steps

### 1. Clone agent-use-skills Repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create Symlink

Create a symlink so OpenClaw discovers the skill-creator skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/skill-creator
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/skill-creator ~/.openclaw/skills/skill-creator
```

### 3. Verify Installation

Restart OpenClaw, then try asking:
- "I need to create a new skill, please help me use skill-creator"
- "do you have skill-creator?"

If successful, OpenClaw will automatically recognize and invoke the Skill Creator skill workflow.

## Updating

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/skill-creator
```

## Getting Help

- GitHub Repository: https://github.com/Zerone-Agent/agent-use-skills
- Report Issues: https://github.com/Zerone-Agent/agent-use-skills/issues
