# Installing webapp-testing for Codex

## Prerequisites

- Codex installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/anthropics/skills.git ~/.codex/anthropics-skills
```

### 2. Symlink Skills

Create symlinks so Codex discovers the skills:

```bash
mkdir -p ~/.codex/skills

for skill in $(ls ~/.codex/anthropics-skills/skills); do
  rm -rf ~/.codex/skills/$skill
  ln -s ~/.codex/anthropics-skills/skills/$skill ~/.codex/skills/$skill
done
```

### 3. Verify Installation

Restart Codex, then try asking:
- "do you have webapp-testing?"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/anthropics-skills
git pull
```

## Getting Help

- GitHub: https://github.com/anthropics/skills
- Report issues: https://github.com/anthropics/skills/issues
