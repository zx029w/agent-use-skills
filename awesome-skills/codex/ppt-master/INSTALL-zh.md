# 在 Codex 中安装 PPT Master

## 准备工作

- 已安装 [Codex CLI](https://github.com/openai/codex)
- 已安装 Git
- 已安装 Python 3.10+

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.codex/ppt-master
```

### 2. 安装依赖

```bash
pip install -r ~/.codex/ppt-master/requirements.txt
```

### 3. 创建软链接

创建软链接使 Codex 能够发现该技能：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/ppt-master
ln -s ~/.codex/ppt-master/skills/ppt-master ~/.codex/skills/ppt-master
```

### 4. 验证安装

重启 Codex，然后尝试提问：
- "do you have ppt-master?"
- "请帮我用 ppt-master 生成一份 PPT"

如果成功，Codex 将自动识别并调用该技能。

## 更新指南

```bash
cd ~/.codex/ppt-master
git pull
```

## 卸载

```bash
rm -rf ~/.codex/skills/ppt-master
rm -rf ~/.codex/ppt-master
```

## 获取帮助

- GitHub: https://github.com/hugohe3/ppt-master
- 提交问题: https://github.com/hugohe3/ppt-master/issues
- 常见问题: https://github.com/hugohe3/ppt-master/blob/main/docs/zh/faq.md
