# Install Weekly Report in Cursor

## Prerequisites

- [Cursor](https://cursor.sh/) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/agent-use-skills
```

### 2. Configure Cursor

In Cursor, open settings and add the skill directory to your workspace:

1. Open Cursor Settings
2. Find "Skills" or "Custom Skills" option
3. Add skill path: `~/agent-use-skills/awesome-skills/skills/weekly-report`

Alternatively, copy the skill files to Cursor's skills directory:

```bash
# Assuming Cursor skills directory is ~/.cursor/skills
mkdir -p ~/.cursor/skills
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.cursor/skills/
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

## Update

```bash
cd ~/agent-use-skills
git pull
# Re-copy to Cursor skills directory
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.cursor/skills/
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
