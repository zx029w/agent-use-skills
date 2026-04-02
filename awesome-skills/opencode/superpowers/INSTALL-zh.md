# 在 OpenCode 中安装 Superpowers

## 前置条件

- 已安装 [OpenCode.ai](https://opencode.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 Superpowers 仓库

```bash
git clone https://github.com/obra/superpowers.git ~/.config/opencode/superpowers
```

### 2. 创建符号链接

创建符号链接，使 OpenCode 的原生技能工具能够发现 Superpowers 技能：

```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/superpowers/skills ~/.config/opencode/skills/superpowers
```

### 3. 验证安装

重启 OpenCode，然后尝试询问以下问题来验证是否安装成功：

- "Help me plan this feature" (触发 `brainstorming`)
- "Let's debug this issue" (触发 `systematic-debugging`)
- "do you have brainstorming?"

如果安装成功，OpenCode 会自动识别并调用相关的 Superpowers 技能工作流。

## 更新

```bash
cd ~/.config/opencode/superpowers
git pull
```

## 获取帮助

- GitHub: https://github.com/obra/superpowers
- 提交问题: https://github.com/obra/superpowers/issues