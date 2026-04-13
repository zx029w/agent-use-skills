# Installing Content Research Writer for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/content-research-writer
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/content-research-writer ~/.openagent/skills/content-research-writer
```

### 3. Verify Installation

Restart OpenAgent and try asking:
- "Help me write a blog post about AI development"
- "do you have content-research-writer?"

If successful, OpenAgent will automatically recognize and invoke the Content Research Writer skill workflow.

## Updating

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/content-research-writer
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues