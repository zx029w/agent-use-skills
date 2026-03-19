# Installing Obsidian Skills for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone obsidian-skills

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.openclaw/obsidian-skills
```

### 2. Symlink Skills

Create symlinks so OpenClaw discovers all Obsidian skills:

```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/obsidian-skills/skills/obsidian-markdown ~/.openclaw/skills/obsidian-markdown
ln -s ~/.openclaw/obsidian-skills/skills/obsidian-bases ~/.openclaw/skills/obsidian-bases
ln -s ~/.openclaw/obsidian-skills/skills/json-canvas ~/.openclaw/skills/json-canvas
ln -s ~/.openclaw/obsidian-skills/skills/obsidian-cli ~/.openclaw/skills/obsidian-cli
ln -s ~/.openclaw/obsidian-skills/skills/defuddle ~/.openclaw/skills/defuddle
```

### 3. Verify Installation

Restart OpenClaw, then try asking:

- "Create a note with wikilinks: [[Another Note]]"
- "do you have obsidian-markdown skill?"

If successful, OpenClaw will automatically recognize and invoke the Obsidian Skills.

## Updating

```bash
cd ~/.openclaw/obsidian-skills
git pull
```

## Getting Help

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills Specification: https://agentskills.io/specification