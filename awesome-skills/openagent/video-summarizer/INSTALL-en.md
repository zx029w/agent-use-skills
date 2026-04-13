# Installing Video Summarizer for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed
- yt-dlp, ffmpeg, and OpenAI Whisper installed

## Installation Steps

### 1. Install Tool Dependencies

```bash
pip install yt-dlp openai-whisper
brew install ffmpeg  # macOS
# or apt install ffmpeg  # Linux
```

### 2. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 3. Symlink Skills

Create a symlink so OpenAgent discovers the skill:

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/video-summarizer
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/video-summarizer ~/.openagent/skills/video-summarizer
```

### 4. Verify Installation

Restart OpenAgent and try asking:
- "Help me summarize this video https://www.youtube.com/watch?v=xxx"
- "do you have video-summarizer?"

If successful, OpenAgent will automatically recognize and invoke the Video Summarizer skill workflow.

## Updating

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.openagent/skills/video-summarizer
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues