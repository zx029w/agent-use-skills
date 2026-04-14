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

Create symlinks so OpenCode discovers the Baoyu skills:

```bash
mkdir -p ~/.config/opencode/skills
for skill in $(ls ~/.config/opencode/baoyu-skills/skills); do
  rm -rf ~/.config/opencode/skills/$skill
  ln -s ~/.config/opencode/baoyu-skills/skills/$skill ~/.config/opencode/skills/$skill
done
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
for skill in $(ls ~/.config/opencode/baoyu-skills/skills); do
  rm -rf ~/.config/opencode/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues
