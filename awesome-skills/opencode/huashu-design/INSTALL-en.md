# Huashu Design - OpenCode Installation Guide

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.config/opencode/huashu-design
```

### 2. Create Symlink

```bash
mkdir -p ~/.config/opencode/skills
ln -sf ~/.config/opencode/huashu-design ~/.config/opencode/skills/huashu-design
```

### 3. Verify Installation

Restart OpenCode, then try:

```
Create a presentation deck about AI psychology, suggest 3 style directions for me to choose
```

If the skill is loaded correctly, the AI will automatically recognize and invoke the Huashu Design workflow.

## Updating

```bash
cd ~/.config/opencode/huashu-design && git pull
```

## Uninstallation

```bash
rm ~/.config/opencode/skills/huashu-design
```

## Getting Help

- GitHub Repository: https://github.com/alchaincyf/huashu-design
- Report Issues: https://github.com/alchaincyf/huashu-design/issues
