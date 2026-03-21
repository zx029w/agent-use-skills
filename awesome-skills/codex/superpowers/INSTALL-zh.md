# 在 Codex 中安装 Superpowers

## 前置条件

- 已安装 [Codex](https://openai.com/index/codex/)
- 已安装 Git

## 安装步骤

### 1. 克隆 Superpowers 仓库

```bash
git clone https://github.com/obra/superpowers.git ~/.codex/superpowers
```

### 2. 创建符号链接

创建符号链接，使 Codex 能够发现 Superpowers 技能：

```bash
mkdir -p ~/.codex/skills

for skill in $(ls ~/.codex/superpowers/skills); do
  rm -rf ~/.codex/skills/$skill
  ln -s ~/.codex/superpowers/skills/$skill ~/.codex/skills/$skill
done
```

### 3. 验证安装

重启 Codex，然后尝试询问以下问题来验证是否安装成功：

- "Help me plan this feature" (触发 `brainstorming`)
- "Let's debug this issue" (触发 `systematic-debugging`)
- "do you have brainstorming?"

如果安装成功，Codex 会自动识别并调用相关的 Superpowers 技能工作流。

## 更新

```bash
cd ~/.codex/superpowers
git pull
```

## 获取帮助

- GitHub: https://github.com/obra/superpowers
- 提交问题: https://github.com/obra/superpowers/issues