# Install Weekly Report in Codex

## Prerequisites

- [Codex](https://github.com/openai/codex) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/agent-use-skills
```

### 2. Create Symbolic Link

Create a symbolic link so Codex can discover the weekly-report skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/weekly-report
ln -s ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.codex/skills/weekly-report
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Codex, then try the following commands to verify installation:

- "帮我生成周报"
- "写一下这周的工作"

If installed successfully, Codex will automatically recognize and invoke the Weekly Report skill workflow.

## Update

```bash
cd ~/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.codex/skills/weekly-report
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
