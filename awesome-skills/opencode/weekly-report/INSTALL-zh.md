# 在 OpenCode 中安装 Weekly Report

## 前置条件

- 已安装 [OpenCode](https://github.com/opencode-ai)
- 已安装 Git
- 已安装 Python 3

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/agent-use-skills
```

### 2. 配置 OpenCode

在 OpenCode 中，通过设置将技能目录添加到工作区：

1. 打开 OpenCode 设置
2. 找到 "Skills" 或 "Custom Skills" 选项
3. 添加技能路径：`~/agent-use-skills/awesome-skills/skills/weekly-report`

或者，将技能文件复制到 OpenCode 的技能目录：

```bash
# 假设 OpenCode 技能目录为 ~/.config/opencode/skills
mkdir -p ~/.config/opencode/skills
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.config/opencode/skills/
```

### 3. 安装 Python 依赖

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. 验证安装

重启 OpenCode，然后尝试输入以下指令来验证是否安装成功：

- "帮我生成周报"
- "写一下这周的工作"

如果安装成功，OpenCode 会自动识别并调用 Weekly Report 技能的工作流。

## 更新

```bash
cd ~/agent-use-skills
git pull
# 重新复制到 OpenCode 技能目录
cp -r ~/agent-use-skills/awesome-skills/skills/weekly-report ~/.config/opencode/skills/
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.config/opencode/skills/weekly-report
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
