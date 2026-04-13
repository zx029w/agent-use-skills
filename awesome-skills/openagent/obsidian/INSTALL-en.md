# Installing Obsidian Skills for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- Node.js and npm installed

## Installation Steps

### 1. Clone obsidian-skills

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.openagent/obsidian-skills
```

### 2. Symlink Skills

Create symlinks so OpenAgent discovers the skills:

```bash
mkdir -p ~/.openagent/skills
for skill in obsidian-markdown obsidian-bases json-canvas obsidian-cli defuddle; do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/obsidian-skills/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. Install Obsidian CLI (Optional)

If you need the obsidian-cli skill:

```bash
npm install -g obsidian-cli
```

### 4. Verify Installation

Restart OpenAgent and try asking:
- "Help me create an Obsidian note"
- "do you have obsidian-markdown?"

If successful, OpenAgent will automatically recognize and invoke Obsidian Skills workflow.

## Updating

```bash
cd ~/.openagent/obsidian-skills
git pull
```

## Uninstallation

Remove the symlinks to uninstall:

```bash
for skill in obsidian-markdown obsidian-bases json-canvas obsidian-cli defuddle; do
  rm -rf ~/.openagent/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/kepano/obsidian-skills