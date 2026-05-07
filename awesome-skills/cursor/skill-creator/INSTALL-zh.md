# 在 Cursor 中安装 Skill Creator

## 前置条件

- 已安装 [Cursor](https://cursor.sh)
- 已安装 Git
- Python 3.8+

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现 skill-creator 技能：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/skill-creator
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/skill-creator ~/.cursor/skills/skill-creator
```

### 3. 验证安装

重启 Cursor，然后尝试输入以下指令来验证是否安装成功：

- "我需要创建一个新的技能，请帮我使用 skill-creator"
- "do you have skill-creator?"

如果安装成功，Cursor 会自动识别并调用 Skill Creator 技能工作流。

## 更新

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.cursor/skills/skill-creator
```

## 获取帮助

- GitHub 仓库：https://github.com/Zerone-Agent/agent-use-skills
- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
