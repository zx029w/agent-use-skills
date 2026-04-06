# 在 Claude Code 中安装 Obsidian Skills

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git

## 安装步骤

### 1. 克隆 obsidian-skills 仓库

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.claude/obsidian-skills
```

### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现所有 Obsidian 技能：

```bash
mkdir -p ~/.claude/skills
ln -s ~/.claude/obsidian-skills ~/.claude/skills/obsidian-skills
```

### 3. 验证安装

重启 Claude Code，然后尝试询问以下问题来验证是否安装成功：

- "Create a note with wikilinks: [[Another Note]]"
- "do you have obsidian-markdown skill?"

如果安装成功，Claude Code 会自动识别并调用 Obsidian Skills。

## 更新

```bash
cd ~/.claude/obsidian-skills
git pull
```

## 获取帮助

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills 规范: https://agentskills.io/specification