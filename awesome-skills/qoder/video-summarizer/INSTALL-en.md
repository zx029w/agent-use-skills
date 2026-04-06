# Install Video Summarizer in Qoder

## Prerequisites

- [Qoder](https://github.com/qoder-ai) installed
- Git installed
- Python 3 installed
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) installed and available in PATH
- [ffmpeg](https://ffmpeg.org/) installed and available in PATH
- [obsidian-cli](https://github.com/Zerone-Agent/agent-use-skills/tree/main/awesome-skills/skills/obsidian-cli) installed (Obsidian CLI skill)
- Obsidian must be running

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/agent-use-skills
```

### 2. Configure Qoder

In Qoder, add the skill directory to your workspace through settings:

1. Open Qoder Settings
2. Find "Skills" or "Custom Skills" option
3. Add skill path: `~/agent-use-skills/awesome-skills/skills/video-summarizer`

Alternatively, copy the skill files to Qoder's skills directory:

```bash
mkdir -p ~/.qoder/skills
cp -r ~/agent-use-skills/awesome-skills/skills/video-summarizer ~/.qoder/skills/
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

Restart Qoder, then try the following commands to verify installation:

- "summarize this video: https://www.youtube.com/watch?v=example"
- "帮我总结这个视频内容"

If installed successfully, Qoder will automatically recognize and invoke the Video Summarizer skill workflow.

## Update

```bash
cd ~/agent-use-skills
git pull
cp -r ~/agent-use-skills/awesome-skills/skills/video-summarizer ~/.qoder/skills/
```

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.qoder/skills/video-summarizer
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
