# Installing MiniMax Skills in OpenCode

## Prerequisites

- OpenCode installed
- Git installed

## Installation Steps

### 1. Clone MiniMax Skills Repository

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.minimax-skills
```

### 2. Create Symbolic Links

**macOS / Linux:**
```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.minimax-skills/skills/* ~/.config/opencode/skills/
```

**Windows (PowerShell, run as Administrator):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.config\opencode\skills"
Get-ChildItem "$env:USERPROFILE\.minimax-skills\skills" | ForEach-Object {
    New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.config\opencode\skills\$($_.Name)" -Target $_.FullName
}
```

### 3. Restart OpenCode

Restart OpenCode to discover the skills.

### 4. Verify Installation

Try asking these questions to verify installation:

- "Help me write GLSL shaders" (triggers `shader-dev`)
- "Generate audio using MiniMax API" (triggers `minimax-multimodal-toolkit`)
- "Create an Excel spreadsheet" (triggers `minimax-xlsx`)

If installed successfully, OpenCode will automatically recognize and invoke relevant MiniMax Skills workflows.

## Updating

**macOS / Linux:**
```bash
cd ~/.minimax-skills
git pull
```

**Windows (PowerShell):**
```powershell
cd $env:USERPROFILE\.minimax-skills
git pull
```

## Getting Help

- GitHub: https://github.com/MiniMax-AI/skills
- OpenCode Installation Docs: https://github.com/MiniMax-AI/skills/blob/main/.opencode/INSTALL.md
- Issues: https://github.com/MiniMax-AI/skills/issues
