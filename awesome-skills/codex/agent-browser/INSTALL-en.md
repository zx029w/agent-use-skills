# Install Agent Browser in Codex

## Prerequisites

- [Codex](https://github.com/codex-editor/codex) installed
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
git clone https://github.com/vercel-labs/agent-browser.git ~/.codex/agent-browser
```

### 3. Configure Skill in Codex

Create a symbolic link so Codex can find and use the skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/agent-browser
ln -s ~/.codex/agent-browser/skills/agent-browser ~/.codex/skills/agent-browser
```

## Verify Installation

Restart Codex and try:

- "Open google.com and tell me the reference ID of the search box"
- "do you have agent-browser skill?"

## Update

1. **Update CLI**: `npm update -g agent-browser`
2. **Update Skill Library**: `cd ~/.codex/agent-browser && git pull`

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.codex/skills/agent-browser
```

## Get Help

- Skill issues: https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser
- CLI issues: https://github.com/vercel-labs/agent-browser/issues
