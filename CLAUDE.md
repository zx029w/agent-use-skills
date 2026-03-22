# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AgentUse Skills is a curated library of reusable AI Agent skills. The repository contains skill definitions, bilingual documentation (Chinese/English), and platform-specific installation guides for 6 supported Agent frameworks: Claude Code, Cursor, Codex, OpenCode, OpenClaw, and Qoder.

This is primarily a **documentation repository** — there is no build system, test suite, or package manager. Skills may include Python or Node.js scripts, but there is no unified build/test pipeline.

## Repository Structure

- `awesome-skills/skills/<skill-name>/SKILL.md` — Skill definitions with YAML frontmatter (`name`, `description`)
- `awesome-skills/skills/<skill-name>/scripts/` — Optional automation scripts (Python/JS)
- `awesome-skills/introductions/{zh,en}/<skill-name>.md` — Bilingual skill introductions
- `awesome-skills/{claudecode,cursor,codex,opencode,openclaw,qoder}/<skill-name>/INSTALL-{zh,en}.md` — Platform-specific install guides
- `agent-ready/{zh,en}/` — Agent-Ready certification program docs
- `.agent/skills/` — Locally installed skills (gitignored)

## Key Workflows

### Adding a New Skill

Use the `agentuse-share` skill to automate the full contribution workflow:
1. Research the target skill (from GitHub URL or local SKILL.md)
2. Write bilingual introductions in `awesome-skills/introductions/{zh,en}/`
3. Create platform-specific installation guides (only for supported platforms)
4. Cross-check links and bilingual consistency

### Browsing/Installing Skills

Use the `skill-market` skill to query the Zerone Skill Market API:
```bash
python3 awesome-skills/skills/skill-market/scripts/market.py list
python3 awesome-skills/skills/skill-market/scripts/market.py info <skill-name>
python3 awesome-skills/skills/skill-market/scripts/market.py install <skill-name> <framework>
```

### Running Skill Scripts

Skills with Python scripts:
```bash
cd awesome-skills/skills/<skill-name>
pip install -r requirements.txt
python3 scripts/<script>.py [args]
```

## Conventions

### Naming
- All files and directories use **kebab-case** (e.g., `ui-ux-pro-max-skill`, `skill-market`)

### Bilingual Requirement
- Every document must exist in **both** Chinese (`-zh.md`) and English (`-en.md`) versions
- Content structure must match between language versions; do not mix languages in one file

### SKILL.md Format
- YAML frontmatter with `name` and `description` fields (required)
- Numbered workflow phases
- Directory structure diagrams where applicable

### Introduction Document Format
- Second-level heading for tags: `## Tags` (en) / `## 标签` (zh)
- Single-line tag format: `[Emoji] [Category] | [Emoji] [Status]`
- Installation section uses hyperlinked list pointing to platform INSTALL guides (not embedded commands)

### Installation Guide Format
- Must use **bash commands** AI agents can execute (not plugin commands like `/plugin install`)
- Sections: Prerequisites → Installation Steps → Verify → Update → Getting Help
- Only create guides for platforms the skill explicitly supports

### Git Conventions
- Branch naming: `feature/<skill-name>`, `docs/<description>`, `fix/<description>`
- Commit messages: conventional commits format `type(scope): description`
- Types: `feat`, `docs`, `fix`, `refactor`, `chore`

### Python Script Style
- `#!/usr/bin/env python3` shebang
- Prefer stdlib (`urllib`, `json`, `pathlib`) over third-party deps
- Use `argparse` for CLI args
- Print errors to `stderr`, exit with `sys.exit(1)` on failure

### JavaScript Script Style
- `#!/usr/bin/env node` shebang
- ES modules, `const`/`let` only, async/await preferred

### Markdown Style
- GitHub-flavored markdown, ATX headers
- Relative paths for internal links (never absolute URLs)
- Max line length: 120 characters (except code blocks)

## Validation

No automated test suite exists. Manual validation checklist:
1. Each skill has both Chinese and English introductions
2. Installation guides exist only for supported platforms
3. All internal links are valid relative paths
4. Kebab-case naming throughout
5. SKILL.md has valid YAML frontmatter
