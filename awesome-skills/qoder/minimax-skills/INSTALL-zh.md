# 在 Qoder 中安装 MiniMax Skills

## 前置条件

- 已安装 Qoder
- 已安装 Git

## 安装步骤

### 1. 克隆 MiniMax Skills 仓库

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.qoder/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.qoder\minimax-skills
```

### 2. 创建符号链接

**macOS / Linux:**
```bash
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/minimax-skills/skills ~/.qoder/skills/minimax-skills
```

**Windows (PowerShell, 以管理员身份运行):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.qoder\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.qoder\skills\minimax-skills" -Target "$env:USERPROFILE\.qoder\minimax-skills\skills"
```

### 3. 重启 Qoder

重启 Qoder 以发现技能。

### 4. 验证安装

尝试询问以下问题来验证是否安装成功：

- "Help me build a fullstack application" (触发 `fullstack-dev`)
- "Create presentation slides" (触发 `pptx-generator`)
- "Process Excel files" (触发 `minimax-xlsx`)

如果安装成功，Qoder 会自动识别并调用相关的 MiniMax Skills 工作流。

## 更新

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

## 获取帮助

- GitHub: https://github.com/MiniMax-AI/skills
- 提交问题: https://github.com/MiniMax-AI/skills/issues
