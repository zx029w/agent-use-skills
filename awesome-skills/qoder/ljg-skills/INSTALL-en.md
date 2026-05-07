# Installing LJG Skills for Qoder

## Prerequisites

- Qoder installed
- Git installed

## Installation Steps

### 1. Clone LJG Skills

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.qoder/ljg-skills
```

### 2. Symlink Skills

Create symlinks so Qoder discovers all the LJG skills:

```bash
mkdir -p ~/.qoder/skills
for skill in $(ls ~/.qoder/ljg-skills/skills); do
  rm -rf ~/.qoder/skills/$skill
  ln -s ~/.qoder/ljg-skills/skills/$skill ~/.qoder/skills/$skill
done
```

### 3. Install ljg-card Dependencies (if using the card casting feature)

`ljg-card` requires Playwright for screenshot capture:

```bash
cd ~/.qoder/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. Verify Installation

Restart Qoder, then try asking:

- "do you have ljg-card?"
- "do you have ljg-learn?"

If successful, Qoder will automatically recognize and invoke the relevant skill.

## Updating

```bash
cd ~/.qoder/ljg-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.qoder/ljg-skills/skills); do
  rm -rf ~/.qoder/skills/$skill
done
rm -rf ~/.qoder/ljg-skills
```

## Getting Help

- GitHub: https://github.com/lijigang/ljg-skills
- Report issues: https://github.com/lijigang/ljg-skills/issues
