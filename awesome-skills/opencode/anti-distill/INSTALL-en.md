# Installing Anti-Distill for OpenCode

## Prerequisites

- [OpenCode](https://github.com/) installed
- Git installed

## Installation Steps

### 1. Clone anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.config/opencode/anti-distill
```

### 2. Symlink Skills

Create symlinks so OpenCode discovers the skills:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/anti-distill
ln -s ~/.config/opencode/anti-distill ~/.config/opencode/skills/anti-distill
```

### 3. Verify Installation

Restart OpenCode, then try asking:
- "do you have anti-distill?"

If successful, OpenCode will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.config/opencode/anti-distill
git pull
```

## Getting Help

- GitHub: https://github.com/leilei926524-tech/anti-distill
- Report issues: https://github.com/leilei926524-tech/anti-distill/issues
