# Huashu Design - Codex Installation Guide

## Prerequisites

- Codex CLI installed
- Git installed

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.codex/huashu-design
```

### 2. Create Symlink

```bash
mkdir -p ~/.codex/skills
ln -sf ~/.codex/huashu-design ~/.codex/skills/huashu-design
```

### 3. Verify Installation

Restart Codex CLI, then try:

```
Turn this logic into a 60-second animation, export as MP4 and GIF
```

If the skill is loaded correctly, the AI will automatically recognize and invoke the Huashu Design workflow.

## Updating

```bash
cd ~/.codex/huashu-design && git pull
```

## Uninstallation

```bash
rm ~/.codex/skills/huashu-design
```

## Getting Help

- GitHub Repository: https://github.com/alchaincyf/huashu-design
- Report Issues: https://github.com/alchaincyf/huashu-design/issues
