# 为 OpenAgent 安装 Baoyu Skills

## 前提条件

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 克隆 Baoyu Skills 仓库

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.openagent/baoyu-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 Baoyu 技能：

```bash
mkdir -p ~/.openagent/skills
for skill in $(ls ~/.openagent/baoyu-skills/skills); do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/baoyu-skills/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. 验证安装

重启 OpenAgent 后，尝试询问：

- "do you have baoyu-imagine?"

如果安装成功，OpenAgent 将自动识别并调用相应的 Baoyu 技能。

## 更新

```bash
cd ~/.openagent/baoyu-skills
git pull
```

## 卸载

```bash
for skill in $(ls ~/.openagent/baoyu-skills/skills); do
  rm -rf ~/.openagent/skills/$skill
done
```

## 获取帮助

- GitHub: https://github.com/JimLiu/baoyu-skills
- 提交问题: https://github.com/JimLiu/baoyu-skills/issues