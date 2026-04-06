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
for skill in $(ls ~/.claude/minimax-skills/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/minimax-skills/skills/$skill ~/.claude/skills/$skill
done
```

**Windows (PowerShell, 以管理员身份运行):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills"
Get-ChildItem -Directory "$env:USERPROFILE\.claude\minimax-skills\skills" | ForEach-Object {
    $targetPath = "$env:USERPROFILE\.claude\skills\$($_.Name)"
    if (Test-Path $targetPath) { Remove-Item -Recurse -Force $targetPath }
    New-Item -ItemType SymbolicLink -Path $targetPath -Target $_.FullName
}
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

## 卸载

删除符号链接即可卸载：

**macOS / Linux:**
```bash
for skill in $(ls ~/.claude/minimax-skills/skills); do
  rm -rf ~/.claude/skills/$skill
done
```

**Windows (PowerShell):**
```powershell
Get-ChildItem "$env:USERPROFILE\.claude\minimax-skills\skills" | ForEach-Object { Remove-Item -Recurse -Force "$env:USERPROFILE\.claude\skills\$($_.Name)" }
```

## 获取帮助

- GitHub: https://github.com/MiniMax-AI/skills
- 提交问题: https://github.com/MiniMax-AI/skills/issues
