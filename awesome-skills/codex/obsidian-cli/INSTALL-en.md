# Installing Obsidian CLI for Codex

## Prerequisites

- [Codex](https://github.com/openai/codex) installed
- Git installed
- Obsidian Desktop v1.12.0+ installed with CLI enabled (Settings → Command line interface → Toggle ON)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/pablo-mano/Obsidian-CLI-skill.git ~/.codex/Obsidian-CLI-skill
```

### 2. Symlink the Skill

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/obsidian-cli
ln -s ~/.codex/Obsidian-CLI-skill/skills/obsidian-cli ~/.codex/skills/obsidian-cli
```

### 3. Verify Installation

Restart Codex, then try asking:

- "Read my daily note"
- "Search my vault for meeting notes"
- "do you have obsidian-cli?"

If successful, Codex will automatically recognize and invoke the Obsidian CLI skill.

## Updating

```bash
cd ~/.codex/Obsidian-CLI-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/obsidian-cli
```

## Getting Help

- GitHub: https://github.com/pablo-mano/Obsidian-CLI-skill
- Report issues: https://github.com/pablo-mano/Obsidian-CLI-skill/issues
