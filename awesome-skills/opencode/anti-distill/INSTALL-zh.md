# 为 OpenCode 安装 Anti-Distill

## 前置要求

- 已安装 [OpenCode](https://github.com/)
- 已安装 Git

## 安装步骤

### 1. 克隆 anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.config/opencode/anti-distill
```

### 2. 创建软链接

创建软链接使 OpenCode 能够发现此技能：

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/anti-distill
ln -s ~/.config/opencode/anti-distill ~/.config/opencode/skills/anti-distill
```

### 3. 验证安装

重启 OpenCode，然后尝试提问：
- "do you have anti-distill?"

如果成功，OpenCode 将会自动识别并调用此技能。

## 更新指南

```bash
cd ~/.config/opencode/anti-distill
git pull
```

## 获取帮助

- GitHub：https://github.com/leilei926524-tech/anti-distill
- 报告问题：https://github.com/leilei926524-tech/anti-distill/issues
