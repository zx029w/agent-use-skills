# Installing Academic Research Skills for Claude Code

> **Note**: Academic Research Skills is a Claude Code **plugin**, not a regular skills file. It **must** be installed through the official plugin system — manual symlink installation is not supported.

## Prerequisites

- [Claude Code](https://docs.claude.com/en/docs/claude-code/setup) installed (latest version; plugin features require v3.7.0+)
- `ANTHROPIC_API_KEY` environment variable exported
- *Optional*: Pandoc for DOCX output, tectonic + Source Han Serif TC for APA 7.0 PDF output (Markdown output works without either)

## Installation Steps

Run the following two commands in Claude Code:

```
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```

## Verify Installation

Restart Claude Code, then try the following command to verify the installation:

```
/ars-plan
```

Describe a paper topic you're working on — ARS will start a Socratic dialogue to map out the chapter structure. For a single-shot test:

```
/ars-lit-review "your topic"
```

If successful, ARS will automatically recognize and invoke the corresponding workflow.

## Updating

```
/plugin update academic-research-skills
```

## Uninstallation

```
/plugin uninstall academic-research-skills
```

## Getting Help

- GitHub: https://github.com/Imbad0202/academic-research-skills
- Report issues: https://github.com/Imbad0202/academic-research-skills/issues
- Full setup guide: https://github.com/Imbad0202/academic-research-skills/blob/main/docs/SETUP.md
