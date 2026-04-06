# PUA Skill - Claude Code Installation Guide

This guide explains how to install and configure the PUA skill in Claude Code.

## Installation Methods

### Method 1: Install via Marketplace (Recommended)

```bash
# Add plugin marketplace
claude plugin marketplace add tanweai/pua

# Install PUA skill
claude plugin install pua@pua-skills
```

### Method 2: Manual Installation

```bash
# Clone repository to plugins directory
git clone https://github.com/tanweai/pua.git ~/.claude/plugins/pua
```

## Language Version Selection

PUA skill provides multi-language versions. Select the appropriate language file during installation:

- **Chinese** (default): `pua`
- **English** (PIP Edition): `pua-en`
- **Japanese**: `pua-ja`

When installing via marketplace, the Chinese version is installed by default. For other language versions, manually install the corresponding files.

## Verify Installation

After installation, verify using the following methods:

1. **Check skill loading**: Confirm no error messages when starting Claude Code
2. **Test trigger**: Execute a command known to fail 2+ times and observe if L1 PUA rhetoric is triggered
3. **Manual trigger**: Type `/pua` in conversation to see if the skill activates manually

## Usage

### Auto-Trigger

PUA skill automatically triggers when:
- Task has failed 2+ times consecutively
- AI is about to say "I cannot solve this"
- Using blame-shifting expressions
- User expresses frustration (e.g., "why does this still not work")

### Manual Trigger

Type `/pua` in conversation to manually activate the skill.

## Update Method

For marketplace installations:
```bash
claude plugin update pua@pua-skills
```

For manual installations:
```bash
cd ~/.claude/plugins/pua
git pull origin main
```

## Agent Team Configuration (Experimental)

To use PUA skill in multi-agent teams:

1. Enable Agent Team feature:
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

2. Add configuration to your project's CLAUDE.md:
```markdown
# Agent Team PUA Config
All teammates must load the pua skill before starting work.
Teammates report to Leader in [PUA-REPORT] format after 2+ failures.
Leader manages global pressure levels and cross-teammate failure transfer.
```

## High-Agency v2 Version

To use the evolved High-Agency version (combining internal and external drive):

```bash
# Install via marketplace (same plugin as PUA)
claude plugin marketplace add tanweai/pua
claude plugin install pua@pua-skills
# High-Agency skill is automatically available as "high-agency"
```

High-Agency can be stacked with PUA v1 for a more complete pressure-driven mechanism.

## FAQ

**Q: Does PUA skill affect normal conversations?**
A: No. The skill only triggers when detecting giving-up tendencies or failure patterns. Successfully completed tasks are not affected.

**Q: How do I disable PUA skill?**
A: To temporarily disable, mention it in conversation; to permanently uninstall, use `claude plugin uninstall pua`.

**Q: What task types are supported?**
A: Debugging, implementation, configuration, deployment, operations, API integration, data processing — all task types.

---

**Detailed Documentation**: [GitHub - tanweai/pua](https://github.com/tanweai/pua)

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.claude/skills/pua
```
