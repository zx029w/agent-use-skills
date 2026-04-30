# Huashu Design - OpenClaw 安装指南

## 前置条件

- OpenClaw 已安装
- Git 已安装

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.openclaw/huashu-design
```

### 2. 创建符号链接

```bash
mkdir -p ~/.openclaw/skills
ln -sf ~/.openclaw/huashu-design ~/.openclaw/skills/huashu-design
```

### 3. 验证安装

重启 OpenClaw，然后尝试以下对话：

```
做个 AI 番茄钟 iOS 原型，4 个核心屏幕要真能点击
```

如果技能正确加载，AI 将自动识别并调用 Huashu Design 的工作流。

## 更新方法

```bash
cd ~/.openclaw/huashu-design && git pull
```

## 卸载

```bash
rm ~/.openclaw/skills/huashu-design
```

## 获取帮助

- GitHub 仓库：https://github.com/alchaincyf/huashu-design
- 问题反馈：https://github.com/alchaincyf/huashu-design/issues
