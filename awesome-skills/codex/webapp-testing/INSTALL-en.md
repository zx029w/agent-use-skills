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

rm -rf ~/.codex/skills/webapp-testing
ln -s ~/.codex/anthropics-skills/skills/webapp-testing ~/.codex/skills/webapp-testing
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
