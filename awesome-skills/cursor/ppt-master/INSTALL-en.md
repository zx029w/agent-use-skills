# Installing PPT Master for Cursor

## Prerequisites

- [Cursor](https://cursor.sh/) installed
- Git installed
- Python 3.10+ installed

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.cursor/ppt-master
```

### 2. Install dependencies

```bash
pip install -r ~/.cursor/ppt-master/requirements.txt
```

### 3. Symlink the skill

Create a symlink so Cursor discovers the skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/ppt-master
ln -s ~/.cursor/ppt-master/skills/ppt-master ~/.cursor/skills/ppt-master
```

### 4. Verify Installation

Restart Cursor, then try asking:
- "do you have ppt-master?"
- "create a PPT from this PDF using ppt-master"

If successful, Cursor will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.cursor/ppt-master
git pull
```

## Uninstallation

```bash
rm -rf ~/.cursor/skills/ppt-master
rm -rf ~/.cursor/ppt-master
```

## Getting Help

- GitHub: https://github.com/hugohe3/ppt-master
- Report issues: https://github.com/hugohe3/ppt-master/issues
- FAQ: https://github.com/hugohe3/ppt-master/blob/main/docs/faq.md
