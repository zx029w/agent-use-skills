# 在 Qoder 中安装 slidev

## 准备工作

- 已安装 Qoder
- 已安装 Git

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/slidevjs/slidev.git ~/.qoder/slidevjs-slidev
```

### 2. 创建软链接

创建软链接使 Qoder 能够发现这些技能：

```bash
mkdir -p ~/.qoder/skills

for skill in $(ls ~/.qoder/slidevjs-slidev/skills); do
  rm -rf ~/.qoder/skills/$skill
  ln -s ~/.qoder/slidevjs-slidev/skills/$skill ~/.qoder/skills/$skill
done
```

### 3. 验证安装

重启 Qoder，然后尝试提问：
- "do you have slidev?" (你拥有 slidev 技能吗？)

如果成功，Qoder 将自动识别并调用该技能。

## 更新指南

```bash
cd ~/.qoder/slidevjs-slidev
git pull
```

## 获取帮助

- GitHub: https://github.com/slidevjs/slidev
- 提交问题: https://github.com/slidevjs/slidev/issues
