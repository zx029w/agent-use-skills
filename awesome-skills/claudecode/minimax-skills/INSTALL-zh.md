# 在 Claude Code 中安装 MiniMax Skills

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git

## 安装步骤

### 1. 克隆 MiniMax Skills 仓库

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.claude/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.claude\minimax-skills
```

### 2. 创建符号链接

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills
ln -s ~/.claude/minimax-skills/skills ~/.claude/skills/minimax-skills
```

**Windows (PowerShell, 以管理员身份运行):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\minimax-skills" -Target "$env:USERPROFILE\.claude\minimax-skills\skills"
```

### 3. 验证安装

重启 Claude Code，然后尝试询问以下问题来验证是否安装成功：

- "Help me create a frontend app with animations" (触发 `frontend-dev`)
- "Guide me through fullstack development" (触发 `fullstack-dev`)
- "Create a PDF document from scratch" (触发 `minimax-pdf`)

如果安装成功，Claude Code 会自动识别并调用相关的 MiniMax Skills 工作流。

## 更新

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

## 获取帮助

- GitHub: https://github.com/MiniMax-AI/skills
- 提交问题: https://github.com/MiniMax-AI/skills/issues
