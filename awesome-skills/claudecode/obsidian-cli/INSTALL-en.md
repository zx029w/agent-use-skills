# Installing Obsidian CLI for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed
- Obsidian Desktop v1.12.0+ installed with CLI enabled (Settings → Command line interface → Toggle ON)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/pablo-mano/Obsidian-CLI-skill.git ~/.claude/Obsidian-CLI-skill
```

### 2. Symlink the Skill

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/obsidian-cli
ln -s ~/.claude/Obsidian-CLI-skill/skills/obsidian-cli ~/.claude/skills/obsidian-cli
```

### 3. Verify Installation

Restart Claude Code, then try asking:

- "Read my daily note"
- "Search my vault for meeting notes"
- "do you have obsidian-cli?"

If successful, Claude Code will automatically recognize and invoke the Obsidian CLI skill.

## Updating

```bash
cd ~/.claude/Obsidian-CLI-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.claude/skills/obsidian-cli
```

## Getting Help

- GitHub: https://github.com/pablo-mano/Obsidian-CLI-skill
- Report issues: https://github.com/pablo-mano/Obsidian-CLI-skill/issues
