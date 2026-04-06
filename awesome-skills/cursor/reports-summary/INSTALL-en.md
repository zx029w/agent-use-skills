# Install Reports Summary in Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Cursor can discover the reports-summary skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/reports-summary
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/reports-summary ~/.cursor/skills/reports-summary
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Cursor and try the following commands to verify the installation:

- "Help me summarize the team's weekly reports"
- "do you have reports-summary skill?"

If successful, Cursor will recognize and invoke the Reports Summary skill workflow.

## Update

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/reports-summary
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
