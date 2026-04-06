# 在 OpenCode 中安装 webapp-testing

## 准备工作

- 已安装 OpenCode
- 已安装 Git

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/anthropics/skills.git ~/.config/opencode/anthropics-skills
```

### 2. 创建软链接

创建软链接使 OpenCode 能够发现这些技能：

```bash
mkdir -p ~/.config/opencode/skills

rm -rf ~/.config/opencode/skills/webapp-testing
ln -s ~/.config/opencode/anthropics-skills/skills/webapp-testing ~/.config/opencode/skills/webapp-testing
```

### 3. 验证安装

重启 OpenCode，然后尝试提问：
- "do you have webapp-testing?" (你拥有 webapp-testing 技能吗？)

如果成功，OpenCode 将自动识别并调用该技能。

## 更新指南

```bash
cd ~/.config/opencode/anthropics-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.config/opencode/skills/webapp-testing
```

## 获取帮助

- GitHub: https://github.com/anthropics/skills
- 提交问题: https://github.com/anthropics/skills/issues
