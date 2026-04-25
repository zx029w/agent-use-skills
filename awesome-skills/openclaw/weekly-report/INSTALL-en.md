# Install Weekly Report in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/openclaw-ai) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create Symbolic Link

Create a symbolic link so OpenClaw can discover the weekly-report skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/weekly-report
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/weekly-report ~/.openclaw/skills/weekly-report
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

## Updating

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/weekly-report
```

## Getting Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
