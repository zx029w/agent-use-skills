# Install Canvas Design in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create a symbolic link

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/canvas-design
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/canvas-design ~/.openclaw/skills/canvas-design
```

### 3. Verify Installation

Restart OpenClaw and verify by asking: "do you have canvas-design skill?"

## Update

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/canvas-design
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
