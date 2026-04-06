# PUA 技能 - Claude Code 安装指南

本指南介绍如何在 Claude Code 中安装和配置 PUA 技能。

## 安装方式

### 方式一：通过插件市场安装（推荐）

```bash
# 添加插件市场
claude plugin marketplace add tanweai/pua

# 安装 PUA 技能
claude plugin install pua@pua-skills
```

### 方式二：手动安装

```bash
# 克隆仓库到插件目录
git clone https://github.com/tanweai/pua.git ~/.claude/plugins/pua
```

## 语言版本选择

PUA 技能提供多语言版本，安装时选择对应语言文件：

- **中文版（默认）**: `pua`
- **英文版（PIP Edition）**: `pua-en`
- **日文版**: `pua-ja`

通过插件市场安装时，默认安装中文版。如需其他语言版本，请手动安装对应文件。

## 验证安装

安装完成后，可以通过以下方式验证：

1. **检查技能加载**: 启动 Claude Code 时，确认没有报错信息
2. **测试触发**: 尝试执行一个已知会失败的命令 2 次以上，观察是否触发 L1 PUA 话术
3. **手动触发**: 在对话中输入 `/pua` 查看是否能手动激活技能

## 使用方法

### 自动触发

当满足以下条件时，PUA 技能会自动触发：
- 任务连续失败 2 次以上
- AI 即将说出"我无法解决"
- 使用推卸责任的表达方式
- 用户表达沮丧情绪（如"为什么还不行"）

### 手动触发

在对话中输入 `/pua` 命令手动激活技能。

## 升级方法

通过插件市场安装的用户：
```bash
claude plugin update pua@pua-skills
```

手动安装的用户：
```bash
cd ~/.claude/plugins/pua
git pull origin main
```

## Agent Team 配置（实验性功能）

如需在多代理团队中使用 PUA 技能：

1. 启用 Agent Team 功能：
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

2. 在项目 CLAUDE.md 中添加配置：
```markdown
# Agent Team PUA Config
All teammates must load the pua skill before starting work.
Teammates report to Leader in [PUA-REPORT] format after 2+ failures.
Leader manages global pressure levels and cross-teammate failure transfer.
```

## High-Agency v2 版本

如需使用进化版 High-Agency（结合内驱力和外驱力）：

```bash
# 通过插件市场安装（与 PUA 同一插件）
claude plugin marketplace add tanweai/pua
claude plugin install pua@pua-skills
# High-Agency 技能会自动作为 "high-agency" 可用
```

High-Agency 可以与 PUA v1 叠加使用，提供更完整的压力驱动机制。

## 常见问题

**Q: PUA 技能会影响正常对话吗？**
A: 不会。技能仅在检测到放弃倾向或失败模式时触发，正常成功的任务不会受影响。

**Q: 如何关闭 PUA 技能？**
A: 暂时禁用可以在对话中说明；永久卸载可以使用 `claude plugin uninstall pua`。

**Q: 支持哪些任务类型？**
A: 调试、实现、配置、部署、运维、API 集成、数据处理等所有任务类型。

---

**详细文档**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.claude/skills/pua
```
