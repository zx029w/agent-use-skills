# 为 Claude Code 安装 Anti-Distill

## 前置要求

- 已安装 [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)
- 已安装 Git

## 安装步骤

### 1. 克隆 anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.claude/anti-distill
```

### 2. 创建软链接

创建软链接使 Claude Code 能够发现此技能：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/anti-distill
ln -s ~/.claude/anti-distill ~/.claude/skills/anti-distill
```

### 3. 验证安装

重启 Claude Code，然后尝试提问：
- "do you have anti-distill?"

如果成功，Claude Code 将会自动识别并调用此技能。

## 更新指南

```bash
cd ~/.claude/anti-distill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.claude/skills/anti-distill
```

## 获取帮助

- GitHub：https://github.com/leilei926524-tech/anti-distill
- 报告问题：https://github.com/leilei926524-tech/anti-distill/issues
