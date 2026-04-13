# 在 OpenAgent 中安装 Colleague Skill

## 前置条件

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 克隆 colleague-skill 仓库

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.openagent/colleague-skill
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 colleague-skill 技能：

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/colleague-skill
ln -s ~/.openagent/colleague-skill/skills/colleague-skill ~/.openagent/skills/colleague-skill
```

### 3. 验证安装

重启 OpenAgent，尝试询问：
- "帮我创建一个同事数字人"
- "do you have colleague-skill?"

如果安装成功，OpenAgent 会自动识别并调用 Colleague Skill 工作流。

## 更新

```bash
cd ~/.openagent/colleague-skill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openagent/skills/colleague-skill
```

## 获取帮助

- GitHub：https://github.com/titanwings/colleague-skill