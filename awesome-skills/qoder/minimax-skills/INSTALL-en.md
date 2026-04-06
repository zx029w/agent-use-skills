# Installing MiniMax Skills in Qoder

## Prerequisites

- Qoder installed
- Git installed

## Installation Steps

### 1. Clone MiniMax Skills Repository

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.qoder/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.qoder\minimax-skills
```

### 2. Create Symbolic Link

**macOS / Linux:**
```bash
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/minimax-skills/skills ~/.qoder/skills/minimax-skills
```

**Windows (PowerShell, run as Administrator):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.qoder\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.qoder\skills\minimax-skills" -Target "$env:USERPROFILE\.qoder\minimax-skills\skills"
```

### 3. Restart Qoder

Restart Qoder to discover the skills.

### 4. Verify Installation

Try asking these questions to verify installation:

- "Help me build a fullstack application" (triggers `fullstack-dev`)
- "Create presentation slides" (triggers `pptx-generator`)
- "Process Excel files" (triggers `minimax-xlsx`)

If installed successfully, Qoder will automatically recognize and invoke relevant MiniMax Skills workflows.

## Updating

**macOS / Linux:**
```bash
cd ~/.qoder/minimax-skills
git pull
```

**Windows (PowerShell):**
```powershell
cd $env:USERPROFILE\.qoder\minimax-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.qoder/skills/minimax-skills
```

## Getting Help

- GitHub: https://github.com/MiniMax-AI/skills
- Issues: https://github.com/MiniMax-AI/skills/issues
