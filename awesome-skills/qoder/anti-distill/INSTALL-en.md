# Installing Anti-Distill for Qoder

## Prerequisites

- [Qoder](https://github.com/) installed
- Git installed

## Installation Steps

### 1. Clone anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.qoder/anti-distill
```

### 2. Symlink Skills

Create symlinks so Qoder discovers the skills:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/anti-distill
ln -s ~/.qoder/anti-distill ~/.qoder/skills/anti-distill
```

### 3. Verify Installation

Restart Qoder, then try asking:
- "do you have anti-distill?"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/anti-distill
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.qoder/skills/anti-distill
```

## Getting Help

- GitHub: https://github.com/leilei926524-tech/anti-distill
- Report issues: https://github.com/leilei926524-tech/anti-distill/issues
