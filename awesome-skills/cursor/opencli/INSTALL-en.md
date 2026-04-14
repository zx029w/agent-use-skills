# Installing OpenCLI for Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
- Git installed
- Node.js >= 21.0.0 (or Bun >= 1.0) installed

## Installation Steps

### 1. Clone OpenCLI Repository

```bash
git clone https://github.com/jackwener/OpenCLI.git ~/.cursor/opencli
```

### 2. Symlink Skills

Create symlinks so Cursor discovers the OpenCLI skills:

```bash
mkdir -p ~/.cursor/skills
for skill in $(ls ~/.cursor/opencli/skills); do
  rm -rf ~/.cursor/skills/$skill
  ln -s ~/.cursor/opencli/skills/$skill ~/.cursor/skills/$skill
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

Restart Cursor, then run:

```bash
opencli doctor
opencli list
```

Try asking Cursor (in Agent mode):
- "do you have opencli-browser?"
- "do you have opencli-explorer?"

If successful, Cursor will automatically recognize and invoke the relevant OpenCLI skill.

## Updating

```bash
cd ~/.cursor/opencli
git pull
npm update -g @jackwener/opencli
```

## Uninstallation

Remove the symlinks and repository:

```bash
for skill in $(ls ~/.cursor/opencli/skills); do
  rm -rf ~/.cursor/skills/$skill
done
rm -rf ~/.cursor/opencli
npm uninstall -g @jackwener/opencli
```

## Getting Help

- GitHub: https://github.com/jackwener/OpenCLI
- Report issues: https://github.com/jackwener/OpenCLI/issues