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

Create symlinks so Qoder discovers the Baoyu skills:

```bash
mkdir -p ~/.qoder/skills
for skill in $(ls ~/.qoder/baoyu-skills/skills); do
  rm -rf ~/.qoder/skills/$skill
  ln -s ~/.qoder/baoyu-skills/skills/$skill ~/.qoder/skills/$skill
done
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
for skill in $(ls ~/.qoder/baoyu-skills/skills); do
  rm -rf ~/.qoder/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues
