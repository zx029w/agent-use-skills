# 为 OpenCode 安装 LJG Skills

## 前提条件

- 已安装 [OpenCode](https://opencode.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 LJG Skills 仓库

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.config/opencode/ljg-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenCode 能够发现所有 LJG 技能：

```bash
mkdir -p ~/.config/opencode/skills
for skill in $(ls ~/.config/opencode/ljg-skills/skills); do
  rm -rf ~/.config/opencode/skills/$skill
  ln -s ~/.config/opencode/ljg-skills/skills/$skill ~/.config/opencode/skills/$skill
done
```

### 3. 安装 ljg-card 依赖（如需使用铸卡功能）

`ljg-card` 依赖 Playwright 进行截图，需额外安装：

```bash
cd ~/.config/opencode/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. 验证安装

重启 OpenCode 后，尝试询问：

- "你有 ljg-card 吗？"
- "do you have ljg-learn?"

如果安装成功，OpenCode 将自动识别并调用相应的技能。

## 更新

```bash
cd ~/.config/opencode/ljg-skills
git pull
```

## 卸载

```bash
for skill in $(ls ~/.config/opencode/ljg-skills/skills); do
  rm -rf ~/.config/opencode/skills/$skill
done
rm -rf ~/.config/opencode/ljg-skills
```

## 获取帮助

- GitHub: https://github.com/lijigang/ljg-skills
- 提交问题: https://github.com/lijigang/ljg-skills/issues
