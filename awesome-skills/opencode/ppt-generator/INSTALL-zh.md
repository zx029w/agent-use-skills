# 为 OpenCode 安装 PPT Generator

## 前置条件

- 已安装 [OpenCode.ai](https://opencode.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. 创建符号链接

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/ppt-generator
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/ppt-generator ~/.config/opencode/skills/ppt-generator
```

### 3. 重启 OpenCode

重启 OpenCode，并通过询问验证是否安装成功："do you have ppt-generator?"

## 更新

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues