# Install Agent Browser in Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
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
git clone https://github.com/vercel-labs/agent-browser.git ~/.qoder/agent-browser
```

### 3. Configure Skill in Qoder

Create a symbolic link so Qoder can find and use the skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/agent-browser
ln -s ~/.qoder/agent-browser/skills/agent-browser ~/.qoder/skills/agent-browser
```

## Verify Installation

Restart Qoder and try:

- "Open google.com and tell me the reference ID of the search box"
- "do you have agent-browser skill?"

## Update

1. **Update CLI**: `npm update -g agent-browser`
2. **Update Skill Library**: `cd ~/.qoder/agent-browser && git pull`

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.qoder/skills/agent-browser
```

## Get Help

- Skill issues: https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser
- CLI issues: https://github.com/vercel-labs/agent-browser/issues
