# Installing Fuck-U-Code Analysis for OpenAgent

## Prerequisites

- [OpenAgent](https://github.com/openagent/openagent) installed
- [Node.js](https://nodejs.org/) >= 18.0.0 installed
- Git installed

## Installation Steps

### 1. Install fuck-u-code CLI

```bash
npm install -g eff-u-code
```

### 2. Clone the fuck-u-code repository

```bash
git clone https://github.com/Zerone-Agent/fuck-u-code.git ~/.openagent/fuck-u-code
```

### 3. Symlink the skill

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/fuck-u-code-analysis
ln -s ~/.openagent/fuck-u-code/skills/fuck-u-code-analysis ~/.openagent/skills/fuck-u-code-analysis
```

### 4. Verify Installation

Restart OpenAgent, then try asking:
- "Analyze the code quality of this project with fuck-u-code"

If successful, OpenAgent will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openagent/fuck-u-code
git pull
```

## Uninstallation

```bash
rm -rf ~/.openagent/skills/fuck-u-code-analysis
```

## Getting Help

- GitHub: https://github.com/Zerone-Agent/fuck-u-code
- Report issues: https://github.com/Zerone-Agent/fuck-u-code/issues
