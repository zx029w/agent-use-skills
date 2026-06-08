# Installing Fuck-U-Code Analysis for Cursor

## Prerequisites

- [Cursor](https://cursor.sh/) installed
- [Node.js](https://nodejs.org/) >= 18.0.0 installed
- Git installed

## Installation Steps

### 1. Install fuck-u-code CLI

```bash
npm install -g eff-u-code
```

### 2. Clone the fuck-u-code repository

```bash
git clone https://github.com/Zerone-Agent/fuck-u-code.git ~/.cursor/fuck-u-code
```

### 3. Symlink the skill

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/fuck-u-code-analysis
ln -s ~/.cursor/fuck-u-code/skills/fuck-u-code-analysis ~/.cursor/skills/fuck-u-code-analysis
```

### 4. Verify Installation

Restart Cursor, then try asking:
- "Analyze the code quality of this project with fuck-u-code"

If successful, Cursor will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.cursor/fuck-u-code
git pull
```

## Uninstallation

```bash
rm -rf ~/.cursor/skills/fuck-u-code-analysis
```

## Getting Help

- GitHub: https://github.com/Zerone-Agent/fuck-u-code
- Report issues: https://github.com/Zerone-Agent/fuck-u-code/issues
