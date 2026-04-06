# Installing Obsidian Skills for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone obsidian-skills

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.claude/obsidian-skills
```

### 2. Symlink Skills

Create symlinks so Claude Code discovers all Obsidian skills:

```bash
mkdir -p ~/.claude/skills
for skill in $(ls ~/.claude/obsidian-skills/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/obsidian-skills/skills/$skill ~/.claude/skills/$skill
done
```

### 3. Verify Installation

Restart Claude Code, then try asking:

- "Create a note with wikilinks: [[Another Note]]"
- "do you have obsidian-markdown skill?"

If successful, Claude Code will automatically recognize and invoke the Obsidian Skills.

## Updating

```bash
cd ~/.claude/obsidian-skills
git pull
```

## Getting Help

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills Specification: https://agentskills.io/specification