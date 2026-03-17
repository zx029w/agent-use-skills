# PUA Skill - OpenAI Codex CLI Installation Guide

This guide explains how to install and configure the PUA skill in OpenAI Codex CLI.

## Installation

Codex CLI uses the same Agent Skills open standard (SKILL.md) as Claude Code. The Codex version uses a condensed description to fit Codex's length limits.

### Global Installation (All Projects)

```bash
# Create skills directory
mkdir -p ~/.codex/skills/pua

# Download Chinese version SKILL.md
curl -o ~/.codex/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md

# For /pua command support
mkdir -p ~/.codex/prompts
curl -o ~/.codex/prompts/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

### Project-Level Installation (Current Project Only)

```bash
# Create project skills directory
mkdir -p .agents/skills/pua

# Download Chinese version SKILL.md
curl -o .agents/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md

# For /pua command support
mkdir -p .agents/prompts
curl -o .agents/prompts/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

## Language Version Selection

| Language | Skills Directory | Description |
|---------|-----------------|-------------|
| Chinese | `codex/pua/` | Chinese tech giant PUA culture (default) |
| English | `codex/pua-en/` | Western tech company PIP rhetoric |
| Japanese | `codex/pua-ja/` | Japanese localized version |

To switch language versions, simply replace `pua` with `pua-en` or `pua-ja` in the URLs.

## Verify Installation

After installation:

1. **Check files exist**:
   ```bash
   ls -la ~/.codex/skills/pua/
   # Should show SKILL.md
   ```

2. **Test skill loading**: Start Codex CLI and observe skill loading prompts

3. **Test trigger**: Execute a command that will fail 2+ times and observe if PUA rhetoric is triggered

## Usage

### Auto-Trigger

Codex CLI automatically triggers PUA skill when:
- Task has failed 2+ times consecutively
- About to say "cannot solve"
- Using blame-shifting expressions

### Manual Trigger

If `/pua` command support is installed:
```bash
codex /pua
```

Or type `/pua` directly in conversation.

## Update Method

Global installation:
```bash
rm -rf ~/.codex/skills/pua
mkdir -p ~/.codex/skills/pua
curl -o ~/.codex/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md
```

Project-level installation:
```bash
rm -rf .agents/skills/pua
mkdir -p .agents/skills/pua
curl -o .agents/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md
```

## File Structure

Installed file structure:

```
~/.codex/
├── skills/
│   └── pua/
│       └── SKILL.md          # Core skill definition
└── prompts/
    └── pua.md                # /pua command definition (optional)
```

Or project-level:

```
.agents/
├── skills/
│   └── pua/
│       └── SKILL.md          # Core skill definition
└── prompts/
    └── pua.md                # /pua command definition (optional)
```

## Differences from Claude Code

| Feature | Claude Code | Codex CLI |
|--------|-------------|-----------|
| Skill Format | SKILL.md | SKILL.md (same) |
| Install Location | `~/.claude/plugins/` | `~/.codex/skills/` or `.agents/skills/` |
| Description Length | Full | Condensed (fits Codex limits) |
| Command Support | `/pua` | Requires manual command file installation |

---

**Detailed Documentation**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)
