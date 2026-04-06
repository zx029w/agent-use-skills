# PUA Skill - OpenClaw Installation Guide

This guide explains how to install and configure the PUA skill in OpenClaw.

## Installation

OpenClaw uses the same AgentSkills open standard (SKILL.md) as Claude Code. Skills work across Claude Code, Codex CLI, and OpenClaw with zero modifications.

### Install via ClawHub (Recommended)

```bash
# Use ClawHub to install PUA skill
clawhub install pua
```

### Manual Installation

```bash
# Create skills directory
mkdir -p ~/.openclaw/skills/pua

# Download Chinese version SKILL.md
curl -o ~/.openclaw/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

### Project-Level Installation (Current Project Only)

```bash
# Create project skills directory
mkdir -p skills/pua

# Download Chinese version SKILL.md
curl -o skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

## Language Version Selection

| Language | Skills Directory | URL Path | Description |
|---------|-----------------|---------|-------------|
| Chinese | `pua` | `skills/pua/` | Chinese tech giant PUA culture (default) |
| English | `pua-en` | `skills/pua-en/` | Western tech company PIP rhetoric |
| Japanese | `pua-ja` | `skills/pua-ja/` | Japanese localized version |

To switch language versions, replace `pua` with `pua-en` or `pua-ja` in the URLs and change directory names accordingly.

## Verify Installation

After installation:

1. **Check files exist**:
   ```bash
   ls -la ~/.openclaw/skills/pua/
   # Should show SKILL.md
   ```

2. **Restart OpenClaw** to ensure the skill is loaded

3. **Test trigger**: Execute a command that will fail 2+ times and observe if PUA rhetoric is triggered

4. **Manual test**: Try typing the `/pua` command

## Usage

### Auto-Trigger

OpenClaw automatically triggers PUA skill when:
- Task has failed 2+ times consecutively
- About to say "cannot solve"
- Using blame-shifting expressions
- User expresses frustration

### Manual Trigger

```bash
/pua
```

Or type `/pua` directly in conversation.

## Update Method

Via ClawHub:
```bash
clawhub update pua
```

Manual installation:
```bash
rm -rf ~/.openclaw/skills/pua
mkdir -p ~/.openclaw/skills/pua
curl -o ~/.openclaw/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

## Cross-Platform Compatibility

OpenClaw's PUA skill files are 100% compatible with:

| Platform | Compatibility | Notes |
|---------|--------------|-------|
| Claude Code | ✅ Fully Compatible | Same SKILL.md format |
| Codex CLI | ✅ Fully Compatible | Zero modifications needed |
| OpenClaw | ✅ Native Support | Recommended |

This means you can seamlessly migrate PUA skill configurations between different platforms.

## File Structure

Installed file structure:

```
~/.openclaw/
└── skills/
    └── pua/
        └── SKILL.md          # Core skill definition
```

Or project-level:

```
skills/
└── pua/
    └── SKILL.md              # Core skill definition
```

## Configuration Options

OpenClaw allows customizing PUA skill behavior via environment variables or config files:

```bash
# Set PUA language environment variable
export PUA_LANGUAGE=zh  # Options: zh, en, ja

# Or add to OpenClaw config
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

## Troubleshooting

**Issue**: Skill not loading  
**Solution**: Check if SKILL.md file exists and is properly formatted

**Issue**: Trigger not sensitive enough  
**Solution**: Ensure auto-trigger conditions are met (requires 2+ consecutive failures)

**Issue**: Wrong language version  
**Solution**: Check URLs are correct, ensure you've downloaded the desired language version

---

**Detailed Documentation**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/pua
```
