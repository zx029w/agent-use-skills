# Installing Skill Creator for Codex

## Prerequisites

- [Codex](https://github.com/openai/codex) installed
- Git installed
- Python 3.8+

## Installation Steps

### 1. Clone agent-use-skills Repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Create Symlink

Create a symlink so Codex discovers the skill-creator skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/skill-creator
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/skill-creator ~/.codex/skills/skill-creator
```

### 3. Verify Installation

Restart Codex, then try asking:
- "I need to create a new skill, please help me use skill-creator"
- "do you have skill-creator?"

If successful, Codex will automatically recognize and invoke the Skill Creator skill workflow.

## Updating

```bash
cd ~/.codex/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.codex/skills/skill-creator
```

## Getting Help

- GitHub Repository: https://github.com/Zerone-Agent/agent-use-skills
- Report Issues: https://github.com/Zerone-Agent/agent-use-skills/issues
