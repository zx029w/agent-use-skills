# 为 Claude Code 安装求是 Skill

## 系统要求

- **Windows**: 默认使用 PowerShell hook,无需额外安装 Bash
- **macOS / Linux**: 需要可用的 `bash` 或 `sh`
- **验证脚本**: 仓库内置 `tests/validate.sh`(macOS/Linux)和 `tests/validate.ps1`(Windows),可用于安装后自检

## 安装步骤

### 方法 A: 通过 Claude Plugin Hub 安装(推荐)

在终端中一键安装:

```bash
npx claudepluginhub hughyau/qiushi-skill
```

或者在 Claude Code 中通过 Marketplace 手动安装:

1. 添加 Marketplace(只需执行一次):
   ```
   /plugin marketplace add https://www.claudepluginhub.com/api/plugins/hughyau-qiushi-skill/marketplace.json
   ```

2. 安装插件:
   ```
   /plugin install hughyau-qiushi-skill@cpd-hughyau-qiushi-skill
   ```

### 方法 B: 源码克隆安装

```bash
git clone https://github.com/HughYau/qiushi-skill
cd qiushi-skill
claude --plugin-dir .
```

`--plugin-dir` 会在当前会话加载插件。如需每次会话都自动加载,可以设置 shell alias:

```bash
# 加入 ~/.bashrc 或 ~/.zshrc
alias claude='claude --plugin-dir /path/to/qiushi-skill'
```

## 验证安装

### macOS / Linux 验证:

```bash
bash tests/validate.sh
```

- hook 入口使用 `hooks/session-start`
- 请确认系统上有 `bash` 或 `sh`

### Windows 验证:

```powershell
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File tests/validate.ps1
```

- 从 `1.2.0` 起,SessionStart hook 优先走原生 PowerShell,不再依赖 Git Bash / WSL
- 如果你的环境禁用了 PowerShell 脚本执行,请使用 `-ExecutionPolicy Bypass` 运行验证脚本确认安装

验证脚本会检查:
- JSON 配置是否有效
- hook 文件与命令文件是否齐全
- `SKILL.md` / agent / command 的 frontmatter 是否完整
- 本地 Markdown 链接和图片路径是否存在
- Windows hook 的原生 PowerShell 输出是否可解析

## 更新

如果使用方法 A(Plugin Hub):

```bash
npx claudepluginhub hughyau/qiushi-skill --update
```

如果使用方法 B(源码克隆):

```bash
cd qiushi-skill
git pull
```

## 获取帮助

- GitHub: https://github.com/HughYau/qiushi-skill
- 问题反馈: https://github.com/HughYau/qiushi-skill/issues
- 平台详情: https://github.com/HughYau/qiushi-skill/blob/main/docs/platforms.md