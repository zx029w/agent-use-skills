# Install Prompt Engineering in OpenClaw

## Installation Steps

### 1. Clone repository
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create symbolic link
```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.openclaw/skills/prompt-engineering
```

## Verify Installation

Restart OpenClaw and try:
- "Help me design a high-reliability prompt template."

## Update
```bash
cd ~/.openclaw/agent-use-skills && git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/prompt-engineering
```
