# 在 OpenAgent 中安装 Reports Summary

## 前置条件

- 已安装 OpenAgent
- 已安装 Git
- 确保已安装 Python 和 pip

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 reports-summary 技能：

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/reports-summary
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/reports-summary ~/.openagent/skills/reports-summary
```

### 3. 安装 Python 依赖

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. 验证安装

重启 OpenAgent，尝试询问：
- "帮我汇总这些周报"
- "do you have reports-summary?"

如果安装成功，OpenAgent 会自动识别并调用 Reports Summary 技能工作流。

## 更新

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openagent/skills/reports-summary
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues