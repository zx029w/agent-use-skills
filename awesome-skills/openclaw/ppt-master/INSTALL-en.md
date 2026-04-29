# Installing PPT Master for OpenClaw

## Prerequisites

- OpenClaw installed
- Git installed
- Python 3.10+ installed

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.openclaw/ppt-master
```

### 2. Install dependencies

```bash
pip install -r ~/.openclaw/ppt-master/requirements.txt
```

### 3. Symlink the skill

Create a symlink so OpenClaw discovers the skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/ppt-master
ln -s ~/.openclaw/ppt-master/skills/ppt-master ~/.openclaw/skills/ppt-master
```

### 4. Verify Installation

Restart OpenClaw, then try asking:
- "do you have ppt-master?"
- "create a PPT from this PDF using ppt-master"

If successful, OpenClaw will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openclaw/ppt-master
git pull
```

## Uninstallation

```bash
rm -rf ~/.openclaw/skills/ppt-master
rm -rf ~/.openclaw/ppt-master
```

## Getting Help

- GitHub: https://github.com/hugohe3/ppt-master
- Report issues: https://github.com/hugohe3/ppt-master/issues
- FAQ: https://github.com/hugohe3/ppt-master/blob/main/docs/faq.md
