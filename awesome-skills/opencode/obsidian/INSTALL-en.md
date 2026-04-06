# Installing Obsidian Skills for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone obsidian-skills

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.config/opencode/obsidian-skills
```

### 2. Symlink Skills

Create symlinks so OpenCode's native skill tool discovers all Obsidian skills:

```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/obsidian-skills/skills ~/.config/opencode/skills/obsidian
```

### 3. Restart OpenCode

Restart OpenCode. The plugin will automatically inject Obsidian Skills context.

Verify by asking: "do you have obsidian-markdown skill?"

## Updating

```bash
cd ~/.config/opencode/obsidian-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.config/opencode/skills/obsidian
```

## Getting Help

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills Specification: https://agentskills.io/specification
