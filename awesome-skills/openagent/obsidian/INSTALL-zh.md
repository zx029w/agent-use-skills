# 在 OpenAgent 中安装 Obsidian Skills

## 前置条件

- 已安装 OpenAgent
- 已安装 Git
- 已安装 Node.js 和 npm

## 安装步骤

### 1. 克隆 obsidian-skills 仓库

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.openagent/obsidian-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 obsidian 技能：

```bash
mkdir -p ~/.openagent/skills
for skill in obsidian-markdown obsidian-bases json-canvas obsidian-cli defuddle; do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/obsidian-skills/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. 安装 Obsidian CLI（可选）

如果需要使用 obsidian-cli 技能：

```bash
npm install -g obsidian-cli
```

### 4. 验证安装

重启 OpenAgent，尝试询问：
- "帮我创建一个 Obsidian 笔记"
- "do you have obsidian-markdown?"

如果安装成功，OpenAgent 会自动识别并调用 Obsidian Skills 工作流。

## 更新

```bash
cd ~/.openagent/obsidian-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
for skill in obsidian-markdown obsidian-bases json-canvas obsidian-cli defuddle; do
  rm -rf ~/.openagent/skills/$skill
done
```

## 获取帮助

- GitHub：https://github.com/kepano/obsidian-skills