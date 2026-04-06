# PUA 技能 - OpenAI Codex CLI 安装指南

本指南介绍如何在 OpenAI Codex CLI 中安装和配置 PUA 技能。

## 安装方式

Codex CLI 使用与 Claude Code 相同的 Agent Skills 开放标准（SKILL.md）。Codex 版本使用精简描述以适应 Codex 的长度限制。

### 全局安装（所有项目）

```bash
# 创建技能目录
mkdir -p ~/.codex/skills/pua

# 下载中文版 SKILL.md
curl -o ~/.codex/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md

# 如需 /pua 命令支持
mkdir -p ~/.codex/prompts
curl -o ~/.codex/prompts/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

### 项目级安装（仅当前项目）

```bash
# 创建项目技能目录
mkdir -p .agents/skills/pua

# 下载中文版 SKILL.md
curl -o .agents/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md

# 如需 /pua 命令支持
mkdir -p .agents/prompts
curl -o .agents/prompts/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

## 语言版本选择

| 语言 | 技能目录 | 说明 |
|-----|---------|-----|
| 中文 | `codex/pua/` | 中国大厂 PUA 文化（默认） |
| 英文 | `codex/pua-en/` | 西方科技公司 PIP 话术 |
| 日文 | `codex/pua-ja/` | 日语本地化版本 |

切换语言版本时，只需将 URL 中的 `pua` 替换为 `pua-en` 或 `pua-ja`。

## 验证安装

安装完成后：

1. **检查文件存在**:
   ```bash
   ls -la ~/.codex/skills/pua/
   # 应显示 SKILL.md
   ```

2. **测试技能加载**: 启动 Codex CLI 并观察是否有技能加载提示

3. **测试触发**: 执行一个会失败的命令 2 次以上，观察是否触发 PUA 话术

## 使用方法

### 自动触发

Codex CLI 会自动在以下情况触发 PUA 技能：
- 任务连续失败 2 次以上
- 即将说出"无法解决"
- 使用推卸责任的表达方式

### 手动触发

如果安装了 `/pua` 命令支持：
```bash
codex /pua
```

或在对话中直接输入 `/pua`。

## 升级方法

全局安装：
```bash
rm -rf ~/.codex/skills/pua
mkdir -p ~/.codex/skills/pua
curl -o ~/.codex/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md
```

项目级安装：
```bash
rm -rf .agents/skills/pua
mkdir -p .agents/skills/pua
curl -o .agents/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md
```

## 文件结构说明

安装后的文件结构：

```
~/.codex/
├── skills/
│   └── pua/
│       └── SKILL.md          # 核心技能定义
└── prompts/
    └── pua.md                # /pua 命令定义（可选）
```

或项目级：

```
.agents/
├── skills/
│   └── pua/
│       └── SKILL.md          # 核心技能定义
└── prompts/
    └── pua.md                # /pua 命令定义（可选）
```

## 与 Claude Code 的区别

| 特性 | Claude Code | Codex CLI |
|-----|------------|-----------|
| 技能格式 | SKILL.md | SKILL.md（相同） |
| 安装位置 | `~/.claude/plugins/` | `~/.codex/skills/` 或 `.agents/skills/` |
| 描述长度 | 完整 | 精简版（适应 Codex 限制） |
| 命令支持 | `/pua` | 需手动安装命令文件 |

---

**详细文档**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.codex/skills/pua
```
