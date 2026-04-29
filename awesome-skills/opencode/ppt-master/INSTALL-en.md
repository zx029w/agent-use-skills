# Installing PPT Master for OpenCode

## Prerequisites

- OpenCode installed
- Git installed
- Python 3.10+ installed

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.config/opencode/ppt-master
```

### 2. Install dependencies

```bash
pip install -r ~/.config/opencode/ppt-master/requirements.txt
```

### 3. Symlink the skill

Create a symlink so OpenCode discovers the skill:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/ppt-master
ln -s ~/.config/opencode/ppt-master/skills/ppt-master ~/.config/opencode/skills/ppt-master
```

### 4. Verify Installation

Restart OpenCode, then try asking:
- "do you have ppt-master?"
- "create a PPT from this PDF using ppt-master"

If successful, OpenCode will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.config/opencode/ppt-master
git pull
```

## Uninstallation

```bash
rm -rf ~/.config/opencode/skills/ppt-master
rm -rf ~/.config/opencode/ppt-master
```

## Getting Help

- GitHub: https://github.com/hugohe3/ppt-master
- Report issues: https://github.com/hugohe3/ppt-master/issues
- FAQ: https://github.com/hugohe3/ppt-master/blob/main/docs/faq.md
