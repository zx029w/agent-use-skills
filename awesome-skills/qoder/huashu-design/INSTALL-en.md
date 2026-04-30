# Huashu Design - Qoder Installation Guide

## Prerequisites

- Qoder installed
- Git installed

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.qoder/huashu-design
```

### 2. Create Symlink

```bash
mkdir -p ~/.qoder/skills
ln -sf ~/.qoder/huashu-design ~/.qoder/skills/huashu-design
```

### 3. Verify Installation

Restart Qoder, then try:

```
Create an infographic showing AI industry trends, print-grade quality
```

If the skill is loaded correctly, the AI will automatically recognize and invoke the Huashu Design workflow.

## Updating

```bash
cd ~/.qoder/huashu-design && git pull
```

## Uninstallation

```bash
rm ~/.qoder/skills/huashu-design
```

## Getting Help

- GitHub Repository: https://github.com/alchaincyf/huashu-design
- Report Issues: https://github.com/alchaincyf/huashu-design/issues
