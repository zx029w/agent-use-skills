# 在 Codex CLI 中安装 Academic Research Skills

> **注意**：Codex 版本的 Academic Research Skills 来自**独立的兄弟仓库** [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex)，以单个技能包 `$academic-research-suite` 的形式打包，包含所有 ARS 工作流。

## 前置条件

- 已安装 [Codex CLI](https://github.com/openai/codex)
- 已安装 Python 3
- 已安装 Git

## 安装步骤

使用 Codex skill-installer 脚本安装：

```bash
python3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo Imbad0202/academic-research-skills-codex \
  --ref main \
  --path skills/academic-research-suite \
  --method git
```

安装完成后，打开一个新的 Codex 会话。已有会话可能保留旧的技能缓存，无需关闭其他 Claude 或 Codex 会话。

### 验证安装

在新 Codex 会话中运行：

```
/skills
```

你应该看到一个 ARS 条目 `academic-research-suite` 或 `Academic Research ...`。你**不应该**看到单独的 `academic-paper`、`academic-pipeline`、`deep-research` 或 `academic-paper-reviewer` 技能。

测试路由功能：

```
Use $academic-research-suite.
I want to write a paper on AI adoption in higher education quality assurance.
I do not yet have a clear research question.
```

如果安装成功，ARS 将路由到 `deep-research` `socratic` 模式并开始提问。

## 更新

```bash
rm -rf "$HOME/.codex/skills/academic-research-suite"
python3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo Imbad0202/academic-research-skills-codex \
  --ref main \
  --path skills/academic-research-suite \
  --method git
```

更新后打开新的 Codex 会话。

## 使用方式

在 Codex 中通过 `$academic-research-suite` 调用：

```
Use $academic-research-suite to help me plan a systematic literature review on AI adoption.
```

也可使用 Claude 风格的别名（如 `ars-plan`、`ars-reviewer`、`ars-lit-review` 等）。

## 卸载

```bash
rm -rf "$HOME/.codex/skills/academic-research-suite"
```

## 获取帮助

- GitHub（Codex 版本）：https://github.com/Imbad0202/academic-research-skills-codex
- 原始项目：https://github.com/Imbad0202/academic-research-skills
- 提交问题：https://github.com/Imbad0202/academic-research-skills-codex/issues
