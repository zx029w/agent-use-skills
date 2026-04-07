# Installing Baoyu Skills for OpenClaw

## Prerequisites

- [OpenClaw](https://openclaw.ai) installed
- Git installed

## Installation Steps

### 1. Clone Baoyu Skills

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.openclaw/baoyu-skills
```

### 2. Symlink Skills

Create a symlink so OpenClaw discovers the Baoyu skills:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/baoyu-skills
ln -s ~/.openclaw/baoyu-skills/skills ~/.openclaw/skills/baoyu-skills
```

### 3. Verify Installation

Restart OpenClaw, then try asking:

- "do you have baoyu-imagine?"

If successful, OpenClaw will automatically recognize and invoke the relevant Baoyu skill.

> **Note**: You can also install individual skills from ClawHub:
> ```bash
> clawhub install baoyu-imagine
> clawhub install baoyu-infographic
> ```

## Updating

```bash
cd ~/.openclaw/baoyu-skills
git pull
```

## Uninstallation

```bash
rm -rf ~/.openclaw/skills/baoyu-skills
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues
