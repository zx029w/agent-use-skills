# 在 OpenAgent 中安装 OfficeCLI

## 前置条件

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 安装 OfficeCLI 二进制文件

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```

### 2. 安装技能

将 OfficeCLI 技能文件下载到 OpenAgent 的技能目录：

```bash
mkdir -p ~/.openagent/skills/officecli
curl -fsSL https://officecli.ai/SKILL.md -o ~/.openagent/skills/officecli/SKILL.md
```

### 3. 验证安装

重启 OpenAgent，然后尝试询问：
- "do you have officecli?"
- "创建一个 PowerPoint 演示文稿"

如果安装成功，OpenAgent 会自动识别并调用 OfficeCLI 技能。

## 更新

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
curl -fsSL https://officecli.ai/SKILL.md -o ~/.openagent/skills/officecli/SKILL.md
```

OfficeCLI 会自动检查更新。可通过 `officecli config autoUpdate false` 关闭。

## 卸载

```bash
rm -rf ~/.openagent/skills/officecli
```

## 获取帮助

- GitHub：https://github.com/iOfficeAI/OfficeCLI
- 提交问题：https://github.com/iOfficeAI/OfficeCLI/issues
