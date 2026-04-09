# Installing Qiushi Skill for OpenCode

## Prerequisites

- OpenCode installed
- Git installed

## Installation Steps

OpenCode recommends using the "manual skill file loading" approach to avoid hiding platform differences in documentation promises.

### 1. Clone Repository Locally

```bash
git clone https://github.com/HughYau/qiushi-skill
```

### 2. Use Entry Skill as Session Start Methodology

Use `skills/arming-thought/SKILL.md` as the starting methodology entry point for new sessions.

### 3. Load Specific Skills as Needed

After specific tasks begin, read corresponding `skills/*/SKILL.md` as needed:
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

### 4. Load Command Files (Optional)

If OpenCode supports command directories, also load `commands/`; otherwise directly read corresponding command file content.

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

Check the following points:
- Entry skill only does routing and constraining, won't override host system rules
- Command files and skill files correspond one-to-one
- Platform descriptions in documentation match your actual installation method

## Updating

```bash
cd qiushi-skill
git pull
```

## Getting Help

- GitHub: https://github.com/HughYau/qiushi-skill
- Report issues: https://github.com/HughYau/qiushi-skill/issues
- OpenCode usage guide: https://github.com/HughYau/qiushi-skill/blob/main/docs/README.opencode.md