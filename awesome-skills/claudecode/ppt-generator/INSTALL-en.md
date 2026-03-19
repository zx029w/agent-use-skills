# Install PPT Generator in Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Create symbolic link

Create a symbolic link so Claude Code can discover the ppt-generator skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/ppt-generator
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/ppt-generator ~/.claude/skills/ppt-generator
```

### 3. Verify installation

Restart Claude Code, then try the following commands to verify the installation:

- "Generate a presentation about [topic]"
- "do you have ppt-generator skill?"

If installed successfully, Claude Code will automatically recognize and invoke the PPT Generator skill workflow.

## Update

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues