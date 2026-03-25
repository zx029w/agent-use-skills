# Installing webapp-testing for Qoder

## Prerequisites

- Qoder installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/anthropics/skills.git ~/.qoder/anthropics-skills
```

### 2. Symlink Skills

Create symlinks so Qoder discovers the skills:

```bash
mkdir -p ~/.qoder/skills

for skill in $(ls ~/.qoder/anthropics-skills/skills); do
  rm -rf ~/.qoder/skills/$skill
  ln -s ~/.qoder/anthropics-skills/skills/$skill ~/.qoder/skills/$skill
done
```

### 3. Verify Installation

Restart Qoder, then try asking:
- "do you have webapp-testing?"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/anthropics-skills
git pull
```

## Getting Help

- GitHub: https://github.com/anthropics/skills
- Report issues: https://github.com/anthropics/skills/issues
