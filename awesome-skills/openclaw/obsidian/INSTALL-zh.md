# 在 OpenClaw 中安装 Obsidian Skills

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Git

## 安装步骤

### 1. 克隆 obsidian-skills 仓库

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.openclaw/obsidian-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenClaw 能够发现所有 Obsidian 技能：

```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/obsidian-skills/skills/obsidian-markdown ~/.openclaw/skills/obsidian-markdown
ln -s ~/.openclaw/obsidian-skills/skills/obsidian-bases ~/.openclaw/skills/obsidian-bases
ln -s ~/.openclaw/obsidian-skills/skills/json-canvas ~/.openclaw/skills/json-canvas
ln -s ~/.openclaw/obsidian-skills/skills/obsidian-cli ~/.openclaw/skills/obsidian-cli
ln -s ~/.openclaw/obsidian-skills/skills/defuddle ~/.openclaw/skills/defuddle
```

### 3. 验证安装

重启 OpenClaw，然后尝试询问：

- "创建一个包含 wikilinks 的笔记：[[Another Note]]"
- "do you have obsidian-markdown skill?"

如果安装成功，OpenClaw 会自动识别并调用 Obsidian Skills。

## 更新

```bash
cd ~/.openclaw/obsidian-skills
git pull
```

## 获取帮助

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills 规范: https://agentskills.io/specification