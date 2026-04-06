# 为 OpenClaw 安装 Colleague Skill

## 前置要求

- 已安装 [OpenClaw](https://github.com/openclaw/openclaw)
- 已安装 Git

## 安装步骤

### 1. 克隆 colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.openclaw/colleague-skill
```

### 2. 创建软链接

创建软链接使 OpenClaw 能够发现此技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/create-colleague
ln -s ~/.openclaw/colleague-skill ~/.openclaw/skills/create-colleague
```

### 3. 验证安装

重启 OpenClaw，然后尝试提问：
- "do you have create-colleague?"

如果成功，OpenClaw 将会自动识别并调用此技能。

## 更新指南

```bash
cd ~/.openclaw/colleague-skill
git pull
```

## 获取帮助

- GitHub：https://github.com/titanwings/colleague-skill
- 报告问题：https://github.com/titanwings/colleague-skill/issues
