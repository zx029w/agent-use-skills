# 在 OpenCode 中安装 Video Summarizer

## 前置条件

- 已安装 [OpenCode](https://github.com/opencode-ai)
- 已安装 Git
- 已安装 Python 3
- 已安装 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 并可在 PATH 中访问
- 已安装 [ffmpeg](https://ffmpeg.org/) 并可在 PATH 中访问
- 已安装 [obsidian-cli](https://github.com/Zerone-Agent/agent-use-skills/tree/main/awesome-skills/skills/obsidian-cli)（Obsidian CLI 技能）
- Obsidian 必须处于运行状态

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/agent-use-skills
```

### 2. 配置 OpenCode

在 OpenCode 中打开设置，将技能目录添加到工作区：

1. 打开 OpenCode Settings
2. 找到 "Skills" 或 "Custom Skills" 选项
3. 添加技能路径：`~/agent-use-skills/awesome-skills/skills/video-summarizer`

或者，将技能文件复制到 OpenCode 的 skills 目录：

```bash
mkdir -p ~/.config/opencode/skills
cp -r ~/agent-use-skills/awesome-skills/skills/video-summarizer ~/.config/opencode/skills/
```

### 3. 安装 Whisper

在独立的虚拟环境中安装 OpenAI Whisper：

```bash
python3 -m venv ~/.whisper-venv
source ~/.whisper-venv/bin/activate
pip install openai-whisper
```

> **注意**：Whisper 首次运行时会下载 turbo 模型（约 1.5GB）。

### 4. 验证安装

重启 OpenCode，然后尝试输入以下指令来验证是否安装成功：

- "summarize this video: https://www.youtube.com/watch?v=example"
- "帮我总结这个视频内容"

如果安装成功，OpenCode 会自动识别并调用 Video Summarizer 技能的工作流。

## 更新

```bash
cd ~/agent-use-skills
git pull
cp -r ~/agent-use-skills/awesome-skills/skills/video-summarizer ~/.config/opencode/skills/
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
