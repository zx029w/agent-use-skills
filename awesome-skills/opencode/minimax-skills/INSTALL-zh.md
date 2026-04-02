# 在 OpenCode 中安装 MiniMax Skills

## 前置条件

- 已安装 OpenCode
- 已安装 Git

## 安装步骤

### 1. 克隆 MiniMax Skills 仓库

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.minimax-skills
```

### 2. 创建符号链接

**macOS / Linux:**
```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.minimax-skills/skills/* ~/.config/opencode/skills/
```

**Windows (PowerShell, 以管理员身份运行):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.config\opencode\skills"
Get-ChildItem "$env:USERPROFILE\.minimax-skills\skills" | ForEach-Object {
    New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.config\opencode\skills\$($_.Name)" -Target $_.FullName
}
```

### 3. 重启 OpenCode

重启 OpenCode 以发现技能。

### 4. 验证安装

尝试询问以下问题来验证是否安装成功：

- "Help me write GLSL shaders" (触发 `shader-dev`)
- "Generate audio using MiniMax API" (触发 `minimax-multimodal-toolkit`)
- "Create an Excel spreadsheet" (触发 `minimax-xlsx`)

如果安装成功，OpenCode 会自动识别并调用相关的 MiniMax Skills 工作流。

## 更新

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

## 获取帮助

- GitHub: https://github.com/MiniMax-AI/skills
- OpenCode 安装文档: https://github.com/MiniMax-AI/skills/blob/main/.opencode/INSTALL.md
- 提交问题: https://github.com/MiniMax-AI/skills/issues
