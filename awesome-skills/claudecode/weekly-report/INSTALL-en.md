# Install Weekly Report in Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Create Symbolic Link

Create a symbolic link so Claude Code can discover the weekly-report skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/weekly-report
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/weekly-report ~/.claude/skills/weekly-report
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Claude Code, then try the following commands to verify installation:

- "帮我生成周报"
- "写一下这周的工作"
- "do you have weekly-report skill?"

If installed successfully, Claude Code will automatically recognize and invoke the Weekly Report skill workflow.

## Update

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.claude/skills/weekly-report
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
