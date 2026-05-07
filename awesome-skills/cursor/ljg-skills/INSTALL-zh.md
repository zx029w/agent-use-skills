# 为 Cursor 安装 LJG Skills

## 前提条件

- 已安装 [Cursor](https://cursor.sh)
- 已安装 Git

## 安装步骤

### 1. 克隆 LJG Skills 仓库

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.cursor/ljg-skills
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现所有 LJG 技能：

```bash
mkdir -p ~/.cursor/skills
for skill in $(ls ~/.cursor/ljg-skills/skills); do
  rm -rf ~/.cursor/skills/$skill
  ln -s ~/.cursor/ljg-skills/skills/$skill ~/.cursor/skills/$skill
done
```

### 3. 安装 ljg-card 依赖（如需使用铸卡功能）

`ljg-card` 依赖 Playwright 进行截图，需额外安装：

```bash
cd ~/.cursor/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. 验证安装

重启 Cursor 后，尝试询问：

- "你有 ljg-card 吗？"
- "do you have ljg-learn?"

如果安装成功，Cursor 将自动识别并调用相应的技能。

## 更新

```bash
cd ~/.cursor/ljg-skills
git pull
```

## 卸载

```bash
for skill in $(ls ~/.cursor/ljg-skills/skills); do
  rm -rf ~/.cursor/skills/$skill
done
rm -rf ~/.cursor/ljg-skills
```

## 获取帮助

- GitHub: https://github.com/lijigang/ljg-skills
- 提交问题: https://github.com/lijigang/ljg-skills/issues
