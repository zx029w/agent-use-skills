# 为 OpenClaw 安装 LJG Skills

## 前提条件

- 已安装 OpenClaw
- 已安装 Git

## 安装步骤

### 1. 克隆 LJG Skills 仓库

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.openclaw/ljg-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenClaw 能够发现所有 LJG 技能：

```bash
mkdir -p ~/.openclaw/skills
for skill in $(ls ~/.openclaw/ljg-skills/skills); do
  rm -rf ~/.openclaw/skills/$skill
  ln -s ~/.openclaw/ljg-skills/skills/$skill ~/.openclaw/skills/$skill
done
```

### 3. 安装 ljg-card 依赖（如需使用铸卡功能）

`ljg-card` 依赖 Playwright 进行截图，需额外安装：

```bash
cd ~/.openclaw/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. 验证安装

重启 OpenClaw 后，尝试询问：

- "你有 ljg-card 吗？"
- "do you have ljg-learn?"

如果安装成功，OpenClaw 将自动识别并调用相应的技能。

## 更新

```bash
cd ~/.openclaw/ljg-skills
git pull
```

## 卸载

```bash
for skill in $(ls ~/.openclaw/ljg-skills/skills); do
  rm -rf ~/.openclaw/skills/$skill
done
rm -rf ~/.openclaw/ljg-skills
```

## 获取帮助

- GitHub: https://github.com/lijigang/ljg-skills
- 提交问题: https://github.com/lijigang/ljg-skills/issues
