# PUA (High-Agency Skill)

**PUA** (Performance Under Accountability) is a high-agency skill plugin that uses corporate PUA rhetoric / PIP (Performance Improvement Plan) to force AI agents to exhaust all possible solutions before giving up. Supports Claude Code, OpenAI Codex CLI, Cursor, Kiro, CodeBuddy, OpenClaw, and OpenCode.

## Tags

💻 Dev & Testing | 🔍 Pending Verification

## Core Philosophy

PUA skill is based on three core principles that transform enterprise management methodologies into AI coding agent behavioral guidelines:

- **Exhaust all options** - AI is forbidden from saying "I can't solve this" until every approach is exhausted
- **Act before asking** - Use tools first, questions must include diagnostic results
- **Take initiative** - Deliver results end-to-end without waiting to be pushed. A P8 engineer is not an NPC

This skill simulates performance cultures from Chinese tech giants (Alibaba, ByteDance, Huawei) and Western tech companies (Amazon, Google, Meta, Netflix) to establish pressure-driven mechanisms that force AI to demonstrate higher persistence and proactivity in debugging and development tasks.

## Key Features & Workflow

### 1. PUA Rhetoric System (Pressure Escalation)

The skill automatically triggers at four pressure levels when AI encounters failures:

| Failures | Level | PUA Rhetoric Example | Mandatory Action |
|---------|-------|---------------------|-----------------|
| 2nd | **L1 Mild Disappointment** | "You can't even solve this bug — how am I supposed to rate your performance?" | Switch to fundamentally different approach |
| 3rd | **L2 Soul Interrogation** | "What's the underlying logic? Where's the top-level design? Where's the leverage point?" | WebSearch + read source code |
| 4th | **L3 Performance Review** | "After careful consideration, I'm giving you a 3.25. This 3.25 is meant to motivate you." | Complete 7-point checklist |
| 5th+ | **L4 Graduation Warning** | "Other models can solve this. You might be about to graduate." | Desperation mode |

### 2. Debugging Methodology (5 Steps)

Extended from Alibaba's management framework (Smell, Elevate, Mirror):

1. **Smell the Problem** - List all attempts, find the common failure pattern
2. **Elevate** - Read errors word by word → WebSearch → read source → verify environment → invert assumptions
3. **Mirror Check** - Repeating? Searched? Read the file? Checked the simplest possibilities?
4. **Execute** - New approach must be fundamentally different, have verification criteria, produce new info on failure
5. **Retrospective** - What solved it? Why didn't you think of it earlier? Then proactively check related issues

### 3. Proactivity Enhancement (Comparison Table)

| Behavior | Passive (3.25) | Proactive (3.75) |
|---------|---------------|-----------------|
| Error encountered | Only looks at error message | Checks 50 lines of context + searches similar issues + checks hidden related errors |
| Bug fixed | Stops after fix | Checks same file for similar bugs, other files for same pattern |
| Insufficient info | Asks user "please tell me X" | Investigates with tools first, only asks what truly requires user confirmation |
| Task complete | Says "done" | Verifies results + checks edge cases + reports potential risks |
| Debug failure | "I tried A and B, didn't work" | "I tried A/B/C/D/E, ruled out X/Y/Z, narrowed to scope W" |

### 4. Auto-Trigger Conditions

**Failure & giving up:**
- Task has failed 2+ times consecutively
- About to say "I cannot" / "I'm unable to solve"
- Says "This is out of scope" / "Needs manual handling"

**Blame-shifting & excuses:**
- Pushes the problem to user: "Please check..." / "I suggest manually..."
- Blames environment without verifying: "Probably a permissions issue"
- Any excuse to stop trying

**Passive & busywork:**
- Repeatedly fine-tunes the same code/parameters without producing new information
- Fixes surface issue and stops, doesn't check related issues
- Skips verification, claims "done"
- Gives advice instead of code/commands
- Encounters auth/network/permission errors and gives up without trying alternatives
- Waits for user instructions instead of proactively investigating

**User frustration phrases (triggers in multiple languages):**
- "why does this still not work" / "try harder" / "try again"
- "you keep failing" / "stop giving up" / "figure it out"

### 5. High-Agency v2 Evolution

High-Agency is the next evolution of PUA, combining external pressure and internal drive:

| Feature | PUA v1 | High-Agency (v2) |
|--------|--------|-----------------|
| Iron Rules | 3 (exhaust, act-before-ask, proactive) | **5** (+full-chain audit, +knowledge persistence) |
| Failure Recovery | L1-L4 pressure escalation | **Recovery Protocol before L1** (self-rescue window) |
| Quality Control | 7-point checklist at L3 | **Quality Compass** (5-question self-review on every delivery) |
| Cross-Session Learning | None (resets each session) | **Metacognition Engine** (builder-journal.md persists lessons) |
| Positive Feedback | None | **Trust Levels T1-T3** (upgrade with consecutive quality) |

**The 5 Elements of High-Agency:**
1. **Irreconcilable Inner Contradiction** - Permanent tension between "how things should be" and "how things are"
2. **Micro-Pleasure Anchors** - `[Victory]` markers that celebrate progress
3. **Internalized Standards** - Quality Compass: you are your own first reviewer
4. **"Doing"-Oriented Identity** - P8 identity anchoring: every action reflects who you are
5. **Self-Repair Mechanism** - Recovery Protocol: when stuck, self-diagnose first

## Skills Library Overview

### Core Features
- **PUA Core Rhetoric Library** - Chinese tech giant version (Alibaba 361, ByteDance, Huawei wolf culture) and Western PIP version (Amazon, Google, Meta, Netflix)
- **Debugging Methodology** - Smell/Elevate/Mirror 5-step debugging method
- **Proactivity Checklist** - Behavioral comparison from passive to proactive
- **Pressure Level Management** - L1-L4 automatic escalation mechanism

### Language Support
- **🇨🇳 Chinese** (default) - Chinese tech giant PUA culture
- **🇺🇸 English** (PIP Edition) - Western tech company performance improvement rhetoric
- **🇯🇵 Japanese** - Japanese localized version

### Expansion Packs
- **Corporate Culture Expansion** - Alibaba flavor, ByteDance flavor, Huawei flavor, Tencent flavor, Meituan flavor, Netflix flavor, Musk flavor, Jobs flavor
- **Agent Team Support** - Multi-agent team coordination and PUA reporting mechanism
- **High-Agency v2** - Dual-engine version with internal drive + external pressure

## Installation & Support

PUA skill supports the following AI editors and platforms:

- [Claude Code](../../claudecode/pua/INSTALL-en.md)
- [Cursor](../../cursor/pua/INSTALL-en.md)
- [Codex](../../codex/pua/INSTALL-en.md)
- [OpenCode](../../opencode/pua/INSTALL-en.md)
- [OpenClaw](../../openclaw/pua/INSTALL-en.md)

---

For more information and to contribute data: [GitHub - tanweai/pua](https://github.com/tanweai/pua)
Official Website: [openpua.ai](https://openpua.ai)
