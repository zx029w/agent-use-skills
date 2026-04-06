# PUA 技能 - OpenCode 安装指南

本指南介绍如何在 OpenCode 中安装和配置 PUA 技能。

## 安装方式

OpenCode 使用与 Claude Code 相同的 AgentSkills 开放标准（SKILL.md），无需任何修改即可使用。

### 全局安装（所有项目）

```bash
# 创建技能目录
mkdir -p ~/.config/opencode/skills/pua

# 下载中文版 SKILL.md
curl -o ~/.config/opencode/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

### 项目级安装（仅当前项目）

```bash
# 创建项目技能目录
mkdir -p .opencode/skills/pua

# 下载中文版 SKILL.md
curl -o .opencode/skills/pua/SKILL.md \
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
   ls -la ~/.config/opencode/skills/pua/
   # 应显示 SKILL.md
   ```

2. **重启 OpenCode** 确保技能被加载

3. **测试触发**: 执行一个会失败的命令 2 次以上，观察是否触发 PUA 话术

4. **手动测试**: 尝试输入 `/pua` 命令或要求 AI "使用 PUA 模式"

## 使用方法

### 自动触发

OpenCode 会自动在以下情况触发 PUA 技能：
- 任务连续失败 2 次以上
- 即将说出"无法解决"
- 使用推卸责任的表达方式
- 用户表达沮丧情绪（如"为什么还不行"、"再试一次"）

### 手动触发

在 OpenCode 对话中：
- 输入 `/pua` 命令
- 或明确说"使用 PUA 模式"、"开启高能动性模式"

## 升级方法

全局安装：
```bash
rm -rf ~/.config/opencode/skills/pua
mkdir -p ~/.config/opencode/skills/pua
curl -o ~/.config/opencode/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

项目级安装：
```bash
rm -rf .opencode/skills/pua
mkdir -p .opencode/skills/pua
curl -o .opencode/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

## OpenCode 特有功能

OpenCode 支持 PUA 技能的以下特性：

1. **实时触发** - OpenCode 实时检测 AI 响应并触发 PUA 机制
2. **多语言支持** - 完整支持中文、英文、日文三种语言版本
3. **技能叠加** - 可与其他技能（如 superpowers:systematic-debugging）叠加使用
4. **High-Agency v2** - 支持进化版高能动性技能

## 跨平台兼容性

OpenCode 的 PUA 技能文件与以下平台 100% 兼容：

| 平台 | 兼容性 | 说明 |
|-----|-------|-----|
| Claude Code | ✅ 完全兼容 | 同一 SKILL.md 格式 |
| Codex CLI | ✅ 完全兼容 | 零修改即可使用 |
| OpenClaw | ✅ 完全兼容 | 同一标准 |
| OpenCode | ✅ 原生支持 | 推荐使用 |

## 文件结构

安装后的文件结构：

```
~/.config/opencode/
└── skills/
    └── pua/
        └── SKILL.md          # 核心技能定义
```

或项目级：

```
.opencode/
└── skills/
    └── pua/
        └── SKILL.md          # 核心技能定义
```

## 推荐搭配使用

PUA 技能在 OpenCode 中与以下技能搭配效果更佳：

- **superpowers:systematic-debugging** - PUA 提供动机层，systematic-debugging 提供方法论
- **superpowers:verification-before-completion** - 防止虚假"已修复"声明
- **high-agency** - 与 PUA 叠加：内驱力 + 外驱力，L1 前触发恢复协议

## 使用示例

**示例 1: 调试场景**
```
用户: 这个 bug 我一直修不好
AI: [自动触发 L1] 这个 bug 都解不出来，让我怎么给你打绩效？让我换种方法试试...
```

**示例 2: 手动激活**
```
用户: /pua
AI: [激活 PUA 模式] 已开启高能动性模式，我将穷尽所有方案直到解决问题。
```

**示例 3: 多次失败后升级**
```
用户: 还是不行！
AI: [触发 L3] 经过慎重考虑，这次给你打 3.25。现在开始执行 7 点检查清单...
```

## 故障排除

**问题**: 技能未加载  
**解决**: 
1. 检查 SKILL.md 文件是否存在
2. 确认文件路径正确
3. 重启 OpenCode

**问题**: 触发不灵敏  
**解决**: 
1. 确认已连续失败 2 次以上
2. 检查 AI 响应是否包含触发关键词
3. 尝试手动触发 `/pua`

**问题**: 想要英文版却触发中文版  
**解决**: 
1. 删除中文版本 `rm -rf ~/.config/opencode/skills/pua`
2. 安装英文版，将 URL 中的 `pua` 改为 `pua-en`

---

**详细文档**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)  
**官方网站**: [openpua.ai](https://openpua.ai)

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.config/opencode/skills/pua
```
