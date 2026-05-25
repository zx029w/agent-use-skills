# 在 OpenClaw 中安装 OfficeCLI

## 前置条件

- 已安装 OpenClaw
- 已安装 Git

## 安装步骤

### 1. 安装 OfficeCLI 二进制文件

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```

### 2. 克隆 OfficeCLI 仓库

```bash
git clone https://github.com/iOfficeAI/OfficeCLI.git ~/.openclaw/officecli
```

### 3. 创建符号链接

创建符号链接，使 OpenClaw 能够发现所有 OfficeCLI 技能：

```bash
mkdir -p ~/.openclaw/skills
for skill in $(ls ~/.openclaw/officecli/skills); do
  rm -rf ~/.openclaw/skills/$skill
  ln -s ~/.openclaw/officecli/skills/$skill ~/.openclaw/skills/$skill
done
```

这将安装全部 11 个技能：`officecli`、`officecli-docx`、`officecli-pptx`、`officecli-xlsx`、`officecli-academic-paper`、`officecli-pitch-deck`、`officecli-data-dashboard`、`officecli-financial-model`、`officecli-word-form`、`morph-ppt`、`morph-ppt-3d`。

### 4. 验证安装

重启 OpenClaw，然后尝试询问：
- "do you have officecli?"
- "创建一个 PowerPoint 演示文稿"

如果安装成功，OpenClaw 会自动识别并调用 OfficeCLI 技能。

## 更新

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
cd ~/.openclaw/officecli
git pull
```

OfficeCLI 会自动检查二进制更新。可通过 `officecli config autoUpdate false` 关闭。

## 卸载

```bash
for skill in $(ls ~/.openclaw/officecli/skills); do
  rm -rf ~/.openclaw/skills/$skill
done
rm -rf ~/.openclaw/officecli
```

## 获取帮助

- GitHub：https://github.com/iOfficeAI/OfficeCLI
- 提交问题：https://github.com/iOfficeAI/OfficeCLI/issues
