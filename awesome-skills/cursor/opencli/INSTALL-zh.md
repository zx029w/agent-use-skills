# 在 Cursor 中安装 OpenCLI

## 前置条件

- 已安装 [Cursor](https://cursor.sh)
- 已安装 Git
- 已安装 Node.js >= 21.0.0（或 Bun >= 1.0）

## 安装步骤

### 1. 克隆 OpenCLI 仓库

```bash
git clone https://github.com/jackwener/OpenCLI.git ~/.cursor/opencli
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现 OpenCLI 技能：

```bash
mkdir -p ~/.cursor/skills
for skill in $(ls ~/.cursor/opencli/skills); do
  rm -rf ~/.cursor/skills/$skill
  ln -s ~/.cursor/opencli/skills/$skill ~/.cursor/skills/$skill
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

重启 Cursor，然后运行以下命令验证：

```bash
opencli doctor
opencli list
```

尝试询问 Cursor（在 Agent 模式下）：
- "do you have opencli-browser?"
- "do you have opencli-explorer?"

如果安装成功，Cursor 会自动识别并调用相关的 OpenCLI 技能。

## 更新

```bash
cd ~/.cursor/opencli
git pull
npm update -g @jackwener/opencli
```

## 卸载

删除符号链接和仓库即可卸载：

```bash
for skill in $(ls ~/.cursor/opencli/skills); do
  rm -rf ~/.cursor/skills/$skill
done
rm -rf ~/.cursor/opencli
npm uninstall -g @jackwener/opencli
```

## 获取帮助

- GitHub: https://github.com/jackwener/OpenCLI
- 提交问题: https://github.com/jackwener/OpenCLI/issues