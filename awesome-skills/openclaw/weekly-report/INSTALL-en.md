# Install Weekly Report in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/openclaw-ai) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/agent-use-skills
```

### 2. Configure OpenClaw

In OpenClaw, add the skill directory to your workspace through settings:

1. Open OpenClaw Settings
2. Find "Skills" or "Custom Skills" option
3. Add skill path: `~/agent-use-skills/awesome-skills/skills/weekly-report`

Alternatively, copy the skill files to OpenClaw's skills directory:

```bash
# Assuming OpenClaw skills directory is ~/.openclaw/skills
mkdir -p ~/.openclaw/skills
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.openclaw/skills/
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart OpenClaw, then try the following commands to verify installation:

- "帮我生成周报"
- "写一下这周的工作"

If installed successfully, OpenClaw will automatically recognize and invoke the Weekly Report skill workflow.

## Update

```bash
cd ~/agent-use-skills
git pull
# Re-copy to OpenClaw skills directory
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.openclaw/skills/
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
