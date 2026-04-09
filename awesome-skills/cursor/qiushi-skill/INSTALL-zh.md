# 为 Cursor 安装求是 Skill

## 系统要求

- **Windows**: 默认使用 PowerShell hook,无需额外安装 Bash
- **macOS / Linux**: 需要可用的 `bash` 或 `sh`
- **验证脚本**: 仓库内置 `tests/validate.sh`(macOS/Linux)和 `tests/validate.ps1`(Windows),可用于安装后自检

## 安装步骤

### 1. 克隆仓库到本地

```bash
git clone https://github.com/HughYau/qiushi-skill
```

### 2. 将项目目录加入 Cursor 的插件路径

在 Cursor 中配置插件路径,使其能够识别 `.cursor-plugin/plugin.json`。

### 3. 确认插件配置已被识别

确保以下文件已被 Cursor 正确识别:
- `.cursor-plugin/plugin.json`
- `commands/` 目录
- `hooks/hooks.json`

### 4. 使用验证脚本检查

检查 hook 与命令文件是否完整:

#### macOS / Linux:

```bash
cd qiushi-skill
bash tests/validate.sh
```

#### Windows:

```powershell
cd qiushi-skill
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File tests/validate.ps1
```

验证脚本会检查:
- JSON 配置是否有效
- hook 文件与命令文件是否齐全
- `SKILL.md` / agent / command 的 frontmatter 是否完整
- 本地 Markdown 链接和图片路径是否存在

## 更新

```bash
cd qiushi-skill
git pull
```

## 获取帮助

- GitHub: https://github.com/HughYau/qiushi-skill
- 问题反馈: https://github.com/HughYau/qiushi-skill/issues
- 平台详情: https://github.com/HughYau/qiushi-skill/blob/main/docs/platforms.md