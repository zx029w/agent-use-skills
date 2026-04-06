# PUA 技能 - Cursor 安装指南

本指南介绍如何在 Cursor 中安装和配置 PUA 技能。

## 安装方式

Cursor 使用 `.mdc` 规则文件（Markdown + YAML 前置信息）。PUA 规则通过 AI 语义匹配自动触发（Agent Discretion 模式）。

### 项目级安装（推荐）

```bash
# 创建规则目录
mkdir -p .cursor/rules

# 下载中文版规则
curl -o .cursor/rules/pua.mdc \
  https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua.mdc

# 如需英文版（PIP Edition）
curl -o .cursor/rules/pua-en.mdc \
  https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua-en.mdc

# 如需日文版
curl -o .cursor/rules/pua-ja.mdc \
  https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua-ja.mdc
```

## 语言版本选择

| 语言 | 文件名 | 说明 |
|-----|-------|-----|
| 中文 | `pua.mdc` | 中国大厂 PUA 文化 |
| 英文 | `pua-en.mdc` | 西方科技公司 PIP 话术 |
| 日文 | `pua-ja.mdc` | 日语本地化版本 |

## 验证安装

安装完成后：

1. **重启 Cursor** 确保规则文件被加载
2. **检查 Agent 模式** - 确保在 Agent Discretion 模式下工作
3. **测试触发** - 尝试执行一个会失败的调试任务，观察 AI 是否展现 PUA 话术

## 使用方法

### 自动触发

在 Cursor 的 Agent 模式下，PUA 技能会自动通过语义匹配触发：
- 检测到放弃倾向
- 连续失败 2 次以上
- 使用推卸责任的表达方式

### 手动激活

由于 Cursor 不支持 `/pua` 命令，你可以：
- 在对话中明确说"使用 PUA 模式"
- 复制 PUA 规则的关键提示词到对话中

## 升级方法

```bash
# 删除旧版本
rm .cursor/rules/pua*.mdc

# 重新下载最新版本
curl -o .cursor/rules/pua.mdc \
  https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua.mdc
```

## 注意事项

1. **仅在 Agent Discretion 模式下有效** - 确保 Cursor 设置为 Agent 模式
2. **语义匹配触发** - 不同于 Claude Code 的精确触发，Cursor 通过 AI 理解上下文自动应用规则
3. **项目级配置** - 每个项目需要单独安装，规则只对当前项目生效

## 工作原理

Cursor 的 `.mdc` 规则文件包含：
- YAML 前置信息定义触发条件和元数据
- Markdown 内容定义 PUA 话术和行为准则
- AI 自动根据对话上下文匹配并应用相应规则

## 与其他平台对比

| 功能 | Claude Code | Cursor |
|-----|------------|--------|
| 触发方式 | 精确规则匹配 | 语义匹配 |
| 手动命令 | `/pua` | 不支持（需明确提示） |
| 安装位置 | `~/.claude/plugins/` | `.cursor/rules/` |
| 作用范围 | 全局 | 项目级 |

---

**详细文档**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.cursor/skills/pua
```
