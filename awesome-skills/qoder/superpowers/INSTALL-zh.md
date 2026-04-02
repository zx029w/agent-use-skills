# 在 Qoder 中安装 Superpowers

## 前置条件

- 已安装 [Qoder](https://qoder.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 Superpowers 仓库

```bash
git clone https://github.com/obra/superpowers.git ~/.qoder/superpowers
```

### 2. 创建符号链接

创建符号链接，使 Qoder 能够发现 Superpowers 技能：

```bash
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/superpowers/skills ~/.qoder/skills/superpowers
```

### 3. 验证安装

重启 Qoder，然后尝试询问以下问题来验证是否安装成功：

- "帮我规划一个新功能" (触发 `brainstorming`)
- "让我们调试一下这个错误" (触发 `systematic-debugging`)
- "do you have brainstorming?"

如果安装成功，Qoder 会自动识别并调用相关的 Superpowers 技能工作流。

## 更新

```bash
cd ~/.qoder/superpowers
git pull
```

## 获取帮助

- GitHub: https://github.com/obra/superpowers
- 提交问题: https://github.com/obra/superpowers/issues
