# Installing Anti-Distill for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.openagent/anti-distill
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/anti-distill
ln -s ~/.openagent/anti-distill/skills/anti-distill ~/.openagent/skills/anti-distill
```

### 3. Verify Installation

Restart OpenAgent and try asking:
- "Help me clean this Skill file"
- "do you have anti-distill?"

If successful, OpenAgent will automatically recognize and invoke the Anti-Distill skill workflow.

## Updating

```bash
cd ~/.openagent/anti-distill
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/anti-distill
```

## Getting Help

- GitHub: https://github.com/leilei926524-tech/anti-distill