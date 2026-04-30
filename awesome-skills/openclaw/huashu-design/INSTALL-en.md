# Huashu Design - OpenClaw Installation Guide

## Prerequisites

- OpenClaw installed
- Git installed

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.openclaw/huashu-design
```

### 2. Create Symlink

```bash
mkdir -p ~/.openclaw/skills
ln -sf ~/.openclaw/huashu-design ~/.openclaw/skills/huashu-design
```

### 3. Verify Installation

Restart OpenClaw, then try:

```
Build an AI Pomodoro timer iOS prototype with 4 core screens that are actually clickable
```

If the skill is loaded correctly, the AI will automatically recognize and invoke the Huashu Design workflow.

## Updating

```bash
cd ~/.openclaw/huashu-design && git pull
```

## Uninstallation

```bash
rm ~/.openclaw/skills/huashu-design
```

## Getting Help

- GitHub Repository: https://github.com/alchaincyf/huashu-design
- Report Issues: https://github.com/alchaincyf/huashu-design/issues
