# Installing Obsidian Skills for Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed

## Installation Steps

### 1. Clone obsidian-skills

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.qoder/obsidian-skills
```

### 2. Symlink Skills

Create symlinks so Qoder discovers all Obsidian skills:

```bash
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/obsidian-skills/skills ~/.qoder/skills/obsidian
```

### 3. Verify Installation

Restart Qoder, then try asking:

- "Create a note with wikilinks: [[Another Note]]"
- "do you have obsidian-markdown skill?"

If successful, Qoder will automatically recognize and invoke the Obsidian Skills.

## Updating

```bash
cd ~/.qoder/obsidian-skills
git pull
```

## Getting Help

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills Specification: https://agentskills.io/specification