# Install Reports Summary in Qoder

## Prerequisites

- Qoder installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Qoder can discover the reports-summary skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/reports-summary
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/reports-summary ~/.qoder/skills/reports-summary
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Qoder and try the following commands to verify the installation:

- "Help me summarize the team's weekly reports"
- "do you have reports-summary skill?"

If successful, Qoder will recognize and invoke the Reports Summary skill workflow.

## Update

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.qoder/skills/reports-summary
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
