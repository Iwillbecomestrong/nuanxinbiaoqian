# 暖心便签弹窗阵列 🎉

<div align="center">

![Version](https://img.shields.io/badge/version-1.1.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

一个充满温暖与关怀的 Python 桌面弹窗程序  
用精美的圆角弹窗展示暖心话语  
适合作为生日祝福或日常温馨提醒

[快速开始](#-使用方法) · [功能特性](#-特性) · [下载 Release](https://github.com/Iwillbecomestrong/nuanxinbiaoqian/releases) · [需求文档](需求文档.md)

</div>

---

## ✨ 特性

<table>
<tr>
<td width="50%">

### 🎨 精美设计

- ✅ 大圆角矩形窗口（36px 圆角）
- ✅ 柔和的马卡龙色系背景
- ✅ 无边框透明设计
- ✅ 始终置顶显示

</td>
<td width="50%">

### 📝 内容丰富

- ✅ 150 条精选暖心话语（完全不重复）
- ✅ 75 条中文（含 13 条毛泽东语录）
- ✅ 75 条英文温馨短语
- ✅ 每条消息独特且富有深意

</td>
</tr>
<tr>
<td width="50%">

### 🎯 智能特性

- ✅ 自动识别中英文
- ✅ 中文使用宋体，英文 Times New Roman
- ✅ 字体加粗，清晰易读
- ✅ 文字自动居中对齐

### 🌿 疗愈风格（新增）

- ✅ 内置“疗愈模式”，将部分偏励志的表述柔化为更温柔的关怀
- ✅ 强调“允许、松弛、被看见、被接纳”的情感表达
- ✅ 不改变消息总量与唯一性（仍为 150 条、全部不重复）

</td>
<td width="50%">

### ⚙️ 灵活配置

- ✅ 自定义弹窗数量（默认 150 个）
- ✅ 可调节显示速度
- ✅ 支持测试模式（5 个弹窗）
- ✅ 命令行参数控制

</td>
</tr>
</table>

## 📸 效果预览

```
🎈 程序运行效果：
┌─────────────────────────────────────┐
│  150个精美圆角弹窗随机分布在屏幕上   │
│  每个弹窗显示一条独特的关怀话语      │
│  柔和的色彩，温馨的文字              │
│  最后屏幕中央出现生日祝福            │
│  点击关闭按钮，所有弹窗统一关闭      │
└─────────────────────────────────────┘
```

**运行流程：**

1. 🚀 双击运行程序
2. 🎨 随机在屏幕上弹出 150 个精美的圆角便签窗口
3. 💬 每个窗口显示一条独特的关怀话语
4. 🎂 最后在屏幕中央显示"Happy birthday to you!"
5. ✖️ 点击生日弹窗上的 X 按钮，一键关闭所有窗口

## 🚀 使用方法

### 方式一：直接运行打包好的 exe 文件（推荐）

**📥 下载地址：** [前往 Releases 页面下载](https://github.com/Iwillbecomestrong/nuanxinbiaoqian/releases)

下载后，无需安装任何环境，双击即可运行！

#### 💡 命令行参数

| 命令           | 说明                   | 示例                                |
| -------------- | ---------------------- | ----------------------------------- |
| 无参数         | 默认运行（150 个弹窗） | `暖心便签弹窗阵列.exe`              |
| `--test`       | 快速测试（5 个弹窗）   | `暖心便签弹窗阵列.exe --test`       |
| `--count N`    | 自定义数量             | `暖心便签弹窗阵列.exe --count 100`  |
| `--stagger ms` | 调整速度（毫秒）       | `暖心便签弹窗阵列.exe --stagger 50` |

#### 📝 使用示例

#### 📝 使用示例

```powershell
# 快速测试（推荐首次使用）
.\暖心便签弹窗阵列.exe --test

# 默认完整运行
.\暖心便签弹窗阵列.exe

# 自定义100个弹窗
.\暖心便签弹窗阵列.exe --count 100

# 加快显示速度（50ms间隔）
.\暖心便签弹窗阵列.exe --count 150 --stagger 50
```

### 方式二：从源码运行

**环境要求：**

| 项目     | 版本要求                  |
| -------- | ------------------------- |
| Python   | 3.8 或更高                |
| tkinter  | Python 自带，无需额外安装 |
| 操作系统 | Windows 10/11             |

**运行步骤：**

```bash
# 1. 克隆仓库
git clone https://github.com/Iwillbecomestrong/nuanxinbiaoqian.git
cd nuanxinbiaoqian

# 2. 测试运行
python 暖心便签弹窗阵列.py --test

# 3. 完整运行
python 暖心便签弹窗阵列.py

# 4. 自定义配置
python 暖心便签弹窗阵列.py --count 200 --stagger 80
```

## 🛠️ 自己打包

想要自己打包成 exe 文件？按照以下步骤操作：

### 步骤 1：安装 PyInstaller

```bash
pip install pyinstaller
```

### 步骤 2：执行打包

**方法一：使用 spec 文件（推荐）**

```bash
pyinstaller 暖心便签弹窗阵列.spec
```

**方法二：使用 PowerShell 脚本（Windows）**

```powershell
.\build.ps1
```

**方法三：手动命令**

```bash
pyinstaller --onefile --windowed \
  --add-binary "path/to/tcl86t.dll;." \
  --add-binary "path/to/tk86t.dll;." \
  --add-data "path/to/tcl8.6;tcl/tcl8.6" \
  --add-data "path/to/tk8.6;tcl/tk8.6" \
  --name "暖心便签弹窗阵列" \
  暖心便签弹窗阵列.py
```

打包完成后，可执行文件位于 `dist` 目录中。

📖 **详细打包说明：** 参见 [打包说明.md](打包说明.md)

## 📋 参数说明

| 参数        | 类型 | 说明                        | 默认值 | 示例            |
| ----------- | ---- | --------------------------- | ------ | --------------- |
| `--count`   | 整数 | 弹窗数量                    | 150    | `--count 200`   |
| `--stagger` | 整数 | 每个弹窗间隔（毫秒）        | 80     | `--stagger 100` |
| `--test`    | 标志 | 测试模式（只显示 5 个弹窗） | -      | `--test`        |

**组合使用示例：**

```powershell
# 快速模式：50个弹窗，50ms间隔
.\暖心便签弹窗阵列.exe --count 50 --stagger 50

# 缓慢模式：100个弹窗，150ms间隔
.\暖心便签弹窗阵列.exe --count 100 --stagger 150
```

## 💡 使用场景

| 场景            | 描述                              | 适用对象     |
| --------------- | --------------------------------- | ------------ |
| 🎂 **生日惊喜** | 给朋友/家人一个充满温暖的生日祝福 | 所有年龄段   |
| 💝 **节日祝福** | 情人节、母亲节、父亲节等特殊日子  | 亲人、爱人   |
| 🎓 **毕业寄语** | 给即将毕业的同学送上祝福          | 同学、朋友   |
| 🏆 **鼓励打气** | 在考试或面试前给朋友加油          | 需要鼓励的人 |
| 😊 **日常关怀** | 随时给身边的人送上温暖            | 家人、朋友   |

## 📁 项目结构

```text
项目根目录/
├── 暖心便签弹窗阵列.py      # 主程序源码
├── 暖心便签弹窗阵列.spec    # PyInstaller打包配置
├── build.ps1               # Windows自动打包脚本
├── 打包说明.md             # 详细打包说明
├── 需求文档.md             # 详细需求规格
├── README.md               # 项目说明文档（本文件）
└── .gitignore              # Git忽略文件配置
```

## 🎨 技术实现

### 核心技术栈

| 技术        | 版本   | 用途         |
| ----------- | ------ | ------------ |
| Python      | 3.13.5 | 主要编程语言 |
| tkinter     | 内置   | GUI 界面框架 |
| PyInstaller | 6.16.0 | 打包工具     |
| Git         | -      | 版本控制     |

### 技术亮点

- ✨ **透明窗口技术**：通过透明色（#010101）实现无边框圆角效果
- 🎨 **Canvas 绘图**：使用 Canvas 绘制圆角矩形，实现平滑过渡
- 🎲 **智能随机布局**：弹窗随机分布，避免超出屏幕边界
- 🌈 **马卡龙配色算法**：动态生成柔和色系背景
- 🔤 **Unicode 字符识别**：自动判断中英文并切换字体
- 🔄 **统一关闭机制**：所有窗口通过最后的生日弹窗统一管理

## 📝 消息内容

程序内置 100 条精心挑选的暖心话语：

- **中文消息（50 条）**
  - 13 条毛泽东经典语录
  - 37 条日常关怀体贴话语
- **英文消息（50 条）**
  - 50 条温馨关怀短语

所有消息都经过精心挑选，传递正能量和关怀。

## ⚠️ 注意事项

1. ⚡ **首次使用建议**：运行时会创建大量弹窗，建议先使用 `--test` 参数测试效果
2. 🖱️ **关闭方式**：弹窗不会自动关闭，需点击最后出现的生日弹窗上的 `X` 按钮统一关闭
3. 💻 **性能考虑**：弹窗数量过多可能影响电脑性能，建议根据配置调整数量（推荐 50-200 个）
4. 📦 **文件体积**：单文件 exe 体积约 10MB，包含了完整的 Python 运行时和 tkinter 库
5. 🔒 **安全提示**：程序完全本地运行，不涉及网络通信，不访问敏感文件

## 🤝 参与贡献

欢迎提交 Issue 和 Pull Request！

### 如何贡献

1. 🍴 Fork 本仓库
2. 🌿 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 💾 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 📤 推送到分支 (`git push origin feature/AmazingFeature`)
5. 🎯 提交 Pull Request

### 贡献方向

- 💬 添加更多暖心话语
- 🎨 改进界面设计
- 🐛 修复 Bug
- 📖 完善文档
- 🌍 支持更多语言
- 💡 提出新功能建议

## 📄 许可证

本项目采用 **MIT 许可证**。您可以自由使用、修改和分发本项目。

详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

感谢所有为这个项目提供灵感和支持的人！

特别感谢：

- 💖 所有使用本项目传递温暖的用户
- 🌟 为项目点 Star 的朋友们
- 🐛 提交 Issue 帮助改进的贡献者
- 🔧 提交 PR 的开发者

## 📞 联系方式

- 📧 GitHub Issues: [提交问题](https://github.com/Iwillbecomestrong/nuanxinbiaoqian/issues)
- 💬 GitHub Discussions: [参与讨论](https://github.com/Iwillbecomestrong/nuanxinbiaoqian/discussions)
- ⭐ 如果这个项目对你有帮助，请给个 Star 支持一下！

---

<div align="center">

### 用心制作，传递温暖 ❤️

**如果这个项目对你有帮助，请给个 ⭐ Star 支持一下！**

[![Star History Chart](https://api.star-history.com/svg?repos=Iwillbecomestrong/nuanxinbiaoqian&type=Date)](https://star-history.com/#Iwillbecomestrong/nuanxinbiaoqian&Date)

</div>
