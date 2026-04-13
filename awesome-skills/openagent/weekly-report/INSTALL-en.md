# Installing Weekly Report for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- Python and pip installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/weekly-report
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/weekly-report ~/.openagent/skills/weekly-report
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart OpenAgent and try asking:
- "Help me generate this week's weekly report"
- "do you have weekly-report?"

If successful, OpenAgent will automatically recognize and invoke the Weekly Report skill workflow.

## Updating

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/weekly-report
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues