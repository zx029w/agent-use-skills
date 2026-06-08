# Installing Fuck-U-Code Analysis for Qoder

## Prerequisites

- [Qoder](https://github.com/qoder/qoder) installed
- [Node.js](https://nodejs.org/) >= 18.0.0 installed
- Git installed

## Installation Steps

### 1. Install fuck-u-code CLI

```bash
npm install -g eff-u-code
```

### 2. Clone the fuck-u-code repository

```bash
git clone https://github.com/Zerone-Agent/fuck-u-code.git ~/.qoder/fuck-u-code
```

### 3. Symlink the skill

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/fuck-u-code-analysis
ln -s ~/.qoder/fuck-u-code/skills/fuck-u-code-analysis ~/.qoder/skills/fuck-u-code-analysis
```

### 4. Verify Installation

Restart Qoder, then try asking:
- "Analyze the code quality of this project with fuck-u-code"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/fuck-u-code
git pull
```

## Uninstallation

```bash
rm -rf ~/.qoder/skills/fuck-u-code-analysis
```

## Getting Help

- GitHub: https://github.com/Zerone-Agent/fuck-u-code
- Report issues: https://github.com/Zerone-Agent/fuck-u-code/issues
