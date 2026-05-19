# Installing Obsidian CLI for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- Obsidian Desktop v1.12.0+ installed with CLI enabled (Settings → Command line interface → Toggle ON)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/pablo-mano/Obsidian-CLI-skill.git ~/.openagent/Obsidian-CLI-skill
```

### 2. Symlink the Skill

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/obsidian-cli
ln -s ~/.openagent/Obsidian-CLI-skill/skills/obsidian-cli ~/.openagent/skills/obsidian-cli
```

### 3. Verify Installation

Restart OpenAgent, then try asking:

- "Read my daily note"
- "Search my vault for meeting notes"
- "do you have obsidian-cli?"

If successful, OpenAgent will automatically recognize and invoke the Obsidian CLI skill.

## Updating

```bash
cd ~/.openagent/Obsidian-CLI-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.openagent/skills/obsidian-cli
```

## Getting Help

- GitHub: https://github.com/pablo-mano/Obsidian-CLI-skill
- Report issues: https://github.com/pablo-mano/Obsidian-CLI-skill/issues
