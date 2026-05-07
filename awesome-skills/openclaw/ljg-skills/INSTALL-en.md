# Installing LJG Skills for OpenClaw

## Prerequisites

- OpenClaw installed
- Git installed

## Installation Steps

### 1. Clone LJG Skills

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.openclaw/ljg-skills
```

### 2. Symlink Skills

Create symlinks so OpenClaw discovers all the LJG skills:

```bash
mkdir -p ~/.openclaw/skills
for skill in $(ls ~/.openclaw/ljg-skills/skills); do
  rm -rf ~/.openclaw/skills/$skill
  ln -s ~/.openclaw/ljg-skills/skills/$skill ~/.openclaw/skills/$skill
done
```

### 3. Install ljg-card Dependencies (if using the card casting feature)

`ljg-card` requires Playwright for screenshot capture:

```bash
cd ~/.openclaw/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. Verify Installation

Restart OpenClaw, then try asking:

- "do you have ljg-card?"
- "do you have ljg-learn?"

If successful, OpenClaw will automatically recognize and invoke the relevant skill.

## Updating

```bash
cd ~/.openclaw/ljg-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.openclaw/ljg-skills/skills); do
  rm -rf ~/.openclaw/skills/$skill
done
rm -rf ~/.openclaw/ljg-skills
```

## Getting Help

- GitHub: https://github.com/lijigang/ljg-skills
- Report issues: https://github.com/lijigang/ljg-skills/issues
