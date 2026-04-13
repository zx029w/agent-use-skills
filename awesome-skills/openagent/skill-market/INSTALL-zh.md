# 在 OpenAgent 中安装 Skill Market

## 前置条件

- 已安装 OpenAgent
- 已安装 Git
- 确保已安装 Python（推荐使用 `uv`，但非必须）

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openagent/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 skill-market 技能：

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/skill-market
ln -s ~/.openagent/agent-use-skills/awesome-skills/skills/skill-market ~/.openagent/skills/skill-market
```

### 3. 验证安装

执行以下命令或重启 OpenAgent 后询问以验证是否安装成功：

```bash
~/.openagent/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

或者在 OpenAgent 中尝试询问：
- "列出 skill market 上的所有可用技能"
- "do you have skill-market?"

如果安装成功，OpenAgent 会自动识别并调用 Skill Market 技能工作流。

## 更新

```bash
cd ~/.openagent/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openagent/skills/skill-market
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues