# Installing Obsidian CLI for Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
- Git installed
- Obsidian Desktop v1.12.0+ installed with CLI enabled (Settings → Command line interface → Toggle ON)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/pablo-mano/Obsidian-CLI-skill.git ~/.cursor/Obsidian-CLI-skill
```

### 2. Symlink the Skill

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/obsidian-cli
ln -s ~/.cursor/Obsidian-CLI-skill/skills/obsidian-cli ~/.cursor/skills/obsidian-cli
```

### 3. Verify Installation

Restart Cursor, then try asking:

- "Read my daily note"
- "Search my vault for meeting notes"
- "do you have obsidian-cli?"

If successful, Cursor will automatically recognize and invoke the Obsidian CLI skill.

## Updating

```bash
cd ~/.cursor/Obsidian-CLI-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.cursor/skills/obsidian-cli
```

## Getting Help

- GitHub: https://github.com/pablo-mano/Obsidian-CLI-skill
- Report issues: https://github.com/pablo-mano/Obsidian-CLI-skill/issues
