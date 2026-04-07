# Installing Baoyu Skills for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Node.js installed (for `npx` support)
- Git installed

## Installation Steps

### Option 1: Quick Install via npx (Recommended)

```bash
npx skills add jimliu/baoyu-skills
```

### Option 2: Manual Install via Git Clone

#### 1. Clone Baoyu Skills

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.claude/baoyu-skills
```

#### 2. Symlink Skills

Create symlinks so Claude Code discovers all the Baoyu skills:

```bash
mkdir -p ~/.claude/skills
for skill in $(ls ~/.claude/baoyu-skills/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/baoyu-skills/skills/$skill ~/.claude/skills/$skill
done
```

### 3. Verify Installation

Restart Claude Code, then try asking:

- "do you have baoyu-imagine?"
- "do you have baoyu-infographic?"

If successful, Claude Code will automatically recognize and invoke the relevant Baoyu skill.

## Updating

```bash
cd ~/.claude/baoyu-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.claude/baoyu-skills/skills); do
  rm -rf ~/.claude/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues
