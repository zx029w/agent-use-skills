# Installing Skill Creator for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed
- Python 3.8+ (for running evaluation scripts)

## Installation Steps

### 1. Clone anthropics/skills Repository

```bash
git clone https://github.com/anthropics/skills.git ~/.claude/anthropics-skills
```

### 2. Create Symlink

Create a symlink so Claude Code discovers the skill-creator skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/skill-creator
ln -s ~/.claude/anthropics-skills/skills/skill-creator ~/.claude/skills/skill-creator
```

### 3. Verify Installation

Restart Claude Code, then try asking:
- "I need to create a new skill, please help me use skill-creator"
- "do you have skill-creator?"

If successful, Claude Code will automatically recognize and invoke the Skill Creator skill workflow.

## Usage

Skill Creator is a skill for creating and improving skills. Its main features include:

1. **Create New Skills**: Build a complete skill from scratch
2. **Improve Existing Skills**: Iteratively optimize skill performance
3. **Run Test Evaluations**: Generate test cases and evaluate skill effectiveness
4. **Optimize Skill Descriptions**: Improve skill triggering accuracy

## Updating

```bash
cd ~/.claude/anthropics-skills
git pull
```

## Getting Help

- GitHub Repository: https://github.com/anthropics/skills
- Report Issues: https://github.com/anthropics/skills/issues