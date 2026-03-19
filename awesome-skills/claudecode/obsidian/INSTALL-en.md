# Obsidian Skills Installation Guide (Claude Code)

This guide explains how to install and configure Obsidian Skills in Claude Code.

## Installation Methods

### Method 1: Via Marketplace (Recommended)

Execute the following commands in Claude Code:

```bash
/plugin marketplace add kepano/obsidian-skills
/plugin install obsidian@obsidian-skills
```

### Method 2: Using npx

```bash
npx skills add git@github.com:kepano/obsidian-skills.git
```

### Method 3: Manual Installation

1. Clone the repository locally:

```bash
git clone https://github.com/kepano/obsidian-skills.git
```

2. Copy the repository contents to the `/.claude` folder in your Obsidian Vault root:

```bash
cp -r obsidian-skills/* /path/to/your/vault/.claude/
```

Or create a symbolic link (recommended for easy updates):

```bash
ln -s /path/to/obsidian-skills /path/to/your/vault/.claude
```

## Verify Installation

After installation, restart Claude Code and test the following features:

1. **Test Markdown Skill**:
   - Try creating a note with wikilinks: `[[Another Note]]`
   - Test callouts: Use `> [!note]` syntax

2. **Test Bases Skill**:
   - Create a `.base` file
   - Define views and filters

3. **Test Canvas Skill**:
   - Create a `.canvas` file
   - Add nodes and edges

4. **Test CLI Skill**:
   - Run `obsidian help` to see available commands

## Update Method

### Update via Marketplace

```bash
/plugin update obsidian@obsidian-skills
```

### Manual Update

If installed via git clone:

```bash
cd /path/to/obsidian-skills
git pull
```

If using a symbolic link, updates will automatically sync to Claude Code.

## Detailed Documentation

- [Claude Code Official Skills Documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Obsidian Skills GitHub](https://github.com/kepano/obsidian-skills)
- [Agent Skills Specification](https://agentskills.io/specification)
