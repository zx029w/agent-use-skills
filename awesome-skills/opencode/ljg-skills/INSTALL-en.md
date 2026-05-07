# Installing LJG Skills for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone LJG Skills

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.config/opencode/ljg-skills
```

### 2. Symlink Skills

Create symlinks so OpenCode discovers all the LJG skills:

```bash
mkdir -p ~/.config/opencode/skills
for skill in $(ls ~/.config/opencode/ljg-skills/skills); do
  rm -rf ~/.config/opencode/skills/$skill
  ln -s ~/.config/opencode/ljg-skills/skills/$skill ~/.config/opencode/skills/$skill
done
```

### 3. Install ljg-card Dependencies (if using the card casting feature)

`ljg-card` requires Playwright for screenshot capture:

```bash
cd ~/.config/opencode/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. Verify Installation

Restart OpenCode, then try asking:

- "do you have ljg-card?"
- "do you have ljg-learn?"

If successful, OpenCode will automatically recognize and invoke the relevant skill.

## Updating

```bash
cd ~/.config/opencode/ljg-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.config/opencode/ljg-skills/skills); do
  rm -rf ~/.config/opencode/skills/$skill
done
rm -rf ~/.config/opencode/ljg-skills
```

## Getting Help

- GitHub: https://github.com/lijigang/ljg-skills
- Report issues: https://github.com/lijigang/ljg-skills/issues
