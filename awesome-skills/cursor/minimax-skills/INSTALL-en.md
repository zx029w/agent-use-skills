# Installing MiniMax Skills in Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
- Git installed

## Installation Steps

### 1. Clone MiniMax Skills Repository

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.cursor/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.cursor\minimax-skills
```

### 2. Configure Cursor

Point the skills path to the cloned directory in Cursor settings:

1. Open Cursor settings (`Cmd/Ctrl + ,`)
2. Navigate to AI-related settings
3. Set Skills Path to `~/.cursor/minimax-skills/skills/`

Alternatively, create a symbolic link manually:

**macOS / Linux:**
```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/minimax-skills/skills ~/.cursor/skills/minimax-skills
```

**Windows (PowerShell, run as Administrator):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.cursor\skills\minimax-skills" -Target "$env:USERPROFILE\.cursor\minimax-skills\skills"
```

### 3. Verify Installation

Restart Cursor and try asking these questions to verify installation:

- "Help me build an Android app with Material Design" (triggers `android-native-dev`)
- "Create an iOS app with SwiftUI" (triggers `ios-application-dev`)
- "Generate a PowerPoint presentation" (triggers `pptx-generator`)

If installed successfully, Cursor will automatically recognize and invoke relevant MiniMax Skills workflows.

## Updating

**macOS / Linux:**
```bash
cd ~/.cursor/minimax-skills
git pull
```

**Windows (PowerShell):**
```powershell
cd $env:USERPROFILE\.cursor\minimax-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/minimax-skills
```

## Getting Help

- GitHub: https://github.com/MiniMax-AI/skills
- Cursor Installation Docs: https://github.com/MiniMax-AI/skills/blob/main/.cursor-plugin/INSTALL.md
- Issues: https://github.com/MiniMax-AI/skills/issues
