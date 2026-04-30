# Huashu Design - Cursor Installation Guide

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.cursor/huashu-design
```

### 2. Create Symlink

```bash
mkdir -p ~/.cursor/skills
ln -sf ~/.cursor/huashu-design ~/.cursor/skills/huashu-design
```

### 3. Verify Installation

Try the following in Cursor's Agent mode:

```
Build an AI Pomodoro timer iOS prototype with 4 core screens that are actually clickable
```

If the skill is loaded correctly, the AI will automatically recognize and invoke the Huashu Design workflow.

## Updating

```bash
cd ~/.cursor/huashu-design && git pull
```

## Uninstallation

```bash
rm ~/.cursor/skills/huashu-design
```

## Getting Help

- GitHub Repository: https://github.com/alchaincyf/huashu-design
- Report Issues: https://github.com/alchaincyf/huashu-design/issues
