# 为 Codex 安装 Anti-Distill

## 前置要求

- 已安装 [Codex](https://github.com/)
- 已安装 Git

## 安装步骤

### 1. 克隆 anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.codex/anti-distill
```

### 2. 创建软链接

创建软链接使 Codex 能够发现此技能：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/anti-distill
ln -s ~/.codex/anti-distill ~/.codex/skills/anti-distill
```

### 3. 验证安装

重启 Codex，然后尝试提问：
- "do you have anti-distill?"

如果成功，Codex 将会自动识别并调用此技能。

## 更新指南

```bash
cd ~/.codex/anti-distill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.codex/skills/anti-distill
```

## 获取帮助

- GitHub：https://github.com/leilei926524-tech/anti-distill
- 报告问题：https://github.com/leilei926524-tech/anti-distill/issues
