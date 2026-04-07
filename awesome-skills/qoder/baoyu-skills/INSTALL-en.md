# Installing Baoyu Skills for Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed

## Installation Steps

### 1. Clone Baoyu Skills

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.qoder/baoyu-skills
```

### 2. Symlink Skills

Create a symlink so Qoder discovers the Baoyu skills:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/baoyu-skills
ln -s ~/.qoder/baoyu-skills/skills ~/.qoder/skills/baoyu-skills
```

### 3. Verify Installation

Restart Qoder, then try asking:

- "do you have baoyu-imagine?"

If successful, Qoder will automatically recognize and invoke the relevant Baoyu skill.

## Updating

```bash
cd ~/.qoder/baoyu-skills
git pull
```

## Uninstallation

```bash
rm -rf ~/.qoder/skills/baoyu-skills
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues
