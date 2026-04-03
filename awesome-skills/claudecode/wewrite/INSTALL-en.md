# Installing WeWrite for Claude Code

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- Git installed
- Python 3 installed

## Installation Steps

### 1. Clone WeWrite Repository

```bash
git clone --depth 1 https://github.com/oaker-io/wewrite.git ~/.claude/wewrite
```

### 2. Create Symlink

Create a symlink so Claude Code discovers the skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/wewrite
ln -s ~/.claude/wewrite ~/.claude/skills/wewrite
```

### 3. Install Python Dependencies

```bash
cd ~/.claude/wewrite && pip install -r requirements.txt
```

### 4. Verify Installation

Restart Claude Code, then try asking:
- "do you have wewrite?"
- "write a WeChat official account article"

If successful, Claude Code will automatically recognize and invoke the WeWrite skill.

## Configuration (Optional)

To enable WeChat draft box publishing and AI image generation, create a configuration file:

```bash
cd ~/.claude/wewrite
cp config.example.yaml config.yaml
```

Edit `config.yaml` and fill in:
- WeChat Official Account `appid` and `secret` (for draft box publishing)
- Image API key (for AI image generation)

> **Note**: Core features work without configuration—the system automatically degrades to local HTML preview + image prompt output.

## Updating

```bash
cd ~/.claude/wewrite
git pull origin main
```

WeWrite automatically checks for new versions on each run. Say "update" to upgrade when available.

## Quick Start

```
You: write a WeChat article
You: write a WeChat article about AI Agents
You: interactive mode, write an article about productivity tools
You: show available themes          → theme gallery
You: switch to sspai theme          → switch theme
You: import exemplar                → build style library
You: learn my edits                 → flywheel learning
```

## Getting Help

- GitHub: https://github.com/oaker-io/wewrite
- Report issues: https://github.com/oaker-io/wewrite/issues
