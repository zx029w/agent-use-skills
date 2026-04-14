# 在 OpenCode 中安装 OpenCLI

## 前置条件

- 已安装 [OpenCode](https://github.com/opencode-ai/opencode)
- 已安装 Git
- 已安装 Node.js >= 21.0.0（或 Bun >= 1.0）

## 安装步骤

### 1. 克隆 OpenCLI 仓库

```bash
git clone https://github.com/jackwener/OpenCLI.git ~/.config/opencode/opencli
```

### 2. 创建符号链接

创建符号链接，使 OpenCode 能够发现 OpenCLI 技能：

```bash
mkdir -p ~/.config/opencode/skills
for skill in $(ls ~/.config/opencode/opencli/skills); do
  rm -rf ~/.config/opencode/skills/$skill
  ln -s ~/.config/opencode/opencli/skills/$skill ~/.config/opencode/skills/$skill
done
```

### 3. 安装 OpenCLI npm 包

```bash
npm install -g @jackwener/opencli
```

### 4. 安装浏览器扩展

OpenCLI 通过 Browser Bridge 扩展连接 Chrome/Chromium：

1. 从 [Releases 页面](https://github.com/jackwener/OpenCLI/releases) 下载最新的 `opencli-extension-v{version}.zip`
2. 解压后，打开 `chrome://extensions`，启用 **开发者模式**
3. 点击 **加载已解压的扩展程序**，选择解压后的文件夹

### 5. 验证安装

重启 OpenCode，然后运行以下命令验证：

```bash
opencli doctor
opencli list
```

尝试询问 OpenCode：
- "do you have opencli-browser?"
- "do you have opencli-explorer?"

如果安装成功，OpenCode 会自动识别并调用相关的 OpenCLI 技能。

## 更新

```bash
cd ~/.config/opencode/opencli
git pull
npm update -g @jackwener/opencli
```

## 卸载

删除符号链接和仓库即可卸载：

```bash
for skill in $(ls ~/.config/opencode/opencli/skills); do
  rm -rf ~/.config/opencode/skills/$skill
done
rm -rf ~/.config/opencode/opencli
npm uninstall -g @jackwener/opencli
```

## 获取帮助

- GitHub: https://github.com/jackwener/OpenCLI
- 提交问题: https://github.com/jackwener/OpenCLI/issues