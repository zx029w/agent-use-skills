# Installing LJG Skills for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Node.js installed (for `npx` support)
- Git installed

## Installation Steps

### Option 1: Quick Install via npx (Recommended)

```bash
npx skills add lijigang/ljg-skills -g --all
```

For Markdown format (compatible with Obsidian / VSCode / Notion etc.):

```bash
npx skills add lijigang/ljg-skills#md -g --all
```

Install a single skill:

```bash
npx skills add lijigang/ljg-skills -g --skill ljg-card
```

### Option 2: Manual Install via Git Clone

#### 1. Clone LJG Skills

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.claude/ljg-skills
```

#### 2. Symlink Skills

Create symlinks so Claude Code discovers all the LJG skills:

```bash
mkdir -p ~/.claude/skills
for skill in $(ls ~/.claude/ljg-skills/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/ljg-skills/skills/$skill ~/.claude/skills/$skill
done
```

### 3. Install ljg-card Dependencies (if using the card casting feature)

`ljg-card` requires Playwright for screenshot capture:

```bash
cd ~/.claude/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. Verify Installation

Restart Claude Code, then try asking:

- "do you have ljg-card?"
- "do you have ljg-learn?"

If successful, Claude Code will automatically recognize and invoke the relevant skill.

## Updating

### npx Method

```bash
npx skills add lijigang/ljg-skills -g --all
```

### Git Method

```bash
cd ~/.claude/ljg-skills
git pull
```

## Uninstallation

### npx Method

```bash
npx skills remove lijigang/ljg-skills -g --all
```

### Git Method

```bash
for skill in $(ls ~/.claude/ljg-skills/skills); do
  rm -rf ~/.claude/skills/$skill
done
rm -rf ~/.claude/ljg-skills
```

## Getting Help

- GitHub: https://github.com/lijigang/ljg-skills
- Report issues: https://github.com/lijigang/ljg-skills/issues
