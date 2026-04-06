# 在 Codex 中安装 Reports Summary

## 前置条件

- 已安装 Codex
- 已安装 Git
- 已安装 Python 3

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Codex 能够发现 reports-summary 技能：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/reports-summary
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/reports-summary ~/.codex/skills/reports-summary
```

### 3. 安装 Python 依赖

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. 验证安装

重启 Codex，然后尝试输入以下指令来验证是否安装成功：

- "帮我汇总一下团队的周报"
- "do you have reports-summary skill?"

如果安装成功，Codex 会自动识别并调用 Reports Summary 技能的工作流。

## 更新

```bash
cd ~/.codex/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.codex/skills/reports-summary
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
