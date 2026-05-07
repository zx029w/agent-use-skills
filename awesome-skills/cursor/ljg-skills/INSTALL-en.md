# Installing LJG Skills for Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
- Git installed

## Installation Steps

### 1. Clone LJG Skills

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.cursor/ljg-skills
```

### 2. Symlink Skills

Create symlinks so Cursor discovers all the LJG skills:

```bash
mkdir -p ~/.cursor/skills
for skill in $(ls ~/.cursor/ljg-skills/skills); do
  rm -rf ~/.cursor/skills/$skill
  ln -s ~/.cursor/ljg-skills/skills/$skill ~/.cursor/skills/$skill
done
```

### 3. Install ljg-card Dependencies (if using the card casting feature)

`ljg-card` requires Playwright for screenshot capture:

```bash
cd ~/.cursor/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. Verify Installation

Restart Cursor, then try asking:

- "do you have ljg-card?"
- "do you have ljg-learn?"

If successful, Cursor will automatically recognize and invoke the relevant skill.

## Updating

```bash
cd ~/.cursor/ljg-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.cursor/ljg-skills/skills); do
  rm -rf ~/.cursor/skills/$skill
done
rm -rf ~/.cursor/ljg-skills
```

## Getting Help

- GitHub: https://github.com/lijigang/ljg-skills
- Report issues: https://github.com/lijigang/ljg-skills/issues
