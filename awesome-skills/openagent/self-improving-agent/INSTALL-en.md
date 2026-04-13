# Installing Self-Improving Agent for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone self-improving-agent

```bash
git clone https://github.com/peterskoett/self-improving-agent.git ~/.openagent/self-improving-agent
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/self-improving-agent
ln -s ~/.openagent/self-improving-agent/skills/self-improving-agent ~/.openagent/skills/self-improving-agent
```

### 3. Verify Installation

Restart OpenAgent and try asking:
- "Help me record this learning experience"
- "do you have self-improving-agent?"

If successful, OpenAgent will automatically recognize and invoke the Self-Improving Agent skill workflow.

## Updating

```bash
cd ~/.openagent/self-improving-agent
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/self-improving-agent
```

## Getting Help

- GitHub: https://github.com/peterskoett/self-improving-agent