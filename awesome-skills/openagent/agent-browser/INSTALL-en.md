# Install Agent Browser in OpenAgent

## Prerequisites

- OpenAgent installed
- Node.js and npm installed
- Git installed

## Installation Steps

### 1. Install Core CLI

Agent Browser is a global CLI tool. Install it via npm first:

```bash
npm install -g agent-browser
agent-browser install --with-deps
```

### 2. Clone agent-browser repository

Clone the skills library to your local machine:

```bash
git clone https://github.com/vercel-labs/agent-browser.git ~/.openagent/agent-browser
```

### 3. Configure Skill in OpenAgent

Create a symbolic link so OpenAgent can find and use the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/agent-browser
ln -s ~/.openagent/agent-browser/skills/agent-browser ~/.openagent/skills/agent-browser
```

## Verify Installation

Restart OpenAgent and try:

- "Open google.com and tell me the reference ID of the search box"
- "do you have agent-browser skill?"

## Update

1. **Update CLI**: `npm update -g agent-browser`
2. **Update Skill Library**: `cd ~/.openagent/agent-browser && git pull`

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.openagent/skills/agent-browser
```

## Get Help

- Skill issues: https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser
- CLI issues: https://github.com/vercel-labs/agent-browser/issues
