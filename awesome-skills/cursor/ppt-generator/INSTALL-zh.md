# 在 Cursor 中安装 PPT Generator

## 前置条件

- 已安装 [Cursor](https://cursor.com)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现 ppt-generator 技能：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/ppt-generator
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/ppt-generator ~/.cursor/skills/ppt-generator
```

### 3. 验证安装

重启 Cursor 并确保处于 **Agent** 模式，然后尝试询问：

- "帮我生成一个关于 [主题] 的演示文稿"
- "do you have ppt-generator skill?"

如果安装成功，Cursor Agent 会自动识别并调用 PPT Generator 技能。

## 更新

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.cursor/skills/ppt-generator
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
