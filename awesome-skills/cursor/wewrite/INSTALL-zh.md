# 在 Cursor 中安装 WeWrite

## 前置要求

- 已安装 [Cursor](https://cursor.sh)
- 已安装 Git
- 已安装 Python 3

## 安装步骤

### 1. 克隆 WeWrite 仓库

```bash
git clone --depth 1 https://github.com/oaker-io/wewrite.git ~/.cursor/wewrite
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现该技能：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/wewrite
ln -s ~/.cursor/wewrite ~/.cursor/skills/wewrite
```

### 3. 安装 Python 依赖

```bash
cd ~/.cursor/wewrite && pip install -r requirements.txt
```

### 4. 验证安装

重启 Cursor，然后尝试询问：
- "你有 wewrite 吗？"
- "写一篇公众号文章"

如果安装成功，Cursor 将自动识别并调用 WeWrite 技能。

## 配置（可选）

如需启用微信公众号草稿箱推送和 AI 配图功能，请创建配置文件：

```bash
cd ~/.cursor/wewrite
cp config.example.yaml config.yaml
```

编辑 `config.yaml` 填入：
- 微信公众号 `appid` 和 `secret`（用于推送草稿箱）
- 图片 API key（用于生成配图）

> **注意**：不配置也能使用核心功能——系统会自动降级为本地 HTML 预览 + 输出图片提示词。

## 更新

```bash
cd ~/.cursor/wewrite
git pull origin main
```

WeWrite 会在每次运行时自动检查新版本。有更新时说"更新"即可升级。

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.cursor/skills/wewrite
```

## 快速开始

```
你：写一篇公众号文章
你：写一篇关于 AI Agent 的公众号文章
你：交互模式，写一篇关于效率工具的推文
你：看看有什么主题                → 主题画廊
你：换成 sspai 主题               → 切换主题
你：导入范文                      → 建立风格库
你：学习我的修改                  → 飞轮学习
```

## 获取帮助

- GitHub: https://github.com/oaker-io/wewrite
- 问题反馈: https://github.com/oaker-io/wewrite/issues
