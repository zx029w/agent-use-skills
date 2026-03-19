# 在 Codex 中安装 Obsidian Skills

## 前置条件

- 已安装 [Codex CLI](https://github.com/openai/codex)
- 已安装 Git

## 安装步骤

### 1. 克隆 obsidian-skills 仓库

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.codex/obsidian-skills
```

### 2. 创建符号链接

创建符号链接，使 Codex 能够发现所有 Obsidian 技能：

```bash
mkdir -p ~/.codex/skills
ln -s ~/.codex/obsidian-skills/skills/obsidian-markdown ~/.codex/skills/obsidian-markdown
ln -s ~/.codex/obsidian-skills/skills/obsidian-bases ~/.codex/skills/obsidian-bases
ln -s ~/.codex/obsidian-skills/skills/json-canvas ~/.codex/skills/json-canvas
ln -s ~/.codex/obsidian-skills/skills/obsidian-cli ~/.codex/skills/obsidian-cli
ln -s ~/.codex/obsidian-skills/skills/defuddle ~/.codex/skills/defuddle
```

### 3. 验证安装

重启 Codex，然后尝试询问：

- "创建一个包含 wikilinks 的笔记：[[Another Note]]"
- "do you have obsidian-markdown skill?"

如果安装成功，Codex 会自动识别并调用 Obsidian Skills。

## 更新

```bash
cd ~/.codex/obsidian-skills
git pull
```

## 获取帮助

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills 规范: https://agentskills.io/specification