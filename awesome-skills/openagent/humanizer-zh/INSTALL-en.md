# Installing Humanizer-zh for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/humanizer-zh
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/humanizer-zh ~/.openagent/skills/humanizer-zh
```

### 3. Verify Installation

Restart OpenAgent and try asking:
- "Help me remove AI writing traces from this text"
- "do you have humanizer-zh?"

If successful, OpenAgent will automatically recognize and invoke the Humanizer-zh skill workflow.

## Updating

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/humanizer-zh
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues