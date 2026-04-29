# Installing PPT Master for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- Python 3.10+ installed

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.openagent/ppt-master
```

### 2. Install dependencies

```bash
pip install -r ~/.openagent/ppt-master/requirements.txt
```

### 3. Symlink the skill

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/ppt-master
ln -s ~/.openagent/ppt-master/skills/ppt-master ~/.openagent/skills/ppt-master
```

### 4. Verify Installation

Restart OpenAgent, then try asking:
- "do you have ppt-master?"
- "create a PPT from this PDF using ppt-master"

If successful, OpenAgent will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openagent/ppt-master
git pull
```

## Uninstallation

```bash
rm -rf ~/.openagent/skills/ppt-master
rm -rf ~/.openagent/ppt-master
```

## Getting Help

- GitHub: https://github.com/hugohe3/ppt-master
- Report issues: https://github.com/hugohe3/ppt-master/issues
- FAQ: https://github.com/hugohe3/ppt-master/blob/main/docs/faq.md
