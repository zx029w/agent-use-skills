# Install Reports Summary in Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Claude Code can discover the reports-summary skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/reports-summary
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/reports-summary ~/.claude/skills/reports-summary
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Claude Code and try the following commands to verify the installation:

- "Help me summarize the team's weekly reports"
- "do you have reports-summary skill?"

If successful, Claude Code will recognize and invoke the Reports Summary skill workflow.

## Update

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.claude/skills/reports-summary
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
