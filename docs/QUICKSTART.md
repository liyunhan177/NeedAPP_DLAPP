# 快速开始指南

本指南将帮助您在 5 分钟内完成 NeedAPP_DLAPP 的安装和运行。

---

## 🚀 5 分钟快速开始

### 步骤 1: 检查环境 (1 分钟)

确保您的系统满足以下要求：

- ✅ **操作系统**: Windows 10/11
- ✅ **Python 版本**: Python 3.8 或更高
- ✅ **网络连接**: WiFi 或以太网（程序启动时需要）

**检查 Python 版本**:
```bash
python --version
```

如果显示 `Python 3.x.x`，则满足要求。

---

### 步骤 2: 获取项目 (1 分钟)

#### 方法 A: 克隆 Git 仓库（推荐）

```bash
git clone https://github.com/liyunhan177/NeedAPP_DLAPP.git
cd NeedAPP_DLAPP
```

#### 方法 B: 下载 ZIP 文件

1. 访问项目 GitHub 页面
2. 点击 "Code" → "Download ZIP"
3. 解压到本地目录

---

### 步骤 3: 安装依赖 (2 分钟)

#### 创建虚拟环境（推荐）

**Windows PowerShell**:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows CMD**:
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```

#### 安装必要的库

```bash
pip install pywifi ttkbootstrap
```

**国内用户加速**:
```bash
pip install pywifi ttkbootstrap -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

### 步骤 4: 运行程序 (1 分钟)

```bash
python src/main_page.py
```

🎉 **成功！** 您应该能看到程序的主界面了！

---

## 📸 初次使用

### 程序启动流程

1. **网络检测**
   - 程序会自动检测网络连接
   - 如果未连接网络，会显示警告并关闭
   - 如果网络正常，显示主界面

2. **主界面**
   ```
   ┌─────────────────────┐
   │  常用软件下载         │
   ├─────────────────────┤
   │  [音乐软件]          │
   │  [视频软件]          │
   │  [输入法]            │
   │  [浏览器]            │
   │  [媒体播放器]        │
   │  [聊天软件]          │
   │  [退出]              │
   └─────────────────────┘
   ```

3. **选择软件类别**
   - 点击任意按钮打开对应的下载窗口
   - 目前版本仅支持跳转到官网下载
   - 未来版本将支持直接下载

---

## ⚡ 常见问题快速解决

### ❌ 问题 1: "找不到模块 'ttkbootstrap'"

**解决方案**:
```bash
pip install ttkbootstrap
```

### ❌ 问题 2: "找不到模块 'pywifi'"

**解决方案**:
```bash
pip install pywifi
```

### ❌ 问题 3: "图标加载失败"

**说明**: 这是正常现象，程序会继续运行。如需修复，请确保 `res/IMG/logo.ico` 文件存在。

### ❌ 问题 4: "网络检测出错"

**解决方案**:
1. 检查网络连接
2. 如果是 WiFi 问题，确保已连接 WiFi
3. 程序仍会继续启动（错误处理机制）

### ❌ 问题 5: "权限不足" (pywifi 需要)

**解决方案**:
- 以管理员身份运行命令行工具
- 或在 IDE 中以管理员权限运行

---

## 🎯 下一步

完成快速开始后，您可以：

### 深入学习
- 📖 阅读 [完整文档](README.md)
- 💻 学习 [开发者指南](DEVELOPER_GUIDE.md)

### 实际使用
- 🎵 浏览音乐软件列表
- 📺 查看视频软件选项
- 🌐 选择浏览器下载
- 💬 找到聊天软件

### 参与开发
- 🛠️ 配置开发环境
- 📝 学习代码规范
- ➕ 添加新的软件类别

---

## 📋 检查清单

完成快速开始后，您应该能够：

- [x] 成功运行程序
- [x] 看到主界面
- [x] 点击按钮打开子窗口
- [x] 理解基本功能

如果以上都已完成，恭喜您！🎊 您已经掌握了 NeedAPP_DLAPP 的基本使用方法。

---

## 🔗 有用的链接

- **项目主页**: [GitHub](https://github.com/liyunhan177/NeedAPP_DLAPP)
- **详细文档**: [docs/README.md](README.md)
- **问题反馈**: [Issues](https://github.com/liyunhan177/NeedAPP_DLAPP/issues)
- **更新日志**: [CHANGELOG.md](CHANGELOG.md)

---

## 💡 小贴士

1. **性能优化**: 使用虚拟环境可以加快包管理速度
2. **网络检测**: 程序启动时的网络检测是为了更好的用户体验
3. **自定义**: 可以修改 `data/data.json` 来定制软件列表
4. **快捷键**: 
   - `Alt+F4`: 快速关闭程序
   - `Tab`: 在按钮间切换焦点

---

## 🆘 需要帮助？

如果您在使用过程中遇到问题：

1. **查看文档**: [INDEX.md](INDEX.md) 查找相关信息
2. **检查 Issue**: 看是否有人遇到过相同问题
3. **提交 Issue**: 详细描述您的问题
4. **联系作者**: liyunhan11111@163.com

---

**祝您使用愉快！** 🎉

*最后更新：2026 年 3 月 15 日*
