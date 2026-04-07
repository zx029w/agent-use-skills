# Installing Baoyu Skills for Codex

## Prerequisites

- [Codex](https://openai.com/codex) installed
- Git installed

## Installation Steps

### 1. Clone Baoyu Skills

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.codex/baoyu-skills
```

### 2. Symlink Skills

Create a symlink so Codex discovers the Baoyu skills:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/baoyu-skills
ln -s ~/.codex/baoyu-skills/skills ~/.codex/skills/baoyu-skills
```

### 3. Verify Installation

Restart Codex, then try asking:

- "do you have baoyu-imagine?"

If successful, Codex will automatically recognize and invoke the relevant Baoyu skill.

## Updating

```bash
cd ~/.codex/baoyu-skills
git pull
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/baoyu-skills
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues
