# Installing Fuck-U-Code Analysis for Claude Code

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- [Node.js](https://nodejs.org/) >= 18.0.0 installed
- Git installed

## Installation Steps

### 1. Install fuck-u-code CLI

```bash
npm install -g eff-u-code
```

### 2. Clone the fuck-u-code repository

```bash
git clone https://github.com/Zerone-Agent/fuck-u-code.git ~/.claude/fuck-u-code
```

### 3. Symlink the skill

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/fuck-u-code-analysis
ln -s ~/.claude/fuck-u-code/skills/fuck-u-code-analysis ~/.claude/skills/fuck-u-code-analysis
```

### 4. Verify Installation

Restart Claude Code, then try asking:
- "Analyze the code quality of this project with fuck-u-code"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/fuck-u-code
git pull
```

## Uninstallation

```bash
rm -rf ~/.claude/skills/fuck-u-code-analysis
```

## Getting Help

- GitHub: https://github.com/Zerone-Agent/fuck-u-code
- Report issues: https://github.com/Zerone-Agent/fuck-u-code/issues
