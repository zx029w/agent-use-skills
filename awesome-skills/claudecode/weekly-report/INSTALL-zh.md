# 在 Claude Code 中安装 Weekly Report

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git
- 已安装 Python 3

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现 weekly-report 技能：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/weekly-report
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/weekly-report ~/.claude/skills/weekly-report
```

### 3. 安装 Python 依赖

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. 验证安装

重启 Claude Code，然后尝试输入以下指令来验证是否安装成功：

- "帮我生成周报"
- "写一下这周的工作"
- "do you have weekly-report skill?"

如果安装成功，Claude Code 会自动识别并调用 Weekly Report 技能的工作流。

## 更新

```bash
cd ~/.claude/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
