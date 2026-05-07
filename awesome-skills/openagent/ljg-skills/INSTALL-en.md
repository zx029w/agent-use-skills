# Installing LJG Skills for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone LJG Skills

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.openagent/ljg-skills
```

### 2. Symlink Skills

Create symlinks so OpenAgent discovers all the LJG skills:

```bash
mkdir -p ~/.openagent/skills
for skill in $(ls ~/.openagent/ljg-skills/skills); do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/ljg-skills/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. Install ljg-card Dependencies (if using the card casting feature)

`ljg-card` requires Playwright for screenshot capture:

```bash
cd ~/.openagent/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. Verify Installation

Restart OpenAgent, then try asking:

- "do you have ljg-card?"
- "do you have ljg-learn?"

If successful, OpenAgent will automatically recognize and invoke the relevant skill.

## Updating

```bash
cd ~/.openagent/ljg-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.openagent/ljg-skills/skills); do
  rm -rf ~/.openagent/skills/$skill
done
rm -rf ~/.openagent/ljg-skills
```

## Getting Help

- GitHub: https://github.com/lijigang/ljg-skills
- Report issues: https://github.com/lijigang/ljg-skills/issues
