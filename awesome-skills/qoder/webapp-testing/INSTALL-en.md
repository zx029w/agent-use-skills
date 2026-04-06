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

rm -rf ~/.qoder/skills/webapp-testing
ln -s ~/.qoder/anthropics-skills/skills/webapp-testing ~/.qoder/skills/webapp-testing
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

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.qoder/skills/webapp-testing
```

## Getting Help

- GitHub: https://github.com/anthropics/skills
- Report issues: https://github.com/anthropics/skills/issues
