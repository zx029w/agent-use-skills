# Installing Skill Market for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- Python installed (recommended: `uv`, but not required)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/skill-market
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/skill-market ~/.openagent/skills/skill-market
```

### 3. Verify Installation

Run the following command or restart OpenAgent and try asking:

```bash
~/.openagent/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

Or in OpenAgent, try asking:
- "List all available skills in the skill market"
- "do you have skill-market?"

If successful, OpenAgent will automatically recognize and invoke the Skill Market skill workflow.

## Updating

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/skill-market
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues