# Installing MiniMax Skills in OpenClaw

## Prerequisites

- OpenClaw installed
- Git installed

## Installation Steps

### 1. Clone MiniMax Skills Repository

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.openclaw/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.openclaw\minimax-skills
```

### 2. Create Symbolic Link

**macOS / Linux:**
```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/minimax-skills/skills ~/.openclaw/skills/minimax-skills
```

**Windows (PowerShell, run as Administrator):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.openclaw\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.openclaw\skills\minimax-skills" -Target "$env:USERPROFILE\.openclaw\minimax-skills\skills"
```

### 3. Restart OpenClaw

Restart OpenClaw to discover the skills.

### 4. Verify Installation

Try asking these questions to verify installation:

- "Help me develop mobile apps" (triggers mobile development skills)
- "Create shader effects" (triggers `shader-dev`)
- "Generate multimedia content" (triggers `minimax-multimodal-toolkit`)

If installed successfully, OpenClaw will automatically recognize and invoke relevant MiniMax Skills workflows.

## Updating

**macOS / Linux:**
```bash
cd ~/.openclaw/minimax-skills
git pull
```

**Windows (PowerShell):**
```powershell
cd $env:USERPROFILE\.openclaw\minimax-skills
git pull
```

## Getting Help

- GitHub: https://github.com/MiniMax-AI/skills
- Issues: https://github.com/MiniMax-AI/skills/issues
