# Installing Anti-Distill for Claude Code

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code) installed
- Git installed

## Installation Steps

### 1. Clone anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.claude/anti-distill
```

### 2. Symlink Skills

Create symlinks so Claude Code discovers the skills:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/anti-distill
ln -s ~/.claude/anti-distill ~/.claude/skills/anti-distill
```

### 3. Verify Installation

Restart Claude Code, then try asking:
- "do you have anti-distill?"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/anti-distill
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.claude/skills/anti-distill
```

## Getting Help

- GitHub: https://github.com/leilei926524-tech/anti-distill
- Report issues: https://github.com/leilei926524-tech/anti-distill/issues
