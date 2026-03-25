# 在 Codex 中安装 webapp-testing

## 准备工作

- 已安装 Codex
- 已安装 Git

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/anthropics/skills.git ~/.codex/anthropics-skills
```

### 2. 创建软链接

创建软链接使 Codex 能够发现这些技能：

```bash
mkdir -p ~/.codex/skills

rm -rf ~/.codex/skills/webapp-testing
ln -s ~/.codex/anthropics-skills/skills/webapp-testing ~/.codex/skills/webapp-testing
```

### 3. 验证安装

重启 Codex，然后尝试提问：
- "do you have webapp-testing?" (你拥有 webapp-testing 技能吗？)

如果成功，Codex 将自动识别并调用该技能。

## 更新指南

```bash
cd ~/.codex/anthropics-skills
git pull
```

## 获取帮助

- GitHub: https://github.com/anthropics/skills
- 提交问题: https://github.com/anthropics/skills/issues
