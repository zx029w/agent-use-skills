# Install Weekly Report in Qoder

## Prerequisites

- [Qoder](https://github.com/qoder-ai) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/agent-use-skills
```

### 2. Configure Qoder

In Qoder, add the skill directory to your workspace through settings:

1. Open Qoder Settings
2. Find "Skills" or "Custom Skills" option
3. Add skill path: `~/agent-use-skills/awesome-skills/skills/weekly-report`

Alternatively, copy the skill files to Qoder's skills directory:

```bash
# Assuming Qoder skills directory is ~/.qoder/skills
mkdir -p ~/.qoder/skills
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.qoder/skills/
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Qoder, then try the following commands to verify installation:

- "帮我生成周报"
- "写一下这周的工作"

If installed successfully, Qoder will automatically recognize and invoke the Weekly Report skill workflow.

## Update

```bash
cd ~/agent-use-skills
git pull
# Re-copy to Qoder skills directory
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.qoder/skills/
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
