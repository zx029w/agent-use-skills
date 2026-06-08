# 在 OpenCode 中安装 Fuck-U-Code Analysis

## 前置条件

- [OpenCode](https://opencode.ai) 已安装
- [Node.js](https://nodejs.org/) >= 18.0.0 已安装
- Git 已安装

## 安装步骤

### 1. 安装 fuck-u-code CLI

```bash
npm install -g eff-u-code
```

### 2. 克隆 fuck-u-code 仓库

```bash
git clone https://github.com/Zerone-Agent/fuck-u-code.git ~/.config/opencode/fuck-u-code
```

### 3. 创建技能软链接

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/fuck-u-code-analysis
ln -s ~/.config/opencode/fuck-u-code/skills/fuck-u-code-analysis ~/.config/opencode/skills/fuck-u-code-analysis
```

### 4. 验证安装

重启 OpenCode，然后尝试提问：
- "请用 fuck-u-code 分析当前项目的代码质量"

如果安装成功，OpenCode 将自动识别并调用该技能。

## 更新

```bash
cd ~/.config/opencode/fuck-u-code
git pull
```

## 卸载

```bash
rm -rf ~/.config/opencode/skills/fuck-u-code-analysis
```

## 获取帮助

- GitHub：https://github.com/Zerone-Agent/fuck-u-code
- 问题反馈：https://github.com/Zerone-Agent/fuck-u-code/issues
