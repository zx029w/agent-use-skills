# Install Weekly Report in OpenCode

## Prerequisites

- [OpenCode](https://github.com/opencode-ai) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/agent-use-skills
```

### 2. Configure OpenCode

In OpenCode, add the skill directory to your workspace through settings:

1. Open OpenCode Settings
2. Find "Skills" or "Custom Skills" option
3. Add skill path: `~/agent-use-skills/awesome-skills/skills/weekly-report`

Alternatively, copy the skill files to OpenCode's skills directory:

```bash
# Assuming OpenCode skills directory is ~/.config/opencode/skills
mkdir -p ~/.config/opencode/skills
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.config/opencode/skills/
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart OpenCode, then try the following commands to verify installation:

- "帮我生成周报"
- "写一下这周的工作"

If installed successfully, OpenCode will automatically recognize and invoke the Weekly Report skill workflow.

## Update

```bash
cd ~/agent-use-skills
git pull
# Re-copy to OpenCode skills directory
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.config/opencode/skills/
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
