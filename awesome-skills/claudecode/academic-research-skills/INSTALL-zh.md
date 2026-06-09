# 在 Claude Code 中安装 Academic Research Skills

> **注意**：Academic Research Skills 是一个 Claude Code **插件**（Plugin），不是普通的 Skills 文件。它**必须**通过官方插件系统安装，不支持手动符号链接方式。

## 前置条件

- 已安装 [Claude Code](https://docs.claude.com/en/docs/claude-code/setup)（最新版本，插件功能需要 v3.7.0+）
- 已导出 `ANTHROPIC_API_KEY` 环境变量
- *可选*：Pandoc（用于 DOCX 输出）、tectonic + Source Han Serif TC（用于 APA 7.0 PDF 输出，Markdown 输出无需安装）

## 安装步骤

在 Claude Code 中依次执行以下两条命令：

```
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```

## 验证安装

重启 Claude Code，然后尝试运行以下命令验证安装是否成功：

```
/ars-plan
```

描述你正在撰写的论文主题，ARS 将启动苏格拉底对话来规划论文结构。也可以用单次测试：

```
/ars-lit-review "your topic"
```

如果安装成功，ARS 会自动识别并启动对应的工作流。

## 更新

```
/plugin update academic-research-skills
```

## 卸载

```
/plugin uninstall academic-research-skills
```

## 获取帮助

- GitHub：https://github.com/Imbad0202/academic-research-skills
- 提交问题：https://github.com/Imbad0202/academic-research-skills/issues
- 详细安装指南：https://github.com/Imbad0202/academic-research-skills/blob/main/docs/SETUP.md
