# Install Reports Summary in Codex

## Prerequisites

- Codex installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Codex can discover the reports-summary skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/reports-summary
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/reports-summary ~/.codex/skills/reports-summary
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Codex and try the following commands to verify the installation:

- "Help me summarize the team's weekly reports"
- "do you have reports-summary skill?"

If successful, Codex will recognize and invoke the Reports Summary skill workflow.

## Update

```bash
cd ~/.codex/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues