# 在 Codex 中安装 OfficeCLI

## 前置条件

- 已安装 Codex CLI
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
git clone https://github.com/iOfficeAI/OfficeCLI.git ~/.codex/officecli
```

### 3. 创建符号链接

创建符号链接，使 Codex 能够发现所有 OfficeCLI 技能：

```bash
mkdir -p ~/.codex/skills
for skill in $(ls ~/.codex/officecli/skills); do
  rm -rf ~/.codex/skills/$skill
  ln -s ~/.codex/officecli/skills/$skill ~/.codex/skills/$skill
done
```

这将安装全部 11 个技能：`officecli`、`officecli-docx`、`officecli-pptx`、`officecli-xlsx`、`officecli-academic-paper`、`officecli-pitch-deck`、`officecli-data-dashboard`、`officecli-financial-model`、`officecli-word-form`、`morph-ppt`、`morph-ppt-3d`。

### 4. 验证安装

重启 Codex，然后尝试询问：
- "do you have officecli?"
- "创建一个 PowerPoint 演示文稿"

如果安装成功，Codex 会自动识别并调用 OfficeCLI 技能。

## 更新

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
cd ~/.codex/officecli
git pull
```

OfficeCLI 会自动检查二进制更新。可通过 `officecli config autoUpdate false` 关闭。

## 卸载

```bash
for skill in $(ls ~/.codex/officecli/skills); do
  rm -rf ~/.codex/skills/$skill
done
rm -rf ~/.codex/officecli
```

## 获取帮助

- GitHub：https://github.com/iOfficeAI/OfficeCLI
- 提交问题：https://github.com/iOfficeAI/OfficeCLI/issues
