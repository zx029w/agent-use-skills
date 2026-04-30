# Huashu Design - Qoder 安装指南

## 前置条件

- Qoder 已安装
- Git 已安装

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.qoder/huashu-design
```

### 2. 创建符号链接

```bash
mkdir -p ~/.qoder/skills
ln -sf ~/.qoder/huashu-design ~/.qoder/skills/huashu-design
```

### 3. 验证安装

重启 Qoder，然后尝试以下对话：

```
做个信息图，展示 AI 行业的发展趋势，印刷级质量
```

如果技能正确加载，AI 将自动识别并调用 Huashu Design 的工作流。

## 更新方法

```bash
cd ~/.qoder/huashu-design && git pull
```

## 卸载

```bash
rm ~/.qoder/skills/huashu-design
```

## 获取帮助

- GitHub 仓库：https://github.com/alchaincyf/huashu-design
- 问题反馈：https://github.com/alchaincyf/huashu-design/issues
