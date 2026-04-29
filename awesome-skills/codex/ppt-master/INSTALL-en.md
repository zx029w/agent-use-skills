# Installing PPT Master for Codex

## Prerequisites

- [Codex CLI](https://github.com/openai/codex) installed
- Git installed
- Python 3.10+ installed

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.codex/ppt-master
```

### 2. Install dependencies

```bash
pip install -r ~/.codex/ppt-master/requirements.txt
```

### 3. Symlink the skill

Create a symlink so Codex discovers the skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/ppt-master
ln -s ~/.codex/ppt-master/skills/ppt-master ~/.codex/skills/ppt-master
```

### 4. Verify Installation

Restart Codex, then try asking:
- "do you have ppt-master?"
- "create a PPT from this PDF using ppt-master"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/ppt-master
git pull
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/ppt-master
rm -rf ~/.codex/ppt-master
```

## Getting Help

- GitHub: https://github.com/hugohe3/ppt-master
- Report issues: https://github.com/hugohe3/ppt-master/issues
- FAQ: https://github.com/hugohe3/ppt-master/blob/main/docs/faq.md
