# PUA Skill - OpenCode Installation Guide

This guide explains how to install and configure the PUA skill in OpenCode.

## Installation

OpenCode uses the same AgentSkills open standard (SKILL.md) as Claude Code. Zero modifications are needed.

### Global Installation (All Projects)

```bash
# Create skills directory
mkdir -p ~/.config/opencode/skills/pua

# Download Chinese version SKILL.md
curl -o ~/.config/opencode/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

### Project-Level Installation (Current Project Only)

```bash
# Create project skills directory
mkdir -p .opencode/skills/pua

# Download Chinese version SKILL.md
curl -o .opencode/skills/pua/SKILL.md \
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
   ls -la ~/.config/opencode/skills/pua/
   # Should show SKILL.md
   ```

2. **Restart OpenCode** to ensure the skill is loaded

3. **Test trigger**: Execute a command that will fail 2+ times and observe if PUA rhetoric is triggered

4. **Manual test**: Try typing the `/pua` command or ask AI to "use PUA mode"

## Usage

### Auto-Trigger

OpenCode automatically triggers PUA skill when:
- Task has failed 2+ times consecutively
- About to say "cannot solve"
- Using blame-shifting expressions
- User expresses frustration (e.g., "why does this still not work", "try again")

### Manual Trigger

In OpenCode conversation:
- Type `/pua` command
- Or explicitly say "use PUA mode" or "enable high-agency mode"

## Update Method

Global installation:
```bash
rm -rf ~/.config/opencode/skills/pua
mkdir -p ~/.config/opencode/skills/pua
curl -o ~/.config/opencode/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

Project-level installation:
```bash
rm -rf .opencode/skills/pua
mkdir -p .opencode/skills/pua
curl -o .opencode/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

## OpenCode-Specific Features

OpenCode supports the following PUA skill features:

1. **Real-time triggering** - OpenCode detects AI responses in real-time and triggers PUA mechanisms
2. **Multi-language support** - Full support for Chinese, English, and Japanese versions
3. **Skill stacking** - Can be used with other skills (e.g., superpowers:systematic-debugging)
4. **High-Agency v2** - Supports the evolved high-agency skill version

## Cross-Platform Compatibility

OpenCode's PUA skill files are 100% compatible with:

| Platform | Compatibility | Notes |
|----------|--------------|-------|
| Claude Code | ✅ Fully Compatible | Same SKILL.md format |
| Codex CLI | ✅ Fully Compatible | Zero modifications needed |
| OpenClaw | ✅ Fully Compatible | Same standard |
| OpenCode | ✅ Native Support | Recommended |

## File Structure

Installed file structure:

```
~/.config/opencode/
└── skills/
    └── pua/
        └── SKILL.md          # Core skill definition
```

Or project-level:

```
.opencode/
└── skills/
    └── pua/
        └── SKILL.md          # Core skill definition
```

## Recommended Combinations

PUA skill works better in OpenCode when combined with:

- **superpowers:systematic-debugging** - PUA provides motivation layer, systematic-debugging provides methodology
- **superpowers:verification-before-completion** - Prevents false "fixed" claims
- **high-agency** - Stack with PUA: inner drive + external pressure, Recovery Protocol before L1

## Usage Examples

**Example 1: Debugging Scenario**
```
User: I can't seem to fix this bug
AI: [Auto-trigger L1] You can't even solve this bug — how am I supposed to rate your performance? Let me try a different approach...
```

**Example 2: Manual Activation**
```
User: /pua
AI: [PUA mode activated] High-agency mode enabled. I will exhaust all solutions until the problem is solved.
```

**Example 3: Escalation After Multiple Failures**
```
User: Still not working!
AI: [Trigger L3] After careful consideration, I'm giving you a 3.25. Now executing the 7-point checklist...
```

## Troubleshooting

**Issue**: Skill not loading  
**Solution**:
1. Check if SKILL.md file exists
2. Confirm file path is correct
3. Restart OpenCode

**Issue**: Trigger not sensitive enough  
**Solution**:
1. Ensure there have been 2+ consecutive failures
2. Check if AI response contains trigger keywords
3. Try manual trigger `/pua`

**Issue**: Chinese version triggers when you want English  
**Solution**:
1. Remove Chinese version: `rm -rf ~/.config/opencode/skills/pua`
2. Install English version by changing `pua` to `pua-en` in the URL

---

**Detailed Documentation**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)  
**Official Website**: [openpua.ai](https://openpua.ai)
