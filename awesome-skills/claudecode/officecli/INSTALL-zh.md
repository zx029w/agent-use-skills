# 在 Claude Code 中安装 OfficeCLI

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git

## 安装步骤

### 1. 安装 OfficeCLI 二进制文件

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```

### 2. 自动安装技能

OfficeCLI 安装时会自动检测 Claude Code 并将技能文件部署到 `~/.claude/skills/officecli/`。

如果未被自动检测到，运行：

```bash
officecli install claude
```

### 3. 验证安装

重启 Claude Code，然后尝试询问：
- "do you have officecli?"
- "创建一个 PowerPoint 演示文稿"

如果安装成功，Claude Code 会自动识别并调用 OfficeCLI 技能。

### 手动安装（可选）

如果自动安装未生效，可以手动安装技能文件：

```bash
mkdir -p ~/.claude/skills/officecli
curl -fsSL https://officecli.ai/SKILL.md -o ~/.claude/skills/officecli/SKILL.md
```

### MCP 服务器（可选）

将 OfficeCLI 注册为 Claude Code 的 MCP 服务器：

```bash
officecli mcp claude
```

检查注册状态：

```bash
officecli mcp list
```

## 更新

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
```

OfficeCLI 会自动检查更新。可通过 `officecli config autoUpdate false` 关闭。

## 卸载

```bash
rm -rf ~/.claude/skills/officecli
```

## 获取帮助

- GitHub：https://github.com/iOfficeAI/OfficeCLI
- 提交问题：https://github.com/iOfficeAI/OfficeCLI/issues
