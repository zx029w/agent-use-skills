# Installing PPT Master for Qoder

## Prerequisites

- Qoder installed
- Git installed
- Python 3.10+ installed

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.qoder/ppt-master
```

### 2. Install dependencies

```bash
pip install -r ~/.qoder/ppt-master/requirements.txt
```

### 3. Symlink the skill

Create a symlink so Qoder discovers the skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/ppt-master
ln -s ~/.qoder/ppt-master/skills/ppt-master ~/.qoder/skills/ppt-master
```

### 4. Verify Installation

Restart Qoder, then try asking:
- "do you have ppt-master?"
- "create a PPT from this PDF using ppt-master"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/ppt-master
git pull
```

## Uninstallation

```bash
rm -rf ~/.qoder/skills/ppt-master
rm -rf ~/.qoder/ppt-master
```

## Getting Help

- GitHub: https://github.com/hugohe3/ppt-master
- Report issues: https://github.com/hugohe3/ppt-master/issues
- FAQ: https://github.com/hugohe3/ppt-master/blob/main/docs/faq.md
