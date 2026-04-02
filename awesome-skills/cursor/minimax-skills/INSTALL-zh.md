# 在 Cursor 中安装 MiniMax Skills

## 前置条件

- 已安装 [Cursor](https://cursor.sh)
- 已安装 Git

## 安装步骤

### 1. 克隆 MiniMax Skills 仓库

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.cursor/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.cursor\minimax-skills
```

### 2. 配置 Cursor

在 Cursor 设置中将 skills 路径指向克隆的目录：

1. 打开 Cursor 设置 (`Cmd/Ctrl + ,`)
2. 导航到 AI 相关设置
3. 设置 Skills Path 为 `~/.cursor/minimax-skills/skills/`

或者手动创建符号链接：

**macOS / Linux:**
```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/minimax-skills/skills ~/.cursor/skills/minimax-skills
```

**Windows (PowerShell, 以管理员身份运行):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.cursor\skills\minimax-skills" -Target "$env:USERPROFILE\.cursor\minimax-skills\skills"
```

### 3. 验证安装

重启 Cursor，然后尝试询问以下问题来验证是否安装成功：

- "Help me build an Android app with Material Design" (触发 `android-native-dev`)
- "Create an iOS app with SwiftUI" (触发 `ios-application-dev`)
- "Generate a PowerPoint presentation" (触发 `pptx-generator`)

如果安装成功，Cursor 会自动识别并调用相关的 MiniMax Skills 工作流。

## 更新

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

## 获取帮助

- GitHub: https://github.com/MiniMax-AI/skills
- Cursor 安装文档: https://github.com/MiniMax-AI/skills/blob/main/.cursor-plugin/INSTALL.md
- 提交问题: https://github.com/MiniMax-AI/skills/issues
