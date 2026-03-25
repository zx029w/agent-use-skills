# Installing webapp-testing for OpenClaw

## Prerequisites

- OpenClaw installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/anthropics/skills.git ~/.openclaw/anthropics-skills
```

### 2. Symlink Skills

Create symlinks so OpenClaw discovers the skills:

```bash
mkdir -p ~/.openclaw/skills

for skill in $(ls ~/.openclaw/anthropics-skills/skills); do
  rm -rf ~/.openclaw/skills/$skill
  ln -s ~/.openclaw/anthropics-skills/skills/$skill ~/.openclaw/skills/$skill
done
```

### 3. Verify Installation

Restart OpenClaw, then try asking:
- "do you have webapp-testing?"

If successful, OpenClaw will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openclaw/anthropics-skills
git pull
```

## Getting Help

- GitHub: https://github.com/anthropics/skills
- Report issues: https://github.com/anthropics/skills/issues
