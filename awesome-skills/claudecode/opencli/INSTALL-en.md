# Installing OpenCLI for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed
- Node.js >= 21.0.0 (or Bun >= 1.0) installed

## Installation Steps

### 1. Clone OpenCLI Repository

```bash
git clone https://github.com/jackwener/OpenCLI.git ~/.claude/opencli
```

### 2. Symlink Skills

Create symlinks so Claude Code discovers the OpenCLI skills:

```bash
mkdir -p ~/.claude/skills
for skill in $(ls ~/.claude/opencli/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/opencli/skills/$skill ~/.claude/skills/$skill
done
```

### 3. Install OpenCLI npm Package

```bash
npm install -g @jackwener/opencli
```

### 4. Install Browser Extension

OpenCLI connects to Chrome/Chromium through a Browser Bridge extension:

1. Download the latest `opencli-extension-v{version}.zip` from the [Releases page](https://github.com/jackwener/OpenCLI/releases)
2. Unzip it, open `chrome://extensions`, and enable **Developer mode**
3. Click **Load unpacked** and select the unzipped folder

### 5. Verify Installation

Restart Claude Code, then run:

```bash
opencli doctor
opencli list
```

Try asking Claude Code:
- "do you have opencli-browser?"
- "do you have opencli-explorer?"

If successful, Claude Code will automatically recognize and invoke the relevant OpenCLI skill.

## Updating

```bash
cd ~/.claude/opencli
git pull
npm update -g @jackwener/opencli
```

To refresh skills:

```bash
npx skills add jackwener/opencli
```

## Uninstallation

Remove the symlinks and repository:

```bash
for skill in $(ls ~/.claude/opencli/skills); do
  rm -rf ~/.claude/skills/$skill
done
rm -rf ~/.claude/opencli
npm uninstall -g @jackwener/opencli
```

## Getting Help

- GitHub: https://github.com/jackwener/OpenCLI
- Report issues: https://github.com/jackwener/OpenCLI/issues