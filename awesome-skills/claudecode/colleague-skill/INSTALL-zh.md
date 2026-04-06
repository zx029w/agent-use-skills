# 为 Claude Code 安装 Colleague Skill

## 前置要求

- 已安装 [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)
- 已安装 Git

## 安装步骤

### 1. 克隆 colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.claude/colleague-skill
```

### 2. 创建软链接

创建软链接使 Claude Code 能够发现此技能：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/create-colleague
ln -s ~/.claude/colleague-skill ~/.claude/skills/create-colleague
```

### 3. 验证安装

重启 Claude Code，然后尝试提问：
- "do you have create-colleague?"

如果成功，Claude Code 将会自动识别并调用此技能。

## 更新指南

```bash
cd ~/.claude/colleague-skill
git pull
```

## 获取帮助

- GitHub：https://github.com/titanwings/colleague-skill
- 报告问题：https://github.com/titanwings/colleague-skill/issues
