# Install Weekly Report in OpenCode

## Prerequisites

- [OpenCode](https://github.com/opencode-ai) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Create Symbolic Link

Create a symbolic link so OpenCode can discover the weekly-report skill:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/weekly-report
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/weekly-report ~/.config/opencode/skills/weekly-report
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

## Updating

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.config/opencode/skills/weekly-report
```

## Getting Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
