# Installing Anti-Distill for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/openclaw/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.openclaw/anti-distill
```

### 2. Symlink Skills

Create symlinks so OpenClaw discovers the skills:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/anti-distill
ln -s ~/.openclaw/anti-distill ~/.openclaw/skills/anti-distill
```

### 3. Verify Installation

Restart OpenClaw, then try asking:
- "do you have anti-distill?"

If successful, OpenClaw will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openclaw/anti-distill
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openclaw/skills/anti-distill
```

## Getting Help

- GitHub: https://github.com/leilei926524-tech/anti-distill
- Report issues: https://github.com/leilei926524-tech/anti-distill/issues
