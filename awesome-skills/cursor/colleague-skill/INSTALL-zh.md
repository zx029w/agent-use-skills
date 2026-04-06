# 为 Cursor 安装 Colleague Skill

## 前置要求

- 已安装 [Cursor](https://cursor.sh/)
- 已安装 Git

## 安装步骤

### 1. 克隆 colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.cursor/colleague-skill
```

### 2. 创建软链接

创建软链接使 Cursor 能够发现此技能：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/create-colleague
ln -s ~/.cursor/colleague-skill ~/.cursor/skills/create-colleague
```

### 3. 验证安装

重启 Cursor，然后尝试提问：
- "do you have create-colleague?"

如果成功，Cursor 将会自动识别并调用此技能。

## 更新指南

```bash
cd ~/.cursor/colleague-skill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.cursor/skills/create-colleague
```

## 获取帮助

- GitHub：https://github.com/titanwings/colleague-skill
- 报告问题：https://github.com/titanwings/colleague-skill/issues
