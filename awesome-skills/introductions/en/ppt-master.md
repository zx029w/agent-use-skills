# PPT Master

**PPT Master** is an AI-driven multi-format content generation system that converts source documents (PDF, DOCX, URL, Markdown, etc.) into natively editable PPTX presentations — every shape, text box, and chart is a real PowerPoint element, clickable and editable.

## Tags

🗂️ Documents & Office | 🔍 Pending Verification

## Core Philosophy
- **Real PowerPoint**: Outputs genuine DrawingML shapes, text boxes, and charts — not embedded images. Every element is directly clickable and editable in PowerPoint.
- **Transparent Cost**: The tool is free and open source (MIT license). The only cost is your AI model usage — no additional subscription fees.
- **Data Stays Local**: The entire pipeline runs on your machine. Files are never uploaded to third-party servers, apart from AI model communication.
- **No Platform Lock-in**: Works with Claude Code, Cursor, VS Code Copilot, and more; supports Claude, GPT, Gemini, Kimi, and other mainstream models.

## Key Features & Workflow
1. **Multi-format Input**: Supports PDF, DOCX, XLSX, PPTX, URLs (including WeChat Official Account articles), Markdown, and more.
2. **Seven-step Serial Pipeline**: `Source Processing → Project Init → Template Option → Strategist (Eight Confirmations) → Image Generator → SVG Executor → Post-processing & PPTX Export`.
3. **Natively Editable Output**: Generates real PowerPoint shapes and text via SVG intermediate format, compatible with Office 2016+.
4. **Animations & Transitions**: Exported PPTX supports page transitions and per-element entrance animations (real OOXML, not embedded video).
5. **AI Image Generation** (Optional): Supports OpenAI, Gemini, and other image generation backends for automated slide imagery.
6. **Multiple Canvas Formats**: Supports PPT 16:9, PPT 4:3, Xiaohongshu, WeChat Moments, and 10+ other canvas formats.
7. **Custom Templates**: Provides a standalone template creation workflow for building brand or industry-specific templates.

## Skills Library Overview
- **Source Conversion Scripts**: `pdf_to_md.py`, `doc_to_md.py`, `excel_to_md.py`, `ppt_to_md.py`, `web_to_md.py`, etc., covering mainstream document formats.
- **Project & Quality Control**: `project_manager.py` (project init/validation), `svg_quality_checker.py` (SVG quality check), `finalize_svg.py` (SVG post-processing).
- **Image Processing**: `image_gen.py` (multi-provider AI image generation), `analyze_images.py` (image analysis).
- **Export & Delivery**: `svg_to_pptx.py` (PPTX export), `total_md_split.py` (speaker notes splitting).
- **Standalone Workflows**: `create-template` (build custom templates), `verify-charts` (chart coordinate calibration).

## Installation & Support
PPT Master supports the following AI editors and platforms:
- [Claude Code](../../claudecode/ppt-master/INSTALL-en.md)
- [Cursor](../../cursor/ppt-master/INSTALL-en.md)
- [Codex](../../codex/ppt-master/INSTALL-en.md)
- [OpenCode](../../opencode/ppt-master/INSTALL-en.md)
- [OpenClaw](../../openclaw/ppt-master/INSTALL-en.md)
- [OpenAgent](../../openagent/ppt-master/INSTALL-en.md)
- [Qoder](../../qoder/ppt-master/INSTALL-en.md)

---
For more information, visit: [GitHub - hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
