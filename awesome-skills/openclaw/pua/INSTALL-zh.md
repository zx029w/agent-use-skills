# PUA 技能 - OpenClaw 安装指南

本指南介绍如何在 OpenClaw 中安装和配置 PUA 技能。

## 安装方式

OpenClaw 使用与 Claude Code 相同的 AgentSkills 开放标准（SKILL.md），技能可以零修改地在 Claude Code、Codex CLI 和 OpenClaw 之间通用。

### 通过 ClawHub 安装（推荐）

```bash
# 使用 ClawHub 安装 PUA 技能
clawhub install pua
```

### 手动安装

```bash
# 创建技能目录
mkdir -p ~/.openclaw/skills/pua

# 下载中文版 SKILL.md
curl -o ~/.openclaw/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

### 项目级安装（仅当前项目）

```bash
# 创建项目技能目录
mkdir -p skills/pua

# 下载中文版 SKILL.md
curl -o skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

## 语言版本选择

| 语言 | 技能目录 | URL 路径 | 说明 |
|-----|---------|---------|-----|
| 中文 | `pua` | `skills/pua/` | 中国大厂 PUA 文化（默认） |
| 英文 | `pua-en` | `skills/pua-en/` | 西方科技公司 PIP 话术 |
| 日文 | `pua-ja` | `skills/pua-ja/` | 日语本地化版本 |

切换语言版本时，将 URL 中的 `pua` 替换为 `pua-en` 或 `pua-ja`，并将目录名相应更改。

## 验证安装

安装完成后：

1. **检查文件存在**:
   ```bash
   ls -la ~/.openclaw/skills/pua/
   # 应显示 SKILL.md
   ```

2. **重启 OpenClaw** 确保技能被加载

3. **测试触发**: 执行一个会失败的命令 2 次以上，观察是否触发 PUA 话术

4. **手动测试**: 尝试输入 `/pua` 命令

## 使用方法

### 自动触发

OpenClaw 会自动在以下情况触发 PUA 技能：
- 任务连续失败 2 次以上
- 即将说出"无法解决"
- 使用推卸责任的表达方式
- 用户表达沮丧情绪

### 手动触发

```bash
/pua
```

或在对话中直接输入 `/pua`。

## 升级方法

通过 ClawHub：
```bash
clawhub update pua
```

手动安装：
```bash
rm -rf ~/.openclaw/skills/pua
mkdir -p ~/.openclaw/skills/pua
curl -o ~/.openclaw/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

## 跨平台兼容性

OpenClaw 的 PUA 技能文件与以下平台 100% 兼容：

| 平台 | 兼容性 | 说明 |
|-----|-------|-----|
| Claude Code | ✅ 完全兼容 | 同一 SKILL.md 格式 |
| Codex CLI | ✅ 完全兼容 | 零修改即可使用 |
| OpenClaw | ✅ 原生支持 | 推荐使用 |

这意味着你可以在不同平台间无缝迁移 PUA 技能配置。

## 文件结构

安装后的文件结构：

```
~/.openclaw/
└── skills/
    └── pua/
        └── SKILL.md          # 核心技能定义
```

或项目级：

```
skills/
└── pua/
    └── SKILL.md              # 核心技能定义
```

## 配置选项

OpenClaw 允许通过环境变量或配置文件自定义 PUA 技能行为：

```bash
# 设置 PUA 语言环境变量
export PUA_LANGUAGE=zh  # 可选: zh, en, ja

# 或添加到 OpenClaw 配置
# ~/.openclaw/config.json
{
  "skills": {
    "pua": {
      "language": "zh",
      "auto_trigger": true
    }
  }
}
```

## 故障排除

**问题**: 技能未加载  
**解决**: 检查 SKILL.md 文件是否存在且格式正确

**问题**: 触发不灵敏  
**解决**: 确认自动触发条件是否满足（需要 2 次以上连续失败）

**问题**: 语言版本错误  
**解决**: 检查 URL 是否正确，确保下载了所需语言版本

---

**详细文档**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openclaw/skills/pua
```
