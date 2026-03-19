# Installing Obsidian Skills for Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone obsidian-skills

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.cursor/obsidian-skills
```

### 2. Symlink Skills

Create symlinks so Cursor discovers all Obsidian skills:

```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/obsidian-skills/skills/obsidian-markdown ~/.cursor/skills/obsidian-markdown
ln -s ~/.cursor/obsidian-skills/skills/obsidian-bases ~/.cursor/skills/obsidian-bases
ln -s ~/.cursor/obsidian-skills/skills/json-canvas ~/.cursor/skills/json-canvas
ln -s ~/.cursor/obsidian-skills/skills/obsidian-cli ~/.cursor/skills/obsidian-cli
ln -s ~/.cursor/obsidian-skills/skills/defuddle ~/.cursor/skills/defuddle
```

### 3. Verify Installation

Restart Cursor and ensure you are in **Agent** mode. Then try asking:

- "Create a note with wikilinks: [[Another Note]]"
- "do you have obsidian-markdown skill?"

If successful, the Cursor Agent will automatically recognize and invoke the Obsidian Skills.

## Updating

```bash
cd ~/.cursor/obsidian-skills
git pull
```

## Getting Help

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills Specification: https://agentskills.io/specification