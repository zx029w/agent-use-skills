# Installing Baoyu Skills for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone Baoyu Skills

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.config/opencode/baoyu-skills
```

### 2. Symlink Skills

Create a symlink so OpenCode discovers the Baoyu skills:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/baoyu-skills
ln -s ~/.config/opencode/baoyu-skills/skills ~/.config/opencode/skills/baoyu-skills
```

### 3. Verify Installation

Restart OpenCode, then try asking:

- "do you have baoyu-imagine?"

If successful, OpenCode will automatically recognize and invoke the relevant Baoyu skill.

## Updating

```bash
cd ~/.config/opencode/baoyu-skills
git pull
```

## Uninstallation

```bash
rm -rf ~/.config/opencode/skills/baoyu-skills
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues
