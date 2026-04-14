# Installing OpenCLI for Codex

## Prerequisites

- Codex installed
- Git installed
- Node.js >= 21.0.0 (or Bun >= 1.0) installed

## Installation Steps

### 1. Clone OpenCLI Repository

```bash
git clone https://github.com/jackwener/OpenCLI.git ~/.codex/opencli
```

### 2. Symlink Skills

Create symlinks so Codex discovers the OpenCLI skills:

```bash
mkdir -p ~/.codex/skills
for skill in $(ls ~/.codex/opencli/skills); do
  rm -rf ~/.codex/skills/$skill
  ln -s ~/.codex/opencli/skills/$skill ~/.codex/skills/$skill
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

Restart Codex, then run:

```bash
opencli doctor
opencli list
```

Try asking Codex:
- "do you have opencli-browser?"
- "do you have opencli-explorer?"

If successful, Codex will automatically recognize and invoke the relevant OpenCLI skill.

## Updating

```bash
cd ~/.codex/opencli
git pull
npm update -g @jackwener/opencli
```

## Uninstallation

Remove the symlinks and repository:

```bash
for skill in $(ls ~/.codex/opencli/skills); do
  rm -rf ~/.codex/skills/$skill
done
rm -rf ~/.codex/opencli
npm uninstall -g @jackwener/opencli
```

## Getting Help

- GitHub: https://github.com/jackwener/OpenCLI
- Report issues: https://github.com/jackwener/OpenCLI/issues