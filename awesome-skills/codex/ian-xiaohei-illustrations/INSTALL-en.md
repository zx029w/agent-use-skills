# Install Ian Xiaohei Illustrations for Codex

## Prerequisites

- [Codex](https://github.com/openai/codex) installed
- Git installed

## Installation Steps

### 1. Clone the ian-xiaohei-illustrations repository

```bash
git clone https://github.com/helloianneo/ian-xiaohei-illustrations.git ~/.codex/ian-xiaohei-illustrations
```

### 2. Copy the skill into Codex skills directory

The actual skill content lives in the nested `ian-xiaohei-illustrations/` subdirectory, which must be copied into Codex's skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R ~/.codex/ian-xiaohei-illustrations/ian-xiaohei-illustrations ~/.codex/skills/ian-xiaohei-illustrations
```

### 3. Verify Installation

Restart Codex, then try asking:
- "Use $ian-xiaohei-illustrations to generate 4 Xiaohei editorial illustrations for this article."
- "Analyze where this article should have illustrations."

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/ian-xiaohei-illustrations
git pull
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/ian-xiaohei-illustrations
cp -R ./ian-xiaohei-illustrations ~/.codex/skills/ian-xiaohei-illustrations
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/ian-xiaohei-illustrations
rm -rf ~/.codex/ian-xiaohei-illustrations
```

## Getting Help

- GitHub: https://github.com/helloianneo/ian-xiaohei-illustrations
- Report issues: https://github.com/helloianneo/ian-xiaohei-illustrations/issues
