# 在 OpenClaw 中安装 MiniMax Skills

## 前置条件

- 已安装 OpenClaw
- 已安装 Git

## 安装步骤

### 1. 克隆 MiniMax Skills 仓库

**macOS / Linux:**
```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.openclaw/minimax-skills
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/MiniMax-AI/skills.git $env:USERPROFILE\.openclaw\minimax-skills
```

### 2. 创建符号链接

**macOS / Linux:**
```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/minimax-skills/skills ~/.openclaw/skills/minimax-skills
```

**Windows (PowerShell, 以管理员身份运行):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.openclaw\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.openclaw\skills\minimax-skills" -Target "$env:USERPROFILE\.openclaw\minimax-skills\skills"
```

### 3. 重启 OpenClaw

重启 OpenClaw 以发现技能。

### 4. 验证安装

尝试询问以下问题来验证是否安装成功：

- "Help me develop mobile apps" (触发移动开发技能)
- "Create shader effects" (触发 `shader-dev`)
- "Generate multimedia content" (触发 `minimax-multimodal-toolkit`)

如果安装成功，OpenClaw 会自动识别并调用相关的 MiniMax Skills 工作流。

## 更新

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

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openclaw/skills/minimax-skills
```

## 获取帮助

- GitHub: https://github.com/MiniMax-AI/skills
- 提交问题: https://github.com/MiniMax-AI/skills/issues
