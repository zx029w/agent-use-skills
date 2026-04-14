# 为 OpenCode 安装 Baoyu Skills

## 前提条件

- 已安装 [OpenCode](https://opencode.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 Baoyu Skills 仓库

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.config/opencode/baoyu-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenCode 能够发现 Baoyu 技能：

```bash
mkdir -p ~/.config/opencode/skills
for skill in $(ls ~/.config/opencode/baoyu-skills/skills); do
  rm -rf ~/.config/opencode/skills/$skill
  ln -s ~/.config/opencode/baoyu-skills/skills/$skill ~/.config/opencode/skills/$skill
done
```

### 3. 验证安装

重启 OpenCode 后，尝试询问：

- "do you have baoyu-imagine?"

如果安装成功，OpenCode 将自动识别并调用相应的 Baoyu 技能。

## 更新

```bash
cd ~/.config/opencode/baoyu-skills
git pull
```

## 卸载

```bash
for skill in $(ls ~/.config/opencode/baoyu-skills/skills); do
  rm -rf ~/.config/opencode/skills/$skill
done
```

## 获取帮助

- GitHub: https://github.com/JimLiu/baoyu-skills
- 提交问题: https://github.com/JimLiu/baoyu-skills/issues
