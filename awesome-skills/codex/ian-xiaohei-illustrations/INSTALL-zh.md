# 在 Codex 中安装 Ian 小黑怪诞正文配图

## 前置条件

- [Codex](https://github.com/openai/codex) 已安装
- Git 已安装

## 安装步骤

### 1. 克隆 ian-xiaohei-illustrations 仓库

```bash
git clone https://github.com/helloianneo/ian-xiaohei-illustrations.git ~/.codex/ian-xiaohei-illustrations
```

### 2. 复制 skill 到 Codex skills 目录

该仓库的有效 skill 内容位于子目录 `ian-xiaohei-illustrations/` 下，需要将其复制到 Codex 的 skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R ~/.codex/ian-xiaohei-illustrations/ian-xiaohei-illustrations ~/.codex/skills/ian-xiaohei-illustrations
```

### 3. 验证安装

重启 Codex，然后尝试询问：
- “Use $ian-xiaohei-illustrations 为这篇文章生成 4 张小黑怪诞正文配图。”
- “请分析这篇文章哪里值得配图。”

如果安装成功，Codex 会自动识别并调用该 skill。

## 更新

```bash
cd ~/.codex/ian-xiaohei-illustrations
git pull
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/ian-xiaohei-illustrations
cp -R ./ian-xiaohei-illustrations ~/.codex/skills/ian-xiaohei-illustrations
```

## 卸载

```bash
rm -rf ~/.codex/skills/ian-xiaohei-illustrations
rm -rf ~/.codex/ian-xiaohei-illustrations
```

## 获取帮助

- GitHub: https://github.com/helloianneo/ian-xiaohei-illustrations
- 提交问题: https://github.com/helloianneo/ian-xiaohei-illustrations/issues
