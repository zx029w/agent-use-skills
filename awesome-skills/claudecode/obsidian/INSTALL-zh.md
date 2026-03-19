# Obsidian Skills 安装指南 (Claude Code)

本指南介绍如何在 Claude Code 中安装和配置 Obsidian Skills。

## 安装方法

### 方法一：通过 Marketplace 安装（推荐）

在 Claude Code 中执行以下命令：

```bash
/plugin marketplace add kepano/obsidian-skills
/plugin install obsidian@obsidian-skills
```

### 方法二：使用 npx 安装

```bash
npx skills add git@github.com:kepano/obsidian-skills.git
```

### 方法三：手动安装

1. 克隆仓库到本地：

```bash
git clone https://github.com/kepano/obsidian-skills.git
```

2. 将仓库内容复制到你的 Obsidian Vault 根目录下的 `/.claude` 文件夹中：

```bash
cp -r obsidian-skills/* /path/to/your/vault/.claude/
```

或者创建符号链接（推荐，便于更新）：

```bash
ln -s /path/to/obsidian-skills /path/to/your/vault/.claude
```

## 验证安装

安装完成后，重启 Claude Code 并测试以下功能：

1. **测试 Markdown 技能**：
   - 尝试创建包含 wikilinks 的笔记：`[[Another Note]]`
   - 测试 callouts：使用 `> [!note]` 语法

2. **测试 Bases 技能**：
   - 创建一个 `.base` 文件
   - 定义视图和过滤器

3. **测试 Canvas 技能**：
   - 创建一个 `.canvas` 文件
   - 添加节点和边

4. **测试 CLI 技能**：
   - 运行 `obsidian help` 查看可用命令

## 更新方法

### 通过 Marketplace 更新

```bash
/plugin update obsidian@obsidian-skills
```

### 手动更新

如果通过 git 克隆安装：

```bash
cd /path/to/obsidian-skills
git pull
```

如果使用了符号链接，更新会自动同步到 Claude Code。

## 详细文档

- [Claude Code 官方 Skills 文档](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Obsidian Skills GitHub](https://github.com/kepano/obsidian-skills)
- [Agent Skills 规范](https://agentskills.io/specification)
