# Huashu Design - OpenCode 安装指南

## 前置条件

- [OpenCode](https://opencode.ai) 已安装
- Git 已安装

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.config/opencode/huashu-design
```

### 2. 创建符号链接

```bash
mkdir -p ~/.config/opencode/skills
ln -sf ~/.config/opencode/huashu-design ~/.config/opencode/skills/huashu-design
```

### 3. 验证安装

重启 OpenCode，然后尝试以下对话：

```
做个 AI 心理学的演讲 PPT，推荐 3 个风格方向让我选
```

如果技能正确加载，AI 将自动识别并调用 Huashu Design 的工作流。

## 更新方法

```bash
cd ~/.config/opencode/huashu-design && git pull
```

## 卸载

```bash
rm ~/.config/opencode/skills/huashu-design
```

## 获取帮助

- GitHub 仓库：https://github.com/alchaincyf/huashu-design
- 问题反馈：https://github.com/alchaincyf/huashu-design/issues
