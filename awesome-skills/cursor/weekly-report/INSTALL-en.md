# Install Weekly Report in Cursor

## Prerequisites

- [Cursor](https://cursor.sh/) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create Symbolic Link

Create a symbolic link so Cursor can discover the weekly-report skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/weekly-report
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/weekly-report ~/.cursor/skills/weekly-report
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Cursor, then try the following commands to verify installation:

- "帮我生成周报"
- "写一下这周的工作"

If installed successfully, Cursor will automatically recognize and invoke the Weekly Report skill workflow.

## Updating

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/weekly-report
```

## Getting Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
