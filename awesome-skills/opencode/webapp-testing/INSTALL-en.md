# Installing webapp-testing for OpenCode

## Prerequisites

- OpenCode installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/anthropics/skills.git ~/.config/opencode/anthropics-skills
```

### 2. Symlink Skills

Create symlinks so OpenCode discovers the skills:

```bash
mkdir -p ~/.config/opencode/skills

for skill in $(ls ~/.config/opencode/anthropics-skills/skills); do
  rm -rf ~/.config/opencode/skills/$skill
  ln -s ~/.config/opencode/anthropics-skills/skills/$skill ~/.config/opencode/skills/$skill
done
```

### 3. Verify Installation

Restart OpenCode, then try asking:
- "do you have webapp-testing?"

If successful, OpenCode will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.config/opencode/anthropics-skills
git pull
```

## Getting Help

- GitHub: https://github.com/anthropics/skills
- Report issues: https://github.com/anthropics/skills/issues
