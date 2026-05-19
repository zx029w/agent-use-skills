# Installing Obsidian CLI for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- Git installed
- Obsidian Desktop v1.12.0+ installed with CLI enabled (Settings → Command line interface → Toggle ON)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/pablo-mano/Obsidian-CLI-skill.git ~/.config/opencode/Obsidian-CLI-skill
```

### 2. Symlink the Skill

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/obsidian-cli
ln -s ~/.config/opencode/Obsidian-CLI-skill/skills/obsidian-cli ~/.config/opencode/skills/obsidian-cli
```

### 3. Verify Installation

Restart OpenCode, then try asking:

- "Read my daily note"
- "Search my vault for meeting notes"
- "do you have obsidian-cli?"

If successful, OpenCode will automatically recognize and invoke the Obsidian CLI skill.

## Updating

```bash
cd ~/.config/opencode/Obsidian-CLI-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.config/opencode/skills/obsidian-cli
```

## Getting Help

- GitHub: https://github.com/pablo-mano/Obsidian-CLI-skill
- Report issues: https://github.com/pablo-mano/Obsidian-CLI-skill/issues
