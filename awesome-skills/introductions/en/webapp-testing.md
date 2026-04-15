# Webapp Testing

**Webapp Testing** is a toolkit for interacting with and testing local web applications using Playwright.

## Tags

💻 Dev & Testing | 🔍 Pending Verification

## Core Philosophy
- Automated server lifecycle management (supports both single and multi-server architectures).
- Reliable local web testing using native Python Playwright scripts.
- Promotes a reconnaissance-then-action pattern for dynamic web applications.
- Provides out-of-the-box helper scripts to accomplish workflows, preventing context window bloat.

## Key Features & Workflow
1. **Static HTML Testing**: Directly read local HTML files to identify selectors and write testing scripts.
2. **Dynamic WebApp Testing**: Automatically manage target servers (e.g., `npm run dev`) via the `with_server.py` helper script.
3. **Multiple Servers**: Start both frontend and backend servers together for end-to-end testing.
4. **Reconnaissance-Then-Action Pattern**:
   - Navigate and wait for network activity to settle (`networkidle`).
   - Take screenshots or inspect the DOM to discover elements.
   - Execute actions using the discovered selectors.

## Skills Library Overview
- **Server Lifecycle Scripts**: Uses `with_server.py` to efficiently manage the web server process.
- **Reference Automation Patterns**: Includes examples for common automation flows like UI element discovery (`element_discovery.py`), static HTML testing (`static_html_automation.py`), and catching console output (`console_logging.py`).

## Installation & Support
Webapp Testing supports the following AI editors and platforms:
- [Claude Code](../../claudecode/webapp-testing/INSTALL-en.md)
- [Cursor](../../cursor/webapp-testing/INSTALL-en.md)
- [Codex](../../codex/webapp-testing/INSTALL-en.md)
- [OpenCode](../../opencode/webapp-testing/INSTALL-en.md)
- [OpenClaw](../../openclaw/webapp-testing/INSTALL-en.md)
- [Qoder](../../qoder/webapp-testing/INSTALL-en.md)

---
For more information, visit: [GitHub - anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/webapp-testing)
