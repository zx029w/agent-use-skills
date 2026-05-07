# 为 OpenAgent 安装 LJG Skills

## 前提条件

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 克隆 LJG Skills 仓库

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.openagent/ljg-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现所有 LJG 技能：

```bash
mkdir -p ~/.openagent/skills
for skill in $(ls ~/.openagent/ljg-skills/skills); do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/ljg-skills/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. 安装 ljg-card 依赖（如需使用铸卡功能）

`ljg-card` 依赖 Playwright 进行截图，需额外安装：

```bash
cd ~/.openagent/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. 验证安装

重启 OpenAgent 后，尝试询问：

- "你有 ljg-card 吗？"
- "do you have ljg-learn?"

如果安装成功，OpenAgent 将自动识别并调用相应的技能。

## 更新

```bash
cd ~/.openagent/ljg-skills
git pull
```

## 卸载

```bash
for skill in $(ls ~/.openagent/ljg-skills/skills); do
  rm -rf ~/.openagent/skills/$skill
done
rm -rf ~/.openagent/ljg-skills
```

## 获取帮助

- GitHub: https://github.com/lijigang/ljg-skills
- 提交问题: https://github.com/lijigang/ljg-skills/issues
