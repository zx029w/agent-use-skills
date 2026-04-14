# Installing Baoyu Skills for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone Baoyu Skills

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.openagent/baoyu-skills
```

### 2. Symlink Skills

Create symlinks so OpenAgent discovers the Baoyu skills:

```bash
mkdir -p ~/.openagent/skills
for skill in $(ls ~/.openagent/baoyu-skills/skills); do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/baoyu-skills/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. Verify Installation

Restart OpenAgent, then try asking:

- "do you have baoyu-imagine?"

If successful, OpenAgent will automatically recognize and invoke the relevant Baoyu skill.

## Updating

```bash
cd ~/.openagent/baoyu-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.openagent/baoyu-skills/skills); do
  rm -rf ~/.openagent/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues