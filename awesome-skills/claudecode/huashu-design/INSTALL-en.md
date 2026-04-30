# Huashu Design - Claude Code Installation Guide

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- Git installed

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.claude/huashu-design
```

### 2. Create Symlink

```bash
mkdir -p ~/.claude/skills
ln -sf ~/.claude/huashu-design ~/.claude/skills/huashu-design
```

### 3. Verify Installation

Restart Claude Code, then try:

```
Create a presentation deck about AI psychology, suggest 3 style directions for me to choose
```

If the skill is loaded correctly, the AI will automatically recognize and invoke the Huashu Design workflow.

## Updating

```bash
cd ~/.claude/huashu-design && git pull
```

## Uninstallation

```bash
rm ~/.claude/skills/huashu-design
```

## Getting Help

- GitHub Repository: https://github.com/alchaincyf/huashu-design
- Report Issues: https://github.com/alchaincyf/huashu-design/issues
