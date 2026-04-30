# Huashu Design - Codex 安装指南

## 前置条件

- Codex CLI 已安装
- Git 已安装

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.codex/huashu-design
```

### 2. 创建符号链接

```bash
mkdir -p ~/.codex/skills
ln -sf ~/.codex/huashu-design ~/.codex/skills/huashu-design
```

### 3. 验证安装

重启 Codex CLI，然后尝试以下对话：

```
把这段逻辑做成 60 秒动画，导出 MP4 和 GIF
```

如果技能正确加载，AI 将自动识别并调用 Huashu Design 的工作流。

## 更新方法

```bash
cd ~/.codex/huashu-design && git pull
```

## 卸载

```bash
rm ~/.codex/skills/huashu-design
```

## 获取帮助

- GitHub 仓库：https://github.com/alchaincyf/huashu-design
- 问题反馈：https://github.com/alchaincyf/huashu-design/issues
