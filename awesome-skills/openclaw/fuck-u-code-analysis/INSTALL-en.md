# Installing Fuck-U-Code Analysis for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/openclaw/openclaw) installed
- [Node.js](https://nodejs.org/) >= 18.0.0 installed
- Git installed

## Installation Steps

### 1. Install fuck-u-code CLI

```bash
npm install -g eff-u-code
```

### 2. Clone the fuck-u-code repository

```bash
git clone https://github.com/Zerone-Agent/fuck-u-code.git ~/.openclaw/fuck-u-code
```

### 3. Symlink the skill

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/fuck-u-code-analysis
ln -s ~/.openclaw/fuck-u-code/skills/fuck-u-code-analysis ~/.openclaw/skills/fuck-u-code-analysis
```

### 4. Verify Installation

Restart OpenClaw, then try asking:
- "Analyze the code quality of this project with fuck-u-code"

If successful, OpenClaw will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openclaw/fuck-u-code
git pull
```

## Uninstallation

```bash
rm -rf ~/.openclaw/skills/fuck-u-code-analysis
```

## Getting Help

- GitHub: https://github.com/Zerone-Agent/fuck-u-code
- Report issues: https://github.com/Zerone-Agent/fuck-u-code/issues
