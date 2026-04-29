# Installing PPT Master for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed
- Python 3.10+ installed

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.claude/ppt-master
```

### 2. Install dependencies

```bash
pip install -r ~/.claude/ppt-master/requirements.txt
```

### 3. Symlink the skill

Create a symlink so Claude Code discovers the skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/ppt-master
ln -s ~/.claude/ppt-master/skills/ppt-master ~/.claude/skills/ppt-master
```

### 4. Verify Installation

Restart Claude Code, then try asking:
- "do you have ppt-master?"
- "create a PPT from this PDF using ppt-master"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/ppt-master
git pull
```

Or use the built-in update script:
```bash
python3 ~/.claude/ppt-master/skills/ppt-master/scripts/update_repo.py
```

## Uninstallation

```bash
rm -rf ~/.claude/skills/ppt-master
rm -rf ~/.claude/ppt-master
```

## Getting Help

- GitHub: https://github.com/hugohe3/ppt-master
- Report issues: https://github.com/hugohe3/ppt-master/issues
- FAQ: https://github.com/hugohe3/ppt-master/blob/main/docs/faq.md
