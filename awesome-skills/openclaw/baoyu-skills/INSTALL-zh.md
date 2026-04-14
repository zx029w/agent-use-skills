# 为 OpenClaw 安装 Baoyu Skills

## 前提条件

- 已安装 [OpenClaw](https://openclaw.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 Baoyu Skills 仓库

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.openclaw/baoyu-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenClaw 能够发现 Baoyu 技能：

```bash
mkdir -p ~/.openclaw/skills
for skill in $(ls ~/.openclaw/baoyu-skills/skills); do
  rm -rf ~/.openclaw/skills/$skill
  ln -s ~/.openclaw/baoyu-skills/skills/$skill ~/.openclaw/skills/$skill
done
```

### 3. 验证安装

重启 OpenClaw 后，尝试询问：

- "do you have baoyu-imagine?"

如果安装成功，OpenClaw 将自动识别并调用相应的 Baoyu 技能。

> **提示**：也可以通过 ClawHub 单独安装某个技能：
> ```bash
> clawhub install baoyu-imagine
> clawhub install baoyu-infographic
> ```

## 更新

```bash
cd ~/.openclaw/baoyu-skills
git pull
```

## 卸载

```bash
for skill in $(ls ~/.openclaw/baoyu-skills/skills); do
  rm -rf ~/.openclaw/skills/$skill
done
```

## 获取帮助

- GitHub: https://github.com/JimLiu/baoyu-skills
- 提交问题: https://github.com/JimLiu/baoyu-skills/issues
