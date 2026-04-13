# 在 OpenAgent 中安装 MiniMax Skills

## 前置条件

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 克隆 MiniMax Skills 仓库

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.openagent/minimax-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 MiniMax 技能：

```bash
mkdir -p ~/.openagent/skills
for skill in android-native-dev ios-application-dev flutter-dev react-native-dev frontend-dev fullstack-dev shader-dev gif-sticker-maker vision-analysis minimax-pdf pptx-generator minimax-xlsx minimax-docx minimax-multimodal-toolkit; do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/minimax-skills/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. 验证安装

重启 OpenAgent，尝试询问：
- "帮我创建一个 PPT 演示文稿"
- "do you have minimax skills?"

如果安装成功，OpenAgent 会自动识别并调用 MiniMax Skills 工作流。

## 更新

```bash
cd ~/.openagent/minimax-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
for skill in android-native-dev ios-application-dev flutter-dev react-native-dev frontend-dev fullstack-dev shader-dev gif-sticker-maker vision-analysis minimax-pdf pptx-generator minimax-xlsx minimax-docx minimax-multimodal-toolkit; do
  rm -rf ~/.openagent/skills/$skill
done
```

## 获取帮助

- GitHub：https://github.com/MiniMax-AI/skills