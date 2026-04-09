# Installing Qiushi Skill for Claude Code

## Prerequisites

- **Windows**: Uses PowerShell hook by default, no need for additional Bash installation
- **macOS / Linux**: Requires available `bash` or `sh`
- **Validation Scripts**: Built-in `tests/validate.sh` (macOS/Linux) and `tests/validate.ps1` (Windows) for post-installation verification

## Installation Steps

### Method A: Install via Claude Plugin Hub (Recommended)

One-click installation in terminal:

```bash
npx claudepluginhub hughyau/qiushi-skill
```

Or manually install via Marketplace in Claude Code:

1. Add Marketplace (execute once only):
   ```
   /plugin marketplace add https://www.claudepluginhub.com/api/plugins/hughyau-qiushi-skill/marketplace.json
   ```

2. Install plugin:
   ```
   /plugin install hughyau-qiushi-skill@cpd-hughyau-qiushi-skill
   ```

### Method B: Clone from Source

```bash
git clone https://github.com/HughYau/qiushi-skill
cd qiushi-skill
claude --plugin-dir .
```

`--plugin-dir` loads the plugin in current session. To auto-load in every session, set a shell alias:

```bash
# Add to ~/.bashrc or ~/.zshrc
alias claude='claude --plugin-dir /path/to/qiushi-skill'
```

## Verify Installation

### macOS / Linux Verification:

```bash
bash tests/validate.sh
```

- Hook entry uses `hooks/session-start`
- Ensure `bash` or `sh` is available on system

### Windows Verification:

```powershell
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File tests/validate.ps1
```

- Since `1.2.0`, SessionStart hook prioritizes native PowerShell, no longer depends on Git Bash / WSL
- If PowerShell script execution is disabled in your environment, use `-ExecutionPolicy Bypass` to run the validation script

Validation script checks:
- JSON configuration validity
- Hook and command files completeness
- `SKILL.md` / agent / command frontmatter completeness
- Local Markdown links and image paths existence
- Windows hook native PowerShell output parseability

## Updating

If using Method A (Plugin Hub):

```bash
npx claudepluginhub hughyau/qiushi-skill --update
```

If using Method B (Source clone):

```bash
cd qiushi-skill
git pull
```

## Getting Help

- GitHub: https://github.com/HughYau/qiushi-skill
- Report issues: https://github.com/HughYau/qiushi-skill/issues
- Platform details: https://github.com/HughYau/qiushi-skill/blob/main/docs/platforms.md