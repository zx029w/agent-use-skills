# Installing Obsidian Skills for Codex

## Prerequisites

- [Codex CLI](https://github.com/openai/codex) installed
- Git installed

## Installation Steps

### 1. Clone obsidian-skills

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.codex/obsidian-skills
```

### 2. Symlink Skills

Create symlinks so Codex discovers the obsidian skills:

```bash
mkdir -p ~/.codex/skills
ln -s ~/.codex/obsidian-skills/skills ~/.codex/skills/obsidian
```

### 3. Verify Installation

Restart Codex, then try asking:

- "Create a note with wikilinks: [[Another Note]]"
- "do you have obsidian-markdown skill?"

If successful, Codex will automatically recognize and invoke the Obsidian Skills.

## Updating

```bash
cd ~/.codex/obsidian-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.codex/skills/obsidian
```

## Getting Help

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills Specification: https://agentskills.io/specification
