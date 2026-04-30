# Huashu Design - Claude Code 安装指南

## 前置条件

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 已安装
- Git 已安装

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.claude/huashu-design
```

### 2. 创建符号链接

```bash
mkdir -p ~/.claude/skills
ln -sf ~/.claude/huashu-design ~/.claude/skills/huashu-design
```

### 3. 验证安装

重启 Claude Code，然后尝试以下对话：

```
做一份 AI 心理学的演讲 PPT，推荐 3 个风格方向让我选
```

如果技能正确加载，AI 将自动识别并调用 Huashu Design 的工作流。

## 更新方法

```bash
cd ~/.claude/huashu-design && git pull
```

## 卸载

```bash
rm ~/.claude/skills/huashu-design
```

## 获取帮助

- GitHub 仓库：https://github.com/alchaincyf/huashu-design
- 问题反馈：https://github.com/alchaincyf/huashu-design/issues
