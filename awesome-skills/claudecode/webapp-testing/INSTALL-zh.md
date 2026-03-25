# 在 Claude Code 中安装 webapp-testing

## 准备工作

- 已安装 Claude Code
- 已安装 Git

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/anthropics/skills.git ~/.claude/anthropics-skills
```

### 2. 创建软链接

创建软链接使 Claude Code 能够发现这些技能：

```bash
mkdir -p ~/.claude/skills

rm -rf ~/.claude/skills/webapp-testing
ln -s ~/.claude/anthropics-skills/skills/webapp-testing ~/.claude/skills/webapp-testing
```

### 3. 验证安装

重启 Claude Code，然后尝试提问：
- "do you have webapp-testing?" (你拥有 webapp-testing 技能吗？)

如果成功，Claude Code 将自动识别并调用该技能。

## 更新指南

```bash
cd ~/.claude/anthropics-skills
git pull
```

## 获取帮助

- GitHub: https://github.com/anthropics/skills
- 提交问题: https://github.com/anthropics/skills/issues
