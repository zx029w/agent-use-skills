# 在 Cursor 中安装 Obsidian Skills

## 前置条件

- 已安装 [Cursor](https://cursor.com)
- 已安装 Git

## 安装步骤

### 1. 克隆 obsidian-skills 仓库

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.cursor/obsidian-skills
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现所有 Obsidian 技能：

```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/obsidian-skills/skills ~/.cursor/skills/obsidian
```

### 3. 验证安装

重启 Cursor 并确保处于 **Agent** 模式，然后尝试询问：

- "创建一个包含 wikilinks 的笔记：[[Another Note]]"
- "do you have obsidian-markdown skill?"

如果安装成功，Cursor Agent 会自动识别并调用 Obsidian Skills。

## 更新

```bash
cd ~/.cursor/obsidian-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.cursor/skills/obsidian
```

## 获取帮助

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills 规范: https://agentskills.io/specification
