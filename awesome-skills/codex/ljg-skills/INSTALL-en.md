# Installing LJG Skills for Codex

## Prerequisites

- Codex installed
- Git installed

## Installation Steps

### 1. Clone LJG Skills

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.codex/ljg-skills
```

### 2. Symlink Skills

Create symlinks so Codex discovers all the LJG skills:

```bash
mkdir -p ~/.codex/skills
for skill in $(ls ~/.codex/ljg-skills/skills); do
  rm -rf ~/.codex/skills/$skill
  ln -s ~/.codex/ljg-skills/skills/$skill ~/.codex/skills/$skill
done
```

### 3. Install ljg-card Dependencies (if using the card casting feature)

`ljg-card` requires Playwright for screenshot capture:

```bash
cd ~/.codex/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. Verify Installation

Restart Codex, then try asking:

- "do you have ljg-card?"
- "do you have ljg-learn?"

If successful, Codex will automatically recognize and invoke the relevant skill.

## Updating

```bash
cd ~/.codex/ljg-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.codex/ljg-skills/skills); do
  rm -rf ~/.codex/skills/$skill
done
rm -rf ~/.codex/ljg-skills
```

## Getting Help

- GitHub: https://github.com/lijigang/ljg-skills
- Report issues: https://github.com/lijigang/ljg-skills/issues
