# 在 OpenAgent 中安装 Humanizer-zh

## 前置条件

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 humanizer-zh 技能：

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/humanizer-zh
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/humanizer-zh ~/.openagent/skills/humanizer-zh
```

### 3. 验证安装

重启 OpenAgent，尝试询问：
- "帮我去除这段文字的 AI 痕迹"
- "do you have humanizer-zh?"

如果安装成功，OpenAgent 会自动识别并调用 Humanizer-zh 技能工作流。

## 更新

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openagent/skills/humanizer-zh
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues