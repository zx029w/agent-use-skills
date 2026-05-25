# 在 Cursor 中安装 OfficeCLI

## 前置条件

- 已安装 [Cursor](https://cursor.sh)
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

OfficeCLI 安装时会自动检测 Cursor 并将技能文件部署到 `~/.cursor/skills/officecli/`。

如果未被自动检测到，运行：

```bash
officecli install cursor
```

### 3. 验证安装

重启 Cursor，然后在 Agent 模式下尝试询问：
- "do you have officecli?"
- "创建一个 PowerPoint 演示文稿"

如果安装成功，Cursor 会自动识别并调用 OfficeCLI 技能。

### 手动安装（可选）

如果自动安装未生效，可以手动安装技能文件：

```bash
mkdir -p ~/.cursor/skills/officecli
curl -fsSL https://officecli.ai/SKILL.md -o ~/.cursor/skills/officecli/SKILL.md
```

### MCP 服务器（可选）

将 OfficeCLI 注册为 Cursor 的 MCP 服务器：

```bash
officecli mcp cursor
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
rm -rf ~/.cursor/skills/officecli
```

## 获取帮助

- GitHub：https://github.com/iOfficeAI/OfficeCLI
- 提交问题：https://github.com/iOfficeAI/OfficeCLI/issues
