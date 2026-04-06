# 在 Codex 中安装 MiniMax Skills

## 前置条件

- 已安装 Codex
- 已安装 Git

## 安装步骤

### 1. 克隆 MiniMax Skills 仓库

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.codex/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.codex\minimax-skills
```

### 2. 创建符号链接

**macOS / Linux:**
```bash
mkdir -p ~/.agents/skills
ln -s ~/.codex/minimax-skills/skills ~/.agents/skills/minimax-skills
```

**Windows (PowerShell, 以管理员身份运行):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.agents\skills\minimax-skills" -Target "$env:USERPROFILE\.codex\minimax-skills\skills"
```

### 3. 重启 Codex

重启 Codex 以发现技能。

### 4. 验证安装

尝试询问以下问题来验证是否安装成功：

- "Help me develop a Flutter app" (触发 `flutter-dev`)
- "Create React Native app with Expo" (触发 `react-native-dev`)
- "Analyze this image" (触发 `vision-analysis`)

如果安装成功，Codex 会自动识别并调用相关的 MiniMax Skills 工作流。

## 更新

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

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.agents/skills/minimax-skills
```

## 获取帮助

- GitHub: https://github.com/MiniMax-AI/skills
- Codex 安装文档: https://github.com/MiniMax-AI/skills/blob/main/.codex/INSTALL.md
- 提交问题: https://github.com/MiniMax-AI/skills/issues
