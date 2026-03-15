# NeedAPP_DLAPP 项目文档

## 项目概述

**NeedAPP_DLAPP**（常用软件及工具下载器）是一个基于 Python 和 ttkbootstrap 开发的图形界面应用程序，旨在为用户提供便捷的常用软件下载服务。用户可以通过直观的图形界面选择需要下载的软件类型，并直接访问官方网站进行下载。

### 基本信息

- **项目名称**: NeedAPP_DLAPP
- **版本**: 0.2.1
- **作者**: liyunhan177
- **开发语言**: Python
- **适用系统**: Windows
- **主要框架**: 
  - tkinter (GUI 基础框架)
  - ttkbootstrap (现代化 UI 组件库)
  - pywifi (网络检测功能)

---

## 项目结构详解

```
NeedAPP_DLAPP/
├── src/                      # 源代码目录
│   ├── __init__.py          # src 包初始化文件
│   └── main_page.py         # 主程序入口和主界面
│
├── lib/                      # 功能库目录
│   ├── __init__.py          # lib 包初始化文件
│   ├── page/                # 页面模块目录
│   │   ├── __init__.py      # page 包初始化文件（未显示）
│   │   ├── music.py         # 音乐软件下载页面
│   │   ├── video.py         # 视频软件下载页面
│   │   ├── input.py         # 输入法下载页面
│   │   ├── browser.py       # 浏览器下载页面
│   │   ├── media.py         # 媒体播放器下载页面
│   │   ├── chat.py          # 聊天软件下载页面
│   │   └── nowifi.py        # 无网络模式页面
│   └── package/             # 工具包目录
│       └── wifi_detection.py  # WiFi 和网络检测工具
│
├── data/                     # 数据文件目录
│   └── data.json            # 软件下载链接配置数据
│
├── res/                      # 资源文件目录
│   ├── IMG/                 # 图片资源
│   │   ├── logo.ico         # 应用程序图标
│   │   ├── DL.png           # 下载相关图片
│   │   ├── test_img.jpg     # 测试图片
│   │   └── UI/              # UI 相关图片
│   │       └── main_page.png  # 主界面截图
│   └── sound/               # 音频资源
│       └── test_sound.mp3   # 测试音频
│
├── test/                     # 测试文件目录
│   └── test_func/           # 功能测试脚本
│
├── docs/                     # 文档目录
│   └── README.md            # 本文档
│
├── .venv/                    # Python 虚拟环境（自动生成）
├── .idea/                    # PyCharm IDE 配置（自动生成）
├── .vscode/                  # VS Code 配置
├── pyproject.toml           # 项目配置文件
└── README.md                # 项目说明文件
```

---

## 核心模块说明

### 1. 主程序模块 (`src/main_page.py`)

**功能描述**:
- 应用程序的主入口点
- 创建主窗口并初始化界面布局
- 启动时自动检测网络连接状态
- 提供各个软件类别的导航按钮

**主要类**:
- `Main(tk.Tk)`: 主窗口类
  - `__init__()`: 初始化窗口、设置图标、创建界面组件
  - `check_network_on_startup()`: 启动时检测网络状态

**工作流程**:
1. 初始化 tkinter 主窗口
2. 设置窗口标题、大小和图标
3. 检测网络连接（WiFi 和以太网）
4. 如果未连接网络，显示警告并关闭应用
5. 如果网络正常，显示主界面按钮
6. 等待用户交互

**依赖模块**:
- `lib.wifi_detection`: 网络检测功能
- `lib.page.*`: 各个软件下载页面

---

### 2. 页面模块 (`lib/page/`)

所有页面模块都继承自 `tk.Toplevel`，提供独立的子窗口界面。

#### 2.1 music.py - 音乐软件页面
- **类**: `Music(tk.Toplevel)`
- **功能**: 提供音乐类软件的下载界面
- **支持的软件**: QQ 音乐、网易云音乐、酷狗音乐等

#### 2.2 video.py - 视频软件页面
- **类**: `Video(tk.Toplevel)`
- **功能**: 提供视频类软件的下载界面
- **支持的软件**: PotPlayer、VLC、KMPlayer 等

#### 2.3 input.py - 输入法页面
- **类**: `Input(tk.Toplevel)`
- **功能**: 提供输入法软件的下载界面
- **支持的软件**: 搜狗输入法、百度输入法、QQ 输入法等

#### 2.4 browser.py - 浏览器页面
- **类**: `Browser(tk.Toplevel)`
- **功能**: 提供浏览器软件的下载界面
- **支持的软件**: Edge、Chrome、Firefox、360 浏览器等

#### 2.5 media.py - 媒体播放器页面
- **类**: `Media(tk.Toplevel)`
- **功能**: 提供媒体播放器软件的下载界面
- **支持的软件**: 各类本地和在线媒体播放工具

#### 2.6 chat.py - 聊天软件页面
- **类**: `Chat(tk.Toplevel)`
- **功能**: 提供聊天社交软件的下载界面
- **支持的软件**: 微信、QQ、钉钉、飞书等

#### 2.7 nowifi.py - 无网络模式页面
- **类**: `Nowifi(tk.Toplevel)`
- **功能**: 提供无网络连接时的本地功能界面

**共同特性**:
- 统一的窗口尺寸（300x300）
- 禁止调整窗口大小
- 自动加载应用程序图标
- 图标加载失败时的容错处理

---

### 3. 网络检测模块 (`lib/package/wifi_detection.py`)

**功能描述**:
提供全面的网络连接状态检测功能，支持 WiFi 和以太网两种连接方式。

**核心函数**:

#### 3.1 `check_wifi_status()`
```python
def check_wifi_status():
    """检测 WiFi 连接状态"""
```
- **返回值**: `(connected: bool, message: str, info: dict)`
- **功能**: 
  - 使用 pywifi 库检测 WiFi 接口状态
  - 获取已连接 WiFi 的 SSID 和信号强度
  - 返回详细的连接状态信息

#### 3.2 `check_ethernet_status()`
```python
def check_ethernet_status():
    """检测以太网连接状态"""
```
- **返回值**: `(connected: bool, message: str, info: dict)`
- **功能**:
  - 通过 socket 连接测试（8.8.8.8:53）判断网络连通性
  - 获取本地 IP 地址
  - 超时时间设置为 2 秒

#### 3.3 `get_network_info()`
```python
def get_network_info():
    """获取网络连接信息（WiFi 和以太网）"""
```
- **返回值**: `dict` 包含完整的网络连接信息
- **数据结构**:
```json
{
    "wifi": {
        "connected": true/false,
        "message": "状态描述",
        "info": {"ssid": "WiFi 名称", "signal": 信号强度}
    },
    "ethernet": {
        "connected": true/false,
        "message": "状态描述",
        "info": {"ip": "本地 IP 地址"}
    },
    "any_connected": true/false  // 是否有任何一种网络已连接
}
```

---

### 4. 数据配置模块 (`data/data.json`)

**功能描述**:
存储所有软件的下载链接和元数据信息。

**数据结构**:
```json
{
    "category": {           // 软件类别（chat, browser, input 等）
        "software_id": {    // 软件唯一标识
            "num": 序号，
            "title": "软件名称",
            "url": "官方下载链接"
        }
    }
}
```

**支持的软件类别**:
- `chat`: 聊天社交软件（微信、QQ、钉钉等）
- `browser`: 浏览器（Edge、Chrome、Firefox 等）
- `input`: 输入法（搜狗、百度、QQ 等）
- `music`: 音乐软件（QQ 音乐、网易云音乐等）
- `video`: 视频播放器（PotPlayer、VLC 等）
- `media`: 媒体平台（哔哩哔哩、抖音、腾讯视频等）

---

## 技术架构

### 依赖库说明

#### 1. **ttkbootstrap**
- **作用**: 现代化的 tkinter 主题组件库
- **特点**: 
  - 提供美观的 Bootstrap 风格 UI 组件
  - 支持多种内置主题
  - 简化 GUI 开发流程

#### 2. **pywifi**
- **作用**: WiFi 网络检测和管理
- **功能**:
  - 扫描 WiFi 网络
  - 获取 WiFi 连接状态
  - 读取 WiFi 信息（SSID、信号强度等）

#### 3. **tkinter**
- **作用**: Python 标准 GUI 库
- **地位**: 整个应用的基础框架

### 模块导入关系

```
src/main_page.py
    ↓
lib/__init__.py
    ↓
lib/page/*.py      (各个页面模块)
lib/package/wifi_detection.py  (网络检测工具)
```

---

## 安装与运行

### 环境要求

- **操作系统**: Windows 10/11
- **Python 版本**: Python 3.8+
- **必需依赖**:
  ```bash
  pip install pywifi ttkbootstrap
  ```

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/liyunhan177/NeedAPP_DLAPP.git
cd NeedAPP_DLAPP
```

2. **创建虚拟环境**（推荐）
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. **安装依赖**
```bash
pip install pywifi ttkbootstrap
```

4. **运行程序**
```bash
python src/main_page.py
```

---

## 使用说明

### 基本操作流程

1. **启动应用**
   - 运行 `python src/main_page.py`
   - 程序自动检测网络连接

2. **网络检测**
   - 如果未连接网络：显示警告并自动关闭
   - 如果网络正常：显示主界面

3. **选择软件类型**
   - 点击对应类别的按钮（音乐、视频、浏览器等）
   - 打开相应的软件下载窗口

4. **下载软件**
   - 在子窗口中选择具体软件
   - 访问官方网站下载安装包

### 界面元素

**主界面按钮**:
- 音乐软件
- 视频软件
- 输入法
- 浏览器
- 媒体播放器
- 聊天软件
- 退出

---

## 开发指南

### 添加新的软件类别

1. **在 `lib/page/` 目录创建新页面文件**
```python
# new_category.py
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

class NewCategory(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("新类别下载")
        self.geometry("300x300")
        self.resizable(False, False)
        # 添加你的界面逻辑
```

2. **在 `lib/__init__.py` 中导出新模块**
```python
from .page import new_category
__all__.append("new_category")
new_category_page = new_category.NewCategory
```

3. **在 `main_page.py` 中添加按钮**
```python
def new_open():
    new_win = lib.new_category_page()
    new_win.mainloop()

new_btn = ttk.Button(self, text="新类别", command=new_open)
```

4. **在 `data/data.json` 中添加数据**
```json
"new_category": {
    "software1": {
        "num": 1,
        "title": "软件名",
        "url": "下载链接"
    }
}
```

---

## 常见问题

### Q1: 为什么启动时提示网络未连接？
**A**: 程序会在启动时检测 WiFi 和以太网连接。请确保至少有一种网络连接正常。

### Q2: 图标无法显示怎么办？
**A**: 检查 `res/IMG/logo.ico` 文件是否存在。如果不存在，程序会自动跳过图标加载。

### Q3: 如何修改软件列表？
**A**: 编辑 `data/data.json` 文件，按照现有格式添加或修改软件信息。

### Q4: 支持 macOS 或 Linux 吗？
**A**: 目前主要针对 Windows 系统开发。其他系统可能需要调整网络检测部分的代码。

---

## 未来规划

- [ ] 实现软件直接下载功能（当前仅支持跳转官网）
- [ ] 本地安装包管理
- [ ] 数据库存储替代 JSON 文件
- [ ] 软件版本检测和更新提醒
- [ ] 下载速度优化（多线程/断点续传）
- [ ] 软件分类细化
- [ ] 用户自定义软件源
- [ ] 打包为 exe 可执行文件
- [ ] 支持更多操作系统

---

## 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

### 贡献方式
1. 报告 Bug
2. 提出新功能建议
3. 改进代码质量
4. 完善文档
5. 美化 UI 界面

---

## 特别说明

> 作者本人为学生，该项目仅为个人兴趣爱好作品，不保证长期维护。代码质量和架构设计可能存在不足，望理解。

---

## 联系方式

- **作者**: liyunhan177
- **邮箱**: liyunhan11111@163.com
- **GitHub**: https://github.com/liyunhan177/NeedAPP_DLAPP

---

## 许可证

本项目采用个人许可证，版权归 liyunhan177 所有。

---

## 致谢

感谢以下开源项目：
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)
- [pywifi](https://github.com/clipcard/pywifi)
- [tkinter](https://docs.python.org/zh-cn/3/library/tkinter.html)

---

*最后更新时间：2026 年 3 月 15 日*
