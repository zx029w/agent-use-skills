# Install Video Summarizer in Cursor

## Prerequisites

- [Cursor](https://cursor.sh/) installed
- Git installed
- Python 3 installed
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) installed and available in PATH
- [ffmpeg](https://ffmpeg.org/) installed and available in PATH
- [obsidian-cli](https://github.com/Zerone-Agent/agent-use-skills/tree/main/awesome-skills/skills/obsidian-cli) installed (Obsidian CLI skill)
- Obsidian must be running

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create Symbolic Link

Create a symbolic link so Cursor can discover the video-summarizer skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/video-summarizer
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/video-summarizer ~/.cursor/skills/video-summarizer
```

### 3. Install Whisper

Install OpenAI Whisper in a dedicated virtual environment:

```bash
python3 -m venv ~/.whisper-venv
source ~/.whisper-venv/bin/activate
pip install openai-whisper
```

> **Note**: The first run of Whisper will download the turbo model (~1.5GB).

### 4. Verify Installation

Restart Cursor, then try the following commands to verify installation:

- "summarize this video: https://www.youtube.com/watch?v=example"
- "帮我总结这个视频内容"

If installed successfully, Cursor will automatically recognize and invoke the Video Summarizer skill workflow.

## Updating

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.cursor/skills/video-summarizer
```

## Getting Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
