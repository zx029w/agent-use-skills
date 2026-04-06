# PUA Skill - Cursor Installation Guide

This guide explains how to install and configure the PUA skill in Cursor.

## Installation

Cursor uses `.mdc` rule files (Markdown + YAML frontmatter). PUA rules automatically trigger via AI semantic matching (Agent Discretion mode).

### Project-Level Installation (Recommended)

```bash
# Create rules directory
mkdir -p .cursor/rules

# Download Chinese version
curl -o .cursor/rules/pua.mdc \
  https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua.mdc

# For English version (PIP Edition)
curl -o .cursor/rules/pua-en.mdc \
  https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua-en.mdc

# For Japanese version
curl -o .cursor/rules/pua-ja.mdc \
  https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua-ja.mdc
```

## Language Version Selection

| Language | Filename | Description |
|---------|---------|-------------|
| Chinese | `pua.mdc` | Chinese tech giant PUA culture |
| English | `pua-en.mdc` | Western tech company PIP rhetoric |
| Japanese | `pua-ja.mdc` | Japanese localized version |

## Verify Installation

After installation:

1. **Restart Cursor** to ensure rule files are loaded
2. **Check Agent mode** - Ensure you're working in Agent Discretion mode
3. **Test trigger** - Try executing a debugging task that will fail and observe if AI exhibits PUA rhetoric

## Usage

### Auto-Trigger

In Cursor's Agent mode, PUA skill automatically triggers via semantic matching:
- Detecting giving-up tendencies
- 2+ consecutive failures
- Using blame-shifting expressions

### Manual Activation

Since Cursor doesn't support the `/pua` command, you can:
- Explicitly say "use PUA mode" in conversation
- Copy key PUA rule prompts into the conversation

## Update Method

```bash
# Remove old version
rm .cursor/rules/pua*.mdc

# Re-download latest version
curl -o .cursor/rules/pua.mdc \
  https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua.mdc
```

## Notes

1. **Only works in Agent Discretion mode** - Ensure Cursor is set to Agent mode
2. **Semantic matching trigger** - Unlike Claude Code's precise triggering, Cursor applies rules automatically through AI understanding of context
3. **Project-level configuration** - Each project needs separate installation; rules only apply to the current project

## How It Works

Cursor's `.mdc` rule files contain:
- YAML frontmatter defining trigger conditions and metadata
- Markdown content defining PUA rhetoric and behavioral guidelines
- AI automatically matches and applies appropriate rules based on conversation context

## Comparison with Other Platforms

| Feature | Claude Code | Cursor |
|--------|-------------|--------|
| Trigger Method | Precise rule matching | Semantic matching |
| Manual Command | `/pua` | Not supported (requires explicit prompt) |
| Install Location | `~/.claude/plugins/` | `.cursor/rules/` |
| Scope | Global | Project-level |

---

**Detailed Documentation**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/pua
```
