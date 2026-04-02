# Installing MiniMax Skills in Codex

## Prerequisites

- Codex installed
- Git installed

## Installation Steps

### 1. Clone MiniMax Skills Repository

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.codex/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.codex\minimax-skills
```

### 2. Create Symbolic Link

**macOS / Linux:**
```bash
mkdir -p ~/.agents/skills
ln -s ~/.codex/minimax-skills/skills ~/.agents/skills/minimax-skills
```

**Windows (PowerShell, run as Administrator):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.agents\skills\minimax-skills" -Target "$env:USERPROFILE\.codex\minimax-skills\skills"
```

### 3. Restart Codex

Restart Codex to discover the skills.

### 4. Verify Installation

Try asking these questions to verify installation:

- "Help me develop a Flutter app" (triggers `flutter-dev`)
- "Create React Native app with Expo" (triggers `react-native-dev`)
- "Analyze this image" (triggers `vision-analysis`)

If installed successfully, Codex will automatically recognize and invoke relevant MiniMax Skills workflows.

## Updating

**macOS / Linux:**
```bash
cd ~/.codex/minimax-skills
git pull
```

**Windows (PowerShell):**
```powershell
cd $env:USERPROFILE\.codex\minimax-skills
git pull
```

## Getting Help

- GitHub: https://github.com/MiniMax-AI/skills
- Codex Installation Docs: https://github.com/MiniMax-AI/skills/blob/main/.codex/INSTALL.md
- Issues: https://github.com/MiniMax-AI/skills/issues
