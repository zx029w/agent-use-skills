# 为 OpenClaw 安装 Anti-Distill

## 前置要求

- 已安装 [OpenClaw](https://github.com/openclaw/openclaw)
- 已安装 Git

## 安装步骤

### 1. 克隆 anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.openclaw/anti-distill
```

### 2. 创建软链接

创建软链接使 OpenClaw 能够发现此技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/anti-distill
ln -s ~/.openclaw/anti-distill ~/.openclaw/skills/anti-distill
```

### 3. 验证安装

重启 OpenClaw，然后尝试提问：
- "do you have anti-distill?"

如果成功，OpenClaw 将会自动识别并调用此技能。

## 更新指南

```bash
cd ~/.openclaw/anti-distill
git pull
```

## 获取帮助

- GitHub：https://github.com/leilei926524-tech/anti-distill
- 报告问题：https://github.com/leilei926524-tech/anti-distill/issues
