# 为 Claude Code 安装 LJG Skills

## 前提条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Node.js（用于 `npx` 命令）
- 已安装 Git

## 安装步骤

### 方式一：通过 npx 快速安装（推荐）

```bash
npx skills add lijigang/ljg-skills -g --all
```

如需 Markdown 格式版本（适用于 Obsidian / VSCode / Notion 等）：

```bash
npx skills add lijigang/ljg-skills#md -g --all
```

安装单个技能：

```bash
npx skills add lijigang/ljg-skills -g --skill ljg-card
```

### 方式二：通过 Git 手动安装

#### 1. 克隆 LJG Skills 仓库

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.claude/ljg-skills
```

#### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现所有 LJG 技能：

```bash
mkdir -p ~/.claude/skills
for skill in $(ls ~/.claude/ljg-skills/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/ljg-skills/skills/$skill ~/.claude/skills/$skill
done
```

### 3. 安装 ljg-card 依赖（如需使用铸卡功能）

`ljg-card` 依赖 Playwright 进行截图，需额外安装：

```bash
cd ~/.claude/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. 验证安装

重启 Claude Code 后，尝试询问：

- "你有 ljg-card 吗？"
- "do you have ljg-learn?"

如果安装成功，Claude Code 将自动识别并调用相应的技能。

## 更新

### npx 方式

```bash
npx skills add lijigang/ljg-skills -g --all
```

### Git 方式

```bash
cd ~/.claude/ljg-skills
git pull
```

## 卸载

### npx 方式

```bash
npx skills remove lijigang/ljg-skills -g --all
```

### Git 方式

```bash
for skill in $(ls ~/.claude/ljg-skills/skills); do
  rm -rf ~/.claude/skills/$skill
done
rm -rf ~/.claude/ljg-skills
```

## 获取帮助

- GitHub: https://github.com/lijigang/ljg-skills
- 提交问题: https://github.com/lijigang/ljg-skills/issues
