# Installing WeWrite for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- Node.js and npm installed

## Installation Steps

### 1. Clone wewrite

```bash
git clone https://github.com/oaker-io/wewrite.git ~/.openagent/wewrite
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/wewrite
ln -s ~/.openagent/wewrite/skills/wewrite ~/.openagent/skills/wewrite
```

### 3. Install Dependencies (Optional)

For full functionality, install dependencies:

```bash
cd ~/.openagent/wewrite
npm install
pip install -r requirements.txt  # Python script dependencies
```

### 4. Verify Installation

Restart OpenAgent and try asking:
- "Help me write a WeChat article"
- "do you have wewrite?"

If successful, OpenAgent will automatically recognize and invoke the WeWrite skill workflow.

## Updating

```bash
cd ~/.openagent/wewrite
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/wewrite
```

## Getting Help

- GitHub: https://github.com/oaker-io/wewrite