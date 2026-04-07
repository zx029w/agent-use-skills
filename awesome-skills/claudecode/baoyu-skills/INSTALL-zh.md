# 为 Claude Code 安装 Baoyu Skills

## 前提条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Node.js（用于 `npx` 命令）
- 已安装 Git

## 安装步骤

### 方式一：通过 npx 快速安装（推荐）

```bash
npx skills add jimliu/baoyu-skills
```

### 方式二：通过 Git 手动安装

#### 1. 克隆 Baoyu Skills 仓库

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.claude/baoyu-skills
```

#### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现所有 Baoyu 技能：

```bash
mkdir -p ~/.claude/skills
for skill in $(ls ~/.claude/baoyu-skills/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/baoyu-skills/skills/$skill ~/.claude/skills/$skill
done
```

### 3. 验证安装

重启 Claude Code 后，尝试询问：

- "你有 baoyu-imagine 吗？"
- "do you have baoyu-infographic?"

如果安装成功，Claude Code 将自动识别并调用相应的 Baoyu 技能。

## 更新

```bash
cd ~/.claude/baoyu-skills
git pull
```

## 卸载

```bash
for skill in $(ls ~/.claude/baoyu-skills/skills); do
  rm -rf ~/.claude/skills/$skill
done
```

## 获取帮助

- GitHub: https://github.com/JimLiu/baoyu-skills
- 提交问题: https://github.com/JimLiu/baoyu-skills/issues
