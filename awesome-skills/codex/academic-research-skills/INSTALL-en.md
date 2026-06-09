# Installing Academic Research Skills for Codex CLI

> **Note**: The Codex version of Academic Research Skills comes from a **separate sibling repository** [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex), packaged as a single skill `$academic-research-suite` containing all ARS workflows.

## Prerequisites

- [Codex CLI](https://github.com/openai/codex) installed
- Python 3 installed
- Git installed

## Installation Steps

Install using the Codex skill-installer script:

```bash
python3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo Imbad0202/academic-research-skills-codex \
  --ref main \
  --path skills/academic-research-suite \
  --method git
```

After installation, open a new Codex conversation. Existing sessions may keep their old skill cache; you do not need to close unrelated Claude or Codex sessions.

### Verify Installation

In a new Codex conversation, run:

```
/skills
```

You should see one ARS entry: `academic-research-suite` or `Academic Research ...`. You should **not** see separate `academic-paper`, `academic-pipeline`, `deep-research`, or `academic-paper-reviewer` skills.

Test the routing:

```
Use $academic-research-suite.
I want to write a paper on AI adoption in higher education quality assurance.
I do not yet have a clear research question.
```

If successful, ARS will route to `deep-research` `socratic` mode and start asking narrowing questions.

## Updating

```bash
rm -rf "$HOME/.codex/skills/academic-research-suite"
python3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo Imbad0202/academic-research-skills-codex \
  --ref main \
  --path skills/academic-research-suite \
  --method git
```

Open a new Codex conversation after updating.

## Usage

Invoke the suite in Codex with `$academic-research-suite`:

```
Use $academic-research-suite to help me plan a systematic literature review on AI adoption.
```

Claude-style aliases are also available (e.g., `ars-plan`, `ars-reviewer`, `ars-lit-review`, etc.).

## Uninstallation

```bash
rm -rf "$HOME/.codex/skills/academic-research-suite"
```

## Getting Help

- GitHub (Codex version): https://github.com/Imbad0202/academic-research-skills-codex
- Original project: https://github.com/Imbad0202/academic-research-skills
- Report issues: https://github.com/Imbad0202/academic-research-skills-codex/issues
