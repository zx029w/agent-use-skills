# Installing Skill Creator for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- Python installed

## Installation Steps

### 1. Clone agent-use-skills Repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/skill-creator
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/skill-creator ~/.openagent/skills/skill-creator
```

### 3. Verify Installation

Restart OpenAgent and try asking:
- "Help me create a new skill"
- "do you have skill-creator?"

If successful, OpenAgent will automatically recognize and invoke the Skill Creator skill workflow.

## Updating

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/skill-creator
```

## Getting Help

- GitHub: https://github.com/Zerone-Agent/agent-use-skills