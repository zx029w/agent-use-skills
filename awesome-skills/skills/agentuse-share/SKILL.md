---
name: agentuse-share
description: Use this skill whenever you need to add a new skill to awesome-skills, document an existing skill, create installation guides, or set up bilingual documentation. Trigger when user mentions "add skill", "document skill", "create install guide", "write skill introduction", "add to awesome-skills", or when working with the awesome-skills repository structure. Also trigger when asked to create bilingual (Chinese/English) documentation for any skill.
---

# AgentUse Share Skill

This skill defines the complete standardized workflow for adding a new Skill to the `awesome-skills` repository.

## Repository Directory Structure

```
awesome-skills/
├── skills/                        # Skill SKILL.md & scripts
│   └── <skill-name>/              # (Optional) Skill source directory
│       └── SKILL.md               #   Original SKILL.md provided by the skill author
├── introductions/                 # Skill introduction documents
│   ├── en/                        # English introductions
│   │   └── <skill-name>.md
│   └── zh/                        # Chinese introductions
│       └── <skill-name>.md
├── claudecode/                    # Claude Code platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── codex/                         # Codex platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── cursor/                        # Cursor platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── openclaw/                      # OpenClaw platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── openagent/                     # OpenAgent platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── opencode/                      # OpenCode platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
└── qoder/                         # Qoder platform install guides
    └── <skill-name>/
        ├── INSTALL-en.md
        └── INSTALL-zh.md
```

## Workflow

### Step 1: Research the Target Skill

First, check whether a `SKILL.md` file is already provided within this repository at `awesome-skills/skills/<skill-name>/SKILL.md`.

#### Case A: SKILL.md Already Exists in the Repository

If `awesome-skills/skills/<skill-name>/SKILL.md` exists, use it as the **primary source of information**:

- Read the `SKILL.md` file directly — it typically contains a comprehensive description of the skill, including its purpose, features, usage instructions, and workflow.
- Supplement with the skill's GitHub repository or official documentation **only if** the SKILL.md does not contain sufficient information (e.g., missing supported platforms list, or lacking detail on core philosophy).
- Focus on extracting the following from the SKILL.md:
  - **What it is**: The core definition and positioning of the Skill.
  - **Core philosophy**: What are the design principles.
  - **Key features and workflow**: What capabilities it provides and how it operates.
  - **Skills library composition**: What sub-skills are included.
  - **Supported platforms**: Determine exactly which AI coding agents/platforms the Skill supports. This is critical — only create installation guides for platforms that are explicitly supported. Skip any unsupported platforms entirely.

> **Tip**: The SKILL.md is typically more detailed and authoritative than a README. Use it as the foundation for writing the introduction documents in Steps 2 and 3 and the installation guides (INSTALL.md) in Step 4. **Please refer to the `content-research-writer` skill's writing style to ensure the generated documentation is professional, structured, and includes clear action items.** The content-research-writer skill is located at `awesome-skills/skills/content-research-writer/SKILL.md`.

#### Case B: No SKILL.md in the Repository

If no `SKILL.md` exists under `awesome-skills/skills/<skill-name>/`:

- Visit the target Skill's **GitHub repository** or official documentation.
- Use the `webfetch` tool (or equivalent URL fetching tool available in your environment) to fetch the README page content.
- Focus on gathering the following information:
  - **What it is**: The core definition and positioning of the Skill.
  - **Core philosophy**: What are the design principles.
  - **Key features and workflow**: What capabilities it provides and how it operates.
  - **Skills library composition**: What sub-skills are included.
  - **Supported platforms**: Determine exactly which AI coding agents/platforms the Skill supports (e.g., Claude Code, Cursor, Codex, OpenCode, OpenClaw, OpenAgent, Qoder). This is critical — only create installation guides for platforms that are explicitly supported. Skip any unsupported platforms entirely.

### Step 2: Write the Chinese Introduction Document

> If a `SKILL.md` was found in Step 1 (Case A), base the introduction on the information from that file. Summarize and restructure the content to fit the introduction template below. Do NOT copy the SKILL.md verbatim — instead, distill it into a concise, reader-friendly introduction.

- **File path**: `awesome-skills/introductions/zh/<skill-name>.md`
- **Content structure** (reference template):

```markdown
# <Skill Name>

**<Skill Name>** is ... (one-line summary)

## Tags (or ## 标签 for zh)

[Emoji] [Category] | [Emoji] [Status]

> **Strict Formatting Rules for Tags**:
> 1. Use a second-level heading: `## 标签` for Chinese documents, `## Tags` for English documents.
> 2. Leave exactly one blank line between the heading and the tags.
> 3. The tags content must be a single line in the format: `[Emoji] [Category] | [Emoji] [Status]`.
> 4. Use a pipe character with exactly one space on each side (` | `) as the separator.
> 5. **Common Categories (zh/en)**: `🧘 人生与哲学` / `🧘 Life & Philosophy`, `🗂️ 文档与办公` / `🗂️ Documents & Office`, `🎨 设计与创意` / `🎨 Design & Creativity`, `💻 开发与测试` / `💻 Development & Testing`, `🛠️ 效率工具` / `🛠️ Productivity Tools`.
> 6. **Common Statuses (zh/en)**: `✅ 已验证` / `✅ Verified`, `🔍 待验证` / `🔍 Pending Verification`.

## Core Philosophy
- Point 1
- Point 2
- ...

## Key Features & Workflow
1. **Feature A**: Description...
2. **Feature B**: Description...
...

## Skills Library Overview
- **Category 1**: List of sub-skills...
- **Category 2**: List of sub-skills...

## Installation & Support
<Skill Name> supports the following AI editors and platforms:
- [Claude Code](../../claudecode/<skill-name>/INSTALL-zh.md)   <!-- only if supported -->
- [Cursor](../../cursor/<skill-name>/INSTALL-zh.md)             <!-- only if supported -->
- [Codex](../../codex/<skill-name>/INSTALL-zh.md)               <!-- only if supported -->
- [OpenCode](../../opencode/<skill-name>/INSTALL-zh.md)         <!-- only if supported -->
- [OpenClaw](../../openclaw/<skill-name>/INSTALL-zh.md)         <!-- only if supported -->
- [OpenAgent](../../openagent/<skill-name>/INSTALL-zh.md)       <!-- only if supported -->
- [Qoder](../../qoder/<skill-name>/INSTALL-zh.md)               <!-- only if supported -->

---
For more information, visit: [GitHub - <repo>](<url>)
```

> **Note**: The Chinese introduction should be written in Chinese. The template above shows the structure only.

### Step 3: Write the English Introduction Document

> Same as Step 2 — if a `SKILL.md` exists, use it as the primary information source for the English version as well.

- **File path**: `awesome-skills/introductions/en/<skill-name>.md`
- Content should be the English translation of the Chinese version from Step 2.
- Ensure the `## Tags` section uses English terms and matching emojis, following the same strict format as the Chinese version:
  - Format: `[Emoji] [Category] | [Emoji] [Status]`
  - Example: `💻 Development & Testing | ✅ Verified` or `🗂️ Documents & Office | 🔍 Pending Verification`
- Installation links should point to `INSTALL-en.md` files.

### Step 4: Create Platform-Specific Installation Guides

Based on the supported platforms identified in **Step 1**, create bilingual installation guides **only** for those platforms. Skip any platform that the Skill does not support.

#### Installation Guide Format Requirements

**CRITICAL**: All installation guides MUST use bash commands that AI agents can execute. Do NOT use plugin commands like `/plugin install` or `/plugin marketplace add` because AI agents cannot execute these commands.

**Required Format** (for skills from external repositories):

```markdown
# Installing <Skill Name> for <Platform>

## Prerequisites

- [<Platform>](<platform-url>) installed
- Git installed

## Installation Steps

### 1. Clone <skill-repo>

```bash
git clone https://github.com/<org>/<skill-repo>.git ~/.<platform>/<skill-repo>
```

### 2. Symlink Skills

Create symlinks so <Platform> discovers the skills:

**For Claude Code**:

- Multi-skill repository (e.g., superpowers):
```bash
mkdir -p ~/.claude/skills
for skill in $(ls ~/.claude/<skill-repo>/skills); do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/<skill-repo>/skills/$skill ~/.claude/skills/$skill
done
```

- Single-skill repository:
```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/<skill-name>
ln -s ~/.claude/<skill-repo>/skills/<skill-name> ~/.claude/skills/<skill-name>
```

**For other platforms (Cursor, Codex, etc.)**:
```bash
mkdir -p ~/.<platform>/skills
rm -rf ~/.<platform>/skills/<skill-repo>
ln -s ~/.<platform>/<skill-repo>/skills ~/.<platform>/skills/<skill-repo>
```

### 3. Verify Installation

Restart <Platform>, then try asking:
- "do you have <skill-name>?"

If successful, <Platform> will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.<platform>/<skill-repo>
git pull
```

## Uninstallation

**For Claude Code**:

- Multi-skill repository:
```bash
for skill in $(ls ~/.claude/<skill-repo>/skills); do
  rm -rf ~/.claude/skills/$skill
done
```

- Single-skill repository:
```bash
rm -rf ~/.claude/skills/<skill-name>
```

**For other platforms**:
```bash
rm -rf ~/.<platform>/skills/<skill-repo>
```

## Getting Help

- GitHub: https://github.com/<org>/<skill-repo>
- Report issues: https://github.com/<org>/<skill-repo>/issues
```

**For skills from the agent-use-skills repository** (internal skills):

```markdown
# Installing <Skill Name> for <Platform>

## Prerequisites

- [<Platform>](<platform-url>) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.<platform>/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so <Platform> discovers the skill:

```bash
mkdir -p ~/.<platform>/skills
rm -rf ~/.<platform>/skills/<skill-name>
ln -s ~/.<platform>/agent-use-skills/awesome-skills/skills/<skill-name> ~/.<platform>/skills/<skill-name>
```

### 3. Verify Installation

Restart <Platform>, then try asking:
- "do you have <skill-name>?"

## Updating

```bash
cd ~/.<platform>/agent-use-skills
git pull
```

## Uninstallation

```bash
rm -rf ~/.<platform>/skills/<skill-name>
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
```

**Platform-specific directories**:

| Platform    | Skills Directory          | Clone Directory                    |
|-------------|---------------------------|-------------------------------------|
| Claude Code | `~/.claude/skills/`       | `~/.claude/` or `~/.claude/agent-use-skills/` |
| Cursor      | `~/.cursor/skills/`       | `~/.cursor/`                        |
| Codex       | `~/.codex/skills/`        | `~/.codex/`                         |
| OpenCode    | `~/.config/opencode/skills/` | `~/.config/opencode/`           |
| OpenClaw    | `~/.openclaw/skills/`     | `~/.openclaw/`                      |
| OpenAgent   | `~/.openagent/skills/`    | `~/.openagent/`                     |
| Qoder       | `~/.qoder/skills/`        | `~/.qoder/`                         |

Each installation guide should include:
1. **Prerequisites**: Required software and dependencies
2. **Installation steps**: Bash commands that AI agents can execute
3. **Verify installation**: How to confirm the installation was successful
4. **Update method**: How to update to the latest version
5. **Getting Help**: Links to GitHub repository and issue tracker

All available platforms and their corresponding file paths:

| Platform    | English                                            | Chinese                                            |
|-------------|----------------------------------------------------|----------------------------------------------------|
| Claude Code | `claudecode/<skill-name>/INSTALL-en.md`            | `claudecode/<skill-name>/INSTALL-zh.md`            |
| Codex       | `codex/<skill-name>/INSTALL-en.md`                 | `codex/<skill-name>/INSTALL-zh.md`                 |
| Cursor      | `cursor/<skill-name>/INSTALL-en.md`                | `cursor/<skill-name>/INSTALL-zh.md`                |
| OpenClaw    | `openclaw/<skill-name>/INSTALL-en.md`              | `openclaw/<skill-name>/INSTALL-zh.md`              |
| OpenAgent   | `openagent/<skill-name>/INSTALL-en.md`             | `openagent/<skill-name>/INSTALL-zh.md`             |
| OpenCode    | `opencode/<skill-name>/INSTALL-en.md`              | `opencode/<skill-name>/INSTALL-zh.md`              |
| Qoder       | `qoder/<skill-name>/INSTALL-en.md`                 | `qoder/<skill-name>/INSTALL-zh.md`                 |

> **Important**: Only create rows for platforms that the Skill actually supports, as determined during Step 1 research. Do NOT create installation guides for unsupported platforms.

### Step 5: Cross-Check

After all files are complete, perform the following checks:
1. **Link validity**: Ensure all installation guide links in the introduction documents have correct paths.
2. **Bilingual consistency**: Both language versions should have matching structure and content.
3. **Information accuracy**: Installation commands and steps should match the official documentation.

## Important Notes

- All documents must be provided in **both Chinese** (`-zh.md`) and **English** (`-en.md`) versions.
- The "Installation & Support" section in introduction documents should use a **hyperlinked list** pointing to each platform's installation guide, rather than embedding installation commands directly.
- File naming should use **kebab-case** (lowercase with hyphens), e.g., `superpowers`, `ui-ux-pro-max-skill`.
- If the target Skill's GitHub repository cannot be accessed via browser, use the `read_url_content` tool to fetch page content.
