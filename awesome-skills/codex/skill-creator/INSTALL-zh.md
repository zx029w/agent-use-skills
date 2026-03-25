# 在 Codex 中安装 Skill Creator

## 前置条件

- 已安装 [Codex](https://github.com/openai/codex)
- 已安装 Git
- Python 3.8+

## 安装步骤

### 1. 克隆 anthropics/skills 仓库

```bash
git clone https://github.com/anthropics/skills.git ~/.codex/anthropics-skills
```

### 2. 创建符号链接

创建符号链接，使 Codex 能够发现 skill-creator 技能：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/skill-creator
ln -s ~/.codex/anthropics-skills/skills/skill-creator ~/.codex/skills/skill-creator
```

### 3. 验证安装

重启 Codex，然后尝试输入以下指令来验证是否安装成功：

- "我需要创建一个新的技能，请帮我使用 skill-creator"
- "do you have skill-creator?"

如果安装成功，Codex 会自动识别并调用 Skill Creator 技能工作流。

## 更新

```bash
cd ~/.codex/anthropics-skills
git pull
```

## 获取帮助

- GitHub 仓库：https://github.com/anthropics/skills
- 提交问题：https://github.com/anthropics/skills/issues