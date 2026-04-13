# Installing Deep Research for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- Python and pip installed
- Google AI API Key (for Gemini Deep Research)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/deep-research
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/deep-research ~/.openagent/skills/deep-research
```

### 3. Configure API Key

Set the Google AI API Key environment variable:

```bash
export GOOGLE_AI_API_KEY="your-api-key-here"
```

### 4. Verify Installation

Restart OpenAgent and try asking:
- "Research the current state of AI programming assistants market"
- "do you have deep-research?"

If successful, OpenAgent will automatically recognize and invoke the Deep Research skill workflow.

## Updating

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/deep-research
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues