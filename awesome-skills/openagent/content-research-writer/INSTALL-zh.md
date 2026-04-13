# 在 OpenAgent 中安装 Content Research Writer

## 前置条件

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 content-research-writer 技能：

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/content-research-writer
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/content-research-writer ~/.openagent/skills/content-research-writer
```

### 3. 验证安装

重启 OpenAgent，尝试询问：
- "帮我写一篇关于 AI 发展的博客文章"
- "do you have content-research-writer?"

如果安装成功，OpenAgent 会自动识别并调用 Content Research Writer 技能工作流。

## 更新

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openagent/skills/content-research-writer
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues