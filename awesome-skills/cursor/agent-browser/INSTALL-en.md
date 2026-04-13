# Install Agent Browser in Cursor

## Prerequisites

- [Cursor](https://cursor.sh) installed
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
git clone https://github.com/vercel-labs/agent-browser.git ~/.cursor/agent-browser
```

### 3. Configure Skill in Cursor

Create a symbolic link so Cursor can find and use the skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/agent-browser
ln -s ~/.cursor/agent-browser/skills/agent-browser ~/.cursor/skills/agent-browser
```

## Verify Installation

Restart Cursor and try:

- "Open google.com and tell me the reference ID of the search box"
- "do you have agent-browser skill?"

## Update

1. **Update CLI**: `npm update -g agent-browser`
2. **Update Skill Library**: `cd ~/.cursor/agent-browser && git pull`

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/agent-browser
```

## Get Help

- Skill issues: https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser
- CLI issues: https://github.com/vercel-labs/agent-browser/issues
