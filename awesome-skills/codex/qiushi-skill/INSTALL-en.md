# Installing Qiushi Skill for Codex

## Prerequisites

- Codex installed
- Git installed

## Installation Steps

Codex does not rely on Claude/Cursor plugin shells. The core approach is: treat `skills/` as a methodology skill library, and `commands/` as optional manual command templates.

### 1. Clone Repository Locally

```bash
git clone https://github.com/HughYau/qiushi-skill
```

### 2. Load Entry Skill at Session Start

Have Codex read `skills/arming-thought/SKILL.md` as the routing and methodology constraint.

### 3. Load Skills as Needed for Specific Tasks

Based on task type, read the following files as needed:
- `skills/contradiction-analysis/SKILL.md` — Contradiction Analysis
- `skills/practice-cognition/SKILL.md` — Practice-Cognition
- `skills/investigation-first/SKILL.md` — Investigation
- `skills/mass-line/SKILL.md` — Mass Line
- `skills/criticism-self-criticism/SKILL.md` — Criticism & Self-Criticism
- `skills/protracted-strategy/SKILL.md` — Protracted Strategy
- `skills/concentrate-forces/SKILL.md` — Concentrate Forces
- `skills/spark-prairie-fire/SKILL.md` — Spark Prairie Fire
- `skills/overall-planning/SKILL.md` — Overall Planning
- `skills/workflows/SKILL.md` — Workflow Combinations

### 4. Load Command Templates (Optional)

If Codex supports Markdown commands, additionally load `commands/` directory as manual entry points; if not supported, directly read the content of corresponding command files.

### 5. Verify Installation

#### macOS / Linux:

```bash
cd qiushi-skill
bash tests/validate.sh
```

#### Windows:

```powershell
cd qiushi-skill
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File tests/validate.ps1
```

Validation script checks:
- JSON configuration validity
- Hook and command files completeness
- `SKILL.md` / agent / command frontmatter completeness
- Local Markdown links and image paths existence

## Verify Installation Success

Manually verify two points:
- Successfully read `arming-thought` at session start
- Switch to corresponding skill as needed for specific problems, not mechanically calling all skills

## Updating

```bash
cd qiushi-skill
git pull
```

## Getting Help

- GitHub: https://github.com/HughYau/qiushi-skill
- Report issues: https://github.com/HughYau/qiushi-skill/issues
- Codex usage guide: https://github.com/HughYau/qiushi-skill/blob/main/docs/README.codex.md