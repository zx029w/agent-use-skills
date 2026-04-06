# 在 OpenClaw 中安装 slidev

## 准备工作

- 已安装 OpenClaw
- 已安装 Git

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/slidevjs/slidev.git ~/.openclaw/slidevjs-slidev
```

### 2. 创建软链接

创建软链接使 OpenClaw 能够发现这些技能：

```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/slidevjs-slidev/skills ~/.openclaw/skills/slidev
```

### 3. 验证安装

重启 OpenClaw，然后尝试提问：
- "do you have slidev?" (你拥有 slidev 技能吗？)

如果成功，OpenClaw 将自动识别并调用该技能。

## 更新指南

```bash
cd ~/.openclaw/slidevjs-slidev
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openclaw/skills/slidev
```

## 获取帮助

- GitHub: https://github.com/slidevjs/slidev
- 提交问题: https://github.com/slidevjs/slidev/issues
