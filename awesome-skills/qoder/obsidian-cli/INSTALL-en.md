# Installing Obsidian CLI for Qoder

## Prerequisites

- Qoder installed
- Git installed
- Obsidian Desktop v1.12.0+ installed with CLI enabled (Settings → Command line interface → Toggle ON)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/pablo-mano/Obsidian-CLI-skill.git ~/.qoder/Obsidian-CLI-skill
```

### 2. Symlink the Skill

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/obsidian-cli
ln -s ~/.qoder/Obsidian-CLI-skill/skills/obsidian-cli ~/.qoder/skills/obsidian-cli
```

### 3. Verify Installation

Restart Qoder, then try asking:

- "Read my daily note"
- "Search my vault for meeting notes"
- "do you have obsidian-cli?"

If successful, Qoder will automatically recognize and invoke the Obsidian CLI skill.

## Updating

```bash
cd ~/.qoder/Obsidian-CLI-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.qoder/skills/obsidian-cli
```

## Getting Help

- GitHub: https://github.com/pablo-mano/Obsidian-CLI-skill
- Report issues: https://github.com/pablo-mano/Obsidian-CLI-skill/issues
