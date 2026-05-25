# 在 OpenCode 中安装 OfficeCLI

## 前置条件

- 已安装 [OpenCode](https://opencode.ai)
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
git clone https://github.com/iOfficeAI/OfficeCLI.git ~/.config/opencode/officecli
```

### 3. 创建符号链接

创建符号链接，使 OpenCode 能够发现所有 OfficeCLI 技能：

```bash
mkdir -p ~/.config/opencode/skills
for skill in $(ls ~/.config/opencode/officecli/skills); do
  rm -rf ~/.config/opencode/skills/$skill
  ln -s ~/.config/opencode/officecli/skills/$skill ~/.config/opencode/skills/$skill
done
```

这将安装全部 11 个技能：`officecli`、`officecli-docx`、`officecli-pptx`、`officecli-xlsx`、`officecli-academic-paper`、`officecli-pitch-deck`、`officecli-data-dashboard`、`officecli-financial-model`、`officecli-word-form`、`morph-ppt`、`morph-ppt-3d`。

### 4. 验证安装

重启 OpenCode，然后尝试询问：
- "do you have officecli?"
- "创建一个 PowerPoint 演示文稿"

如果安装成功，OpenCode 会自动识别并调用 OfficeCLI 技能。

## 更新

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
cd ~/.config/opencode/officecli
git pull
```

OfficeCLI 会自动检查二进制更新。可通过 `officecli config autoUpdate false` 关闭。

## 卸载

```bash
for skill in $(ls ~/.config/opencode/officecli/skills); do
  rm -rf ~/.config/opencode/skills/$skill
done
rm -rf ~/.config/opencode/officecli
```

## 获取帮助

- GitHub：https://github.com/iOfficeAI/OfficeCLI
- 提交问题：https://github.com/iOfficeAI/OfficeCLI/issues
