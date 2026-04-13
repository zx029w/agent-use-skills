# Install Agent Browser in Claude Code

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) installed
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
git clone https://github.com/vercel-labs/agent-browser.git ~/.claude/agent-browser
```

### 3. Configure Skill in Claude Code

Create a symbolic link so Claude Code can find and use the skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/agent-browser
ln -s ~/.claude/agent-browser/skills/agent-browser ~/.claude/skills/agent-browser
```

## Verify Installation

Restart Claude Code and try:

- "Open google.com and tell me the reference ID of the search box"
- "do you have agent-browser skill?"

## Update

1. **Update CLI**: `npm update -g agent-browser`
2. **Update Skill Library**: `cd ~/.claude/agent-browser && git pull`

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.claude/skills/agent-browser
```

## Get Help

- Skill issues: https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser
- CLI issues: https://github.com/vercel-labs/agent-browser/issues
