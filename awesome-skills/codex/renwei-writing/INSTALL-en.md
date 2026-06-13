# Install Renwei Writing for Codex

## Prerequisites

- [Codex](https://github.com/openai/codex) installed
- Git installed

## Installation Steps

### 1. Clone the renwei-writing repository

```bash
git clone https://github.com/orange2ai/renwei-writing.git ~/.codex/skills/renwei-writing
```

### 2. Verify Installation

Restart Codex, then try asking:
- "Do you know Renwei Writing?"
- "Help me polish this paragraph"

If successful, Codex will automatically recognize and invoke the Renwei Writing skill.

## Updating

```bash
cd ~/.codex/skills/renwei-writing
git pull
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/renwei-writing
```

## Getting Help

- GitHub: https://github.com/orange2ai/renwei-writing
- Report issues: https://github.com/orange2ai/renwei-writing/issues
