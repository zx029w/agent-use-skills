# Installing Skill Creator for OpenCode

## Prerequisites

- [OpenCode](https://github.com/opencode-ai/opencode) installed
- Git installed
- Python 3.8+ (for running evaluation scripts)

## Installation Steps

### 1. Clone anthropics/skills Repository

```bash
git clone https://github.com/anthropics/skills.git ~/.config/opencode/anthropics-skills
```

### 2. Create Symlink

Create a symlink so OpenCode discovers the skill-creator skill:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/skill-creator
ln -s ~/.config/opencode/anthropics-skills/skills/skill-creator ~/.config/opencode/skills/skill-creator
```

### 3. Verify Installation

Restart OpenCode, then try asking:
- "I need to create a new skill, please help me use skill-creator"
- "do you have skill-creator?"

If successful, OpenCode will automatically recognize and invoke the Skill Creator skill workflow.

## Usage

Skill Creator is a skill for creating and improving skills. Its main features include:

1. **Create New Skills**: Build a complete skill from scratch
2. **Improve Existing Skills**: Iteratively optimize skill performance
3. **Run Test Evaluations**: Generate test cases and evaluate skill effectiveness
4. **Optimize Skill Descriptions**: Improve skill triggering accuracy

## Updating

```bash
cd ~/.config/opencode/anthropics-skills
git pull
```

## Getting Help

- GitHub Repository: https://github.com/anthropics/skills
- Report Issues: https://github.com/anthropics/skills/issues