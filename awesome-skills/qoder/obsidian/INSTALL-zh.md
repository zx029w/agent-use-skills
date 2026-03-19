# 在 Qoder 中安装 Obsidian Skills

## 前置条件

- 已安装 [Qoder](https://qoder.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 obsidian-skills 仓库

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.qoder/obsidian-skills
```

### 2. 创建符号链接

创建符号链接，使 Qoder 能够发现所有 Obsidian 技能：

```bash
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/obsidian-skills/skills/obsidian-markdown ~/.qoder/skills/obsidian-markdown
ln -s ~/.qoder/obsidian-skills/skills/obsidian-bases ~/.qoder/skills/obsidian-bases
ln -s ~/.qoder/obsidian-skills/skills/json-canvas ~/.qoder/skills/json-canvas
ln -s ~/.qoder/obsidian-skills/skills/obsidian-cli ~/.qoder/skills/obsidian-cli
ln -s ~/.qoder/obsidian-skills/skills/defuddle ~/.qoder/skills/defuddle
```

### 3. 验证安装

重启 Qoder，然后尝试询问：

- "创建一个包含 wikilinks 的笔记：[[Another Note]]"
- "do you have obsidian-markdown skill?"

如果安装成功，Qoder 会自动识别并调用 Obsidian Skills。

## 更新

```bash
cd ~/.qoder/obsidian-skills
git pull
```

## 获取帮助

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills 规范: https://agentskills.io/specification