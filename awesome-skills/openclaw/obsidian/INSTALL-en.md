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
ln -s ~/.openclaw/obsidian-skills/skills ~/.openclaw/skills/obsidian
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

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/obsidian
```

## Getting Help

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills Specification: https://agentskills.io/specification
