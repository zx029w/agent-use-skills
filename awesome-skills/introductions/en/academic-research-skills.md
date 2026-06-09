# Academic Research Skills

**Academic Research Skills (ARS)** is a comprehensive AI collaboration suite for the full academic research pipeline — from deep research and paper writing to peer review and final publication. Powered by 40+ specialized agents working together under a human-in-the-loop philosophy, ARS handles the grunt work so researchers can focus on what actually requires human thinking.

## Tags

🗂️ Documents & Office | 🔍 Pending Verification

## Core Philosophy

- **AI is your copilot, not the pilot**: ARS doesn't write papers for you. It handles reference hunting, citation formatting, data verification, and logical consistency checks — so you can focus on defining the question, choosing the method, interpreting data, and crafting arguments.
- **Human-in-the-loop, not full automation**: Based on Lu et al. (2026, *Nature*) analysis of autonomous AI research system failure modes, ARS places integrity gates at multiple stages. Every stage in the 10-stage pipeline requires user confirmation checkpoints; integrity verification (Stage 2.5 + 4.5) cannot be skipped.
- **Anti-sycophancy & anti-frame-lock**: Built-in mechanisms include a Concession Threshold Protocol (DA must score rebuttals before conceding), Intent Detection Layer (distinguishes exploratory vs. goal-oriented dialogue), and Dialogue Health Indicator — combating AI's inherent sycophancy and frame-lock tendencies.
- **Citation integrity assurance**: Based on Zhao et al. (2026) audit of 2.5M papers and 111M references, ARS v3.8+ implements three-layer citation anchoring, optional claim audit (`ARS_CLAIM_AUDIT=1`), and a deterministic citation-existence verification gate (four-index cross-check: Semantic Scholar + OpenAlex + Crossref + arXiv).

## Key Features & Workflow

1. **Deep Research**: 13-agent research team with 7 modes — full research, quick brief, PRISMA systematic review, Socratic guided, fact-check, literature review, and research quality review. Supports Semantic Scholar API verification and optional cross-model verification.
2. **Academic Paper**: 12-agent writing pipeline with 10 modes — full writing, guided planning, outline generation, revision, revision coaching, abstract generation, literature review paper, format conversion (APA 7.0/Chicago/MLA/IEEE/Vancouver), citation check, and AI disclosure. Supports Style Calibration and Writing Quality Check.
3. **Paper Reviewer**: 7-agent multi-perspective review with EIC + 3 dynamic reviewers + Devil's Advocate, using a 0-100 quality rubric (≥80 Accept, 65-79 Minor Revision, 50-64 Major Revision, <50 Reject). Supports 6 modes — full review, quick assessment, guided improvement, methodology focus, re-review, and calibration.
4. **Academic Pipeline**: 10-stage orchestrator from Stage 0 intent classification to Stage 6 process summary, featuring adaptive checkpoints, claim verification, Material Passport, optional cross-model integrity verification, score trajectory tracking, and Collaboration Depth Observer. Integrity gates at Stage 2.5/4.5 are mandatory and cannot be skipped.

## Skills Library Overview

- **Research**: Deep Research — full research, quick brief, PRISMA systematic review, Socratic guided, fact-check, literature review, research review
- **Writing**: Academic Paper — full writing, planning, outline, revision, revision coaching, abstract, literature review paper, format conversion, citation check, AI disclosure
- **Review**: Paper Reviewer — full review, quick assessment, guided improvement, methodology focus, re-review, calibration
- **Orchestration**: Pipeline — 10-stage end-to-end pipeline with mid-entry support (existing paper enters at Stage 2.5, reviewer comments enter at Stage 4)

## Supported Languages & Formats

- **Writing languages**: Traditional Chinese (default for Chinese input), English (default for English input), bilingual abstracts
- **Citation formats**: APA 7.0 (default), Chicago, MLA, IEEE, Vancouver
- **Paper structures**: IMRaD, Thematic Literature Review, Theoretical Analysis, Case Study, Policy Brief, Conference Paper
- **Output formats**: Markdown + DOCX (via Pandoc) + LaTeX (APA 7.0 `apa7` class) → PDF

## Cost & Performance

| Metric | Value |
|--------|-------|
| Full pipeline (15k-word paper) | ~$4–6 |
| Recommended settings | Skip Permissions mode, Agent Team optional |

## Installation & Support

Academic Research Skills is distributed as a Claude Code plugin, with a Codex CLI adapter also available:

- [Claude Code](../../claudecode/academic-research-skills/INSTALL-en.md) (plugin install, recommended)
- [Codex](../../codex/academic-research-skills/INSTALL-en.md) (skill package install)

---
For more information, visit: [GitHub - Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)
