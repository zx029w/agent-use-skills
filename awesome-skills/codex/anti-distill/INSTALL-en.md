# Installing Anti-Distill for Codex

## Prerequisites

- [Codex](https://github.com/) installed
- Git installed

## Installation Steps

### 1. Clone anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.codex/anti-distill
```

### 2. Symlink Skills

Create symlinks so Codex discovers the skills:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/anti-distill
ln -s ~/.codex/anti-distill ~/.codex/skills/anti-distill
```

### 3. Verify Installation

Restart Codex, then try asking:
- "do you have anti-distill?"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/anti-distill
git pull
```

## Getting Help

- GitHub: https://github.com/leilei926524-tech/anti-distill
- Report issues: https://github.com/leilei926524-tech/anti-distill/issues
