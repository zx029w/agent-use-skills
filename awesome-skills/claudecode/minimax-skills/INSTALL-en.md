# Installing MiniMax Skills in Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone MiniMax Skills Repository

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.claude/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.claude\minimax-skills
```

### 2. Create Symbolic Link

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills
ln -s ~/.claude/minimax-skills/skills ~/.claude/skills/minimax-skills
```

**Windows (PowerShell, run as Administrator):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\minimax-skills" -Target "$env:USERPROFILE\.claude\minimax-skills\skills"
```

### 3. Verify Installation

Restart Claude Code and try asking these questions to verify installation:

- "Help me create a frontend app with animations" (triggers `frontend-dev`)
- "Guide me through fullstack development" (triggers `fullstack-dev`)
- "Create a PDF document from scratch" (triggers `minimax-pdf`)

If installed successfully, Claude Code will automatically recognize and invoke relevant MiniMax Skills workflows.

## Updating

**macOS / Linux:**
```bash
cd ~/.claude/minimax-skills
git pull
```

**Windows (PowerShell):**
```powershell
cd $env:USERPROFILE\.claude\minimax-skills
git pull
```

## Getting Help

- GitHub: https://github.com/MiniMax-AI/skills
- Issues: https://github.com/MiniMax-AI/skills/issues
