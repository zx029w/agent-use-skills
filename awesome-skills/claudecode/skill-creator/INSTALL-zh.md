# 在 Claude Code 中安装 Skill Creator

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git
- Python 3.8+（用于运行评估脚本）

## 安装步骤

### 1. 克隆 anthropics/skills 仓库

```bash
git clone https://github.com/anthropics/skills.git ~/.claude/skills-repo
```

### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现 skill-creator 技能：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/skill-creator
ln -s ~/.claude/skills-repo/skills/skill-creator ~/.claude/skills/skill-creator
```

### 3. 验证安装

重启 Claude Code，然后尝试输入以下指令来验证是否安装成功：

- "我需要创建一个新的技能，请帮我使用 skill-creator"
- "do you have skill-creator?"如果安装成功，Claude Code 会自动识别并调用 Skill Creator 技能工作流。

## 使用说明

Skill Creator 是一个用于创建和改进技能的技能，主要功能包括：

1. **创建新技能**：从零开始构建一个完整的技能
2. **改进现有技能**：迭代优化技能表现
3. **运行测试评估**：生成测试用例并评估技能效果
4. **优化技能描述**：提高技能触发准确率

## 更新

```bash
cd ~/.claude/skills-repo
git pull
```

## 获取帮助

- GitHub 仓库：https://github.com/anthropics/skills
- 提交问题：https://github.com/anthropics/skills/issues