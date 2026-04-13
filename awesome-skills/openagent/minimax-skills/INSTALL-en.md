# Installing MiniMax Skills for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone MiniMax Skills

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.openagent/minimax-skills
```

### 2. Symlink Skills

Create symlinks so OpenAgent discovers the skills:

```bash
mkdir -p ~/.openagent/skills
for skill in android-native-dev ios-application-dev flutter-dev react-native-dev frontend-dev fullstack-dev shader-dev gif-sticker-maker vision-analysis minimax-pdf pptx-generator minimax-xlsx minimax-docx minimax-multimodal-toolkit; do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/minimax-skills/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. Verify Installation

Restart OpenAgent and try asking:
- "Help me create a PowerPoint presentation"
- "do you have minimax skills?"

If successful, OpenAgent will automatically recognize and invoke MiniMax Skills workflow.

## Updating

```bash
cd ~/.openagent/minimax-skills
git pull
```

## Uninstallation

Remove the symlinks to uninstall:

```bash
for skill in android-native-dev ios-application-dev flutter-dev react-native-dev frontend-dev fullstack-dev shader-dev gif-sticker-maker vision-analysis minimax-pdf pptx-generator minimax-xlsx minimax-docx minimax-multimodal-toolkit; do
  rm -rf ~/.openagent/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/MiniMax-AI/skills