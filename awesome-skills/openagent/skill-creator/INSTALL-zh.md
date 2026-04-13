# 在 OpenAgent 中安装 Skill Creator

## 前置条件

- 已安装 OpenAgent
- 已安装 Git
- 已安装 Python

## 安装步骤

### 1. 克隆 Anthropic Skills 仓库

```bash
git clone https://github.com/anthropics/skills.git ~/.openagent/anthropic-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 skill-creator 技能：

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/skill-creator
ln -s ~/.openagent/anthropic-skills/skills/skill-creator ~/.openagent/skills/skill-creator
```

### 3. 验证安装

重启 OpenAgent，尝试询问：
- "帮我创建一个新的技能"
- "do you have skill-creator?"

如果安装成功，OpenAgent 会自动识别并调用 Skill Creator 技能工作流。

## 更新

```bash
cd ~/.openagent/anthropic-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openagent/skills/skill-creator
```

## 获取帮助

- GitHub：https://github.com/anthropics/skills