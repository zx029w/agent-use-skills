# 在 Claude Code 中安装 PPT Generator

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现 ppt-generator 技能：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/ppt-generator
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/ppt-generator ~/.claude/skills/ppt-generator
```

### 3. 验证安装

重启 Claude Code，然后尝试输入以下指令来验证是否安装成功：

- "帮我生成一个关于 [主题] 的演示文稿"
- "do you have ppt-generator skill?"

如果安装成功，Claude Code 会自动识别并调用 PPT Generator 技能的工作流。

## 更新

```bash
cd ~/.claude/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues