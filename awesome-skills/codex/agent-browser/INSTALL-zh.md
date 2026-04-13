# 在 Codex 中安装 Agent Browser

## 前置条件

- 已安装 [Codex](https://github.com/codex-editor/codex)
- 已安装 Node.js 和 npm
- 已安装 Git

## 安装步骤

### 1. 安装核心 CLI

Agent Browser 是一个全局命令行工具，首先需要通过 npm 安装：

```bash
npm install -g agent-browser
agent-browser install --with-deps
```

### 2. 克隆 agent-browser 仓库

将技能库克隆到本地：

```bash
git clone https://github.com/vercel-labs/agent-browser.git ~/.codex/agent-browser
```

### 3. 在 Codex 中配置技能

创建符号链接，使 Codex 能够调用该技能：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/agent-browser
ln -s ~/.codex/agent-browser/skills/agent-browser ~/.codex/skills/agent-browser
```

## 验证安装

重启 Codex，尝试提问：

- "打开 google.com 并告诉我搜索框的引用 ID"
- "do you have agent-browser skill?"

## 更新

1. **更新 CLI**: `npm update -g agent-browser`
2. **更新技能库**: `cd ~/.codex/agent-browser && git pull`

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.codex/skills/agent-browser
```

## 获取帮助

- 技能逻辑问题：https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser
- CLI 工具问题：https://github.com/vercel-labs/agent-browser/issues
