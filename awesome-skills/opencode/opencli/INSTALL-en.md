# Installing OpenCLI for OpenCode

## Prerequisites

- [OpenCode](https://github.com/opencode-ai/opencode) installed
- Git installed
- Node.js >= 21.0.0 (or Bun >= 1.0) installed

## Installation Steps

### 1. Clone OpenCLI Repository

```bash
git clone https://github.com/jackwener/OpenCLI.git ~/.config/opencode/opencli
```

### 2. Symlink Skills

Create symlinks so OpenCode discovers the OpenCLI skills:

```bash
mkdir -p ~/.config/opencode/skills
for skill in $(ls ~/.config/opencode/opencli/skills); do
  rm -rf ~/.config/opencode/skills/$skill
  ln -s ~/.config/opencode/opencli/skills/$skill ~/.config/opencode/skills/$skill
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

Restart OpenCode, then run:

```bash
opencli doctor
opencli list
```

Try asking OpenCode:
- "do you have opencli-browser?"
- "do you have opencli-explorer?"

If successful, OpenCode will automatically recognize and invoke the relevant OpenCLI skill.

## Updating

```bash
cd ~/.config/opencode/opencli
git pull
npm update -g @jackwener/opencli
```

## Uninstallation

Remove the symlinks and repository:

```bash
for skill in $(ls ~/.config/opencode/opencli/skills); do
  rm -rf ~/.config/opencode/skills/$skill
done
rm -rf ~/.config/opencode/opencli
npm uninstall -g @jackwener/opencli
```

## Getting Help

- GitHub: https://github.com/jackwener/OpenCLI
- Report issues: https://github.com/jackwener/OpenCLI/issues