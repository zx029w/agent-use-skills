# 在 Cursor 中安装 Superpowers

## 前置条件

- 已安装 [Cursor](https://cursor.sh)
- 已安装 Git

## 安装步骤

### 1. 克隆 Superpowers 仓库

```bash
git clone https://github.com/obra/superpowers.git ~/.cursor/superpowers
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现 Superpowers 技能：

```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/superpowers/skills ~/.cursor/skills/superpowers
```

### 3. 验证安装

重启 Cursor，然后尝试询问以下问题来验证是否安装成功：

- "Help me plan this feature" (触发 `brainstorming`)
- "Let's debug this issue" (触发 `systematic-debugging`)
- "do you have brainstorming?"

如果安装成功，Cursor 会自动识别并调用相关的 Superpowers 技能工作流。

## 更新

```bash
cd ~/.cursor/superpowers
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.cursor/skills/superpowers
```

## 获取帮助

- GitHub: https://github.com/obra/superpowers
- 提交问题: https://github.com/obra/superpowers/issues
