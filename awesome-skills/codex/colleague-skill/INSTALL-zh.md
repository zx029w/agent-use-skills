# 为 Codex 安装 Colleague Skill

## 前置要求

- 已安装 [Codex](https://github.com/)
- 已安装 Git

## 安装步骤

### 1. 克隆 colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.codex/colleague-skill
```

### 2. 创建软链接

创建软链接使 Codex 能够发现此技能：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/create-colleague
ln -s ~/.codex/colleague-skill ~/.codex/skills/create-colleague
```

### 3. 验证安装

重启 Codex，然后尝试提问：
- "do you have create-colleague?"

如果成功，Codex 将会自动识别并调用此技能。

## 更新指南

```bash
cd ~/.codex/colleague-skill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.codex/skills/create-colleague
```

## 获取帮助

- GitHub：https://github.com/titanwings/colleague-skill
- 报告问题：https://github.com/titanwings/colleague-skill/issues
