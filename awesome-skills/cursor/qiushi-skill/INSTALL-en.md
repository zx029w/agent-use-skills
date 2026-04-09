# Installing Qiushi Skill for Cursor

## Prerequisites

- **Windows**: Uses PowerShell hook by default, no need for additional Bash installation
- **macOS / Linux**: Requires available `bash` or `sh`
- **Validation Scripts**: Built-in `tests/validate.sh` (macOS/Linux) and `tests/validate.ps1` (Windows) for post-installation verification

## Installation Steps

### 1. Clone Repository Locally

```bash
git clone https://github.com/HughYau/qiushi-skill
```

### 2. Add Project Directory to Cursor Plugin Path

Configure Cursor's plugin path to recognize `.cursor-plugin/plugin.json`.

### 3. Verify Plugin Configuration Recognition

Ensure the following files are properly recognized by Cursor:
- `.cursor-plugin/plugin.json`
- `commands/` directory
- `hooks/hooks.json`

### 4. Run Validation Script

Check that hooks and command files are complete:

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

## Updating

```bash
cd qiushi-skill
git pull
```

## Getting Help

- GitHub: https://github.com/HughYau/qiushi-skill
- Report issues: https://github.com/HughYau/qiushi-skill/issues
- Platform details: https://github.com/HughYau/qiushi-skill/blob/main/docs/platforms.md