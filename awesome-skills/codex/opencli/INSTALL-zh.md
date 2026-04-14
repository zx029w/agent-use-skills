# 在 Codex 中安装 OpenCLI

## 前置条件

- 已安装 Codex
- 已安装 Git
- 已安装 Node.js >= 21.0.0（或 Bun >= 1.0）

## 安装步骤

### 1. 克隆 OpenCLI 仓库

```bash
git clone https://github.com/jackwener/OpenCLI.git ~/.codex/opencli
```

### 2. 创建符号链接

创建符号链接，使 Codex 能够发现 OpenCLI 技能：

```bash
mkdir -p ~/.codex/skills
for skill in $(ls ~/.codex/opencli/skills); do
  rm -rf ~/.codex/skills/$skill
  ln -s ~/.codex/opencli/skills/$skill ~/.codex/skills/$skill
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

重启 Codex，然后运行以下命令验证：

```bash
opencli doctor
opencli list
```

尝试询问 Codex：
- "do you have opencli-browser?"
- "do you have opencli-explorer?"

如果安装成功，Codex 会自动识别并调用相关的 OpenCLI 技能。

## 更新

```bash
cd ~/.codex/opencli
git pull
npm update -g @jackwener/opencli
```

## 卸载

删除符号链接和仓库即可卸载：

```bash
for skill in $(ls ~/.codex/opencli/skills); do
  rm -rf ~/.codex/skills/$skill
done
rm -rf ~/.codex/opencli
npm uninstall -g @jackwener/opencli
```

## 获取帮助

- GitHub: https://github.com/jackwener/OpenCLI
- 提交问题: https://github.com/jackwener/OpenCLI/issues