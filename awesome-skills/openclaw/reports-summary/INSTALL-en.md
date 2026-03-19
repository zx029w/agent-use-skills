# Install Reports Summary in OpenClaw

## Prerequisites

- OpenClaw installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that OpenClaw can discover the reports-summary skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/reports-summary
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/reports-summary ~/.openclaw/skills/reports-summary
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart OpenClaw and try the following commands to verify the installation:

- "Help me summarize the team's weekly reports"
- "do you have reports-summary skill?"

If successful, OpenClaw will recognize and invoke the Reports Summary skill workflow.

## Update

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues