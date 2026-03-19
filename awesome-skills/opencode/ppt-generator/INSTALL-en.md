# Install PPT Generator for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Create symbolic link

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/ppt-generator
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/ppt-generator ~/.config/opencode/skills/ppt-generator
```

### 3. Restart OpenCode

Restart OpenCode and verify the installation by asking: "do you have ppt-generator?"

## Update

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues