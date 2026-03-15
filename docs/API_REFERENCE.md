# API 参考文档

## 概述

本文档提供了 NeedAPP_DLAPP 项目的完整 API 参考，包括所有公共类、方法和函数的详细说明。

---

## 模块索引

### 核心模块
- [`src/main_page.py`](#srcmain_pagepy) - 主程序入口
- [`lib/page/`](#libpage) - 页面模块集合
- [`lib/package/wifi_detection.py`](#libpackagewifi_detectionpy) - 网络检测工具

---

## src/main_page.py

### 类：Main

主应用程序窗口类

#### 继承关系
```python
Main(tk.Tk)
```

#### 构造函数

**`__init__()`**

初始化主窗口，包括：
- 设置窗口标题和尺寸
- 配置图标
- 启动网络检测
- 创建所有功能按钮

**参数**: 无

**返回**: 无

**示例**:
```python
app = Main()
app.mainloop()
```

#### 方法

**`check_network_on_startup()`**

启动时检测网络状态（WiFi 和以太网）

**功能描述**:
- 调用 `wifi_detection.get_network_info()` 获取网络状态
- 如果未连接任何网络，显示警告对话框并关闭应用
- 如果已连接，打印网络状态信息到控制台
- 异常情况下记录错误并继续启动

**参数**: 无

**返回**: 无

**异常处理**:
- 捕获所有异常，确保应用能够正常启动

**网络状态字典结构**:
```python
{
    "wifi": {
        "connected": bool,      # WiFi 是否连接
        "message": str,         # WiFi 状态消息
        "info": dict or None    # WiFi 详细信息 (SSID, signal)
    },
    "ethernet": {
        "connected": bool,      # 以太网是否连接
        "message": str,         # 以太网状态消息
        "info": dict or None    # 以太网详细信息 (IP)
    },
    "any_connected": bool       # 任一网络已连接则为 True
}
```

---

## lib/page/ 模块

所有页面模块都遵循统一的设计模式，继承自 `tk.Toplevel`。

### 通用类结构

每个页面模块都包含一个以模块名命名的类：

- `music.py` → `Music` 类
- `video.py` → `Video` 类
- `input.py` → `Input` 类
- `browser.py` → `Browser` 类
- `media.py` → `Media` 类
- `chat.py` → `Chat` 类

#### 通用属性

**窗口配置**:
- 标题：根据功能自动设置（如"音乐软件下载"）
- 尺寸：300x300 像素
- 可调整大小：否（固定窗口）
- 图标：`res/IMG/logo.ico`

#### 构造函数

**`__init__()`**

初始化页面窗口

**参数**: 无

**返回**: 无

**示例**:
```python
# 音乐页面
music_win = Music()
music_win.mainloop()

# 视频页面
video_win = Video()
video_win.mainloop()
```

### 各模块说明

#### 1. music.py - 音乐软件页面

**类**: `Music(tk.Toplevel)`

**支持的软件**:
- QQ 音乐
- 网易云音乐
- 酷狗音乐
- 酷我音乐
- 咪咕音乐
- 千千音乐

#### 2. video.py - 视频播放软件页面

**类**: `Video(tk.Toplevel)`

**支持的软件**:
- PotPlayer
- VLC
- KMPlayer
- 暴风影音

#### 3. input.py - 输入法页面

**类**: `Input(tk.Toplevel)`

**支持的软件**:
- 搜狗输入法
- 百度输入法
- QQ 输入法
- 讯飞输入法
- 小狼毫 (Rime)
- 微软拼音

#### 4. browser.py - 浏览器页面

**类**: `Browser(tk.Toplevel)`

**支持的软件**:
- Edge
- Chrome
- 360 安全浏览器
- 360 极速浏览器
- QQ 浏览器
- Firefox

#### 5. media.py - 媒体播放器页面

**类**: `Media(tk.Toplevel)`

**支持的软件**:
- 哔哩哔哩
- 抖音
- 腾讯视频
- 爱奇艺
- 优酷
- 咪咕视频

#### 6. chat.py - 聊天软件页面

**类**: `Chat(tk.Toplevel)`

**支持的软件**:
- 微信
- Tim
- QQ
- 钉钉
- 飞书

---

## lib/package/wifi_detection.py

网络检测工具模块，提供 WiFi 和以太网状态检测功能。

### 函数列表

#### `check_wifi_status()`

检测 WiFi 连接状态

**返回值**:
```python
tuple: (是否连接，状态消息，连接信息字典)
    - 是否连接 (bool): True 表示已连接，False 表示未连接
    - 状态消息 (str): 描述当前 WiFi 状态
    - 连接信息字典 (dict or None): 包含 SSID 和信号强度
```

**返回示例**:
```python
# 已连接
(True, "WiFi 已连接：MyWiFi", {"ssid": "MyWiFi", "signal": -65})

# 未连接
(False, "WiFi 未连接", None)

# 出错
(False, "WiFi 检测出错：No interface found", None)
```

**依赖**:
- pywifi.PyWiFi
- pywifi.const.IFACE_DISCONNECTED

**异常处理**:
- 捕获所有异常并返回友好的错误消息

---

#### `check_ethernet_status()`

检测以太网连接状态

**检测方法**:
通过 socket 尝试连接到 Google DNS 服务器 (8.8.8.8:53)

**返回值**:
```python
tuple: (是否连接，状态消息，连接信息字典)
    - 是否连接 (bool): True 表示已连接，False 表示未连接
    - 状态消息 (str): 描述当前以太网状态
    - 连接信息字典 (dict or None): 包含本地 IP 地址
```

**返回示例**:
```python
# 已连接
(True, "以太网已连接 (IP: 192.168.1.100)", {"ip": "192.168.1.100"})

# 未连接
(False, "以太网未连接", None)

# 出错
(False, "以太网检测出错：Connection timed out", None)
```

**技术参数**:
- 目标主机：8.8.8.8 (Google DNS)
- 端口：53 (DNS)
- 超时时间：2 秒

---

#### `get_network_info()`

获取网络连接信息（WiFi 和以太网）

**功能**:
综合检测两种网络连接方式

**返回值**:
```python
dict: 包含网络连接信息的字典
{
    "wifi": {
        "connected": bool,      # WiFi 是否连接
        "message": str,         # WiFi 状态消息
        "info": dict or None    # WiFi 详细信息
    },
    "ethernet": {
        "connected": bool,      # 以太网是否连接
        "message": str,         # 以太网状态消息
        "info": dict or None    # 以太网详细信息
    },
    "any_connected": bool       # 任一网络已连接
}
```

**返回示例**:
```python
{
    "wifi": {
        "connected": True,
        "message": "WiFi 已连接：MyWiFi",
        "info": {"ssid": "MyWiFi", "signal": -65}
    },
    "ethernet": {
        "connected": False,
        "message": "以太网未连接",
        "info": None
    },
    "any_connected": True
}
```

**使用示例**:
```python
from lib.package import wifi_detection

result = wifi_detection.get_network_info()

if result["any_connected"]:
    print("网络已连接")
    if result["wifi"]["connected"]:
        print(f"WiFi: {result['wifi']['info']['ssid']}")
else:
    print("未连接任何网络")
```

---

## 数据文件格式

### data/data.json

软件信息数据文件

#### 数据结构

```json
{
  "<category>": {
    "<software_id>": {
      "num": <int>,        // 软件序号
      "title": <str>,      // 软件名称
      "url": <str>         // 官方下载链接
    }
  }
}
```

#### 支持的类别 (category)

| 类别键名 | 中文名称 | 包含软件数 |
|---------|---------|-----------|
| chat | 聊天软件 | 5 |
| browser | 浏览器 | 6 |
| input | 输入法 | 6 |
| music | 音乐软件 | 6 |
| video | 视频播放 | 4 |
| media | 媒体平台 | 6 |

#### 数据访问示例

```python
import json

with open('data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取所有音乐软件
music_apps = data['music']

# 获取 QQ 音乐信息
qq_music = music_apps['qq_music']
print(f"名称：{qq_music['title']}")
print(f"链接：{qq_music['url']}")
```

---

## 常量定义

### ttkbootstrap 样式常量

```python
from ttkbootstrap.constants import *

# 按钮样式
BOOTSTYLE_OUTLINE = "outline"           # 轮廓样式
BOOTSTYLE_DANGER_OUTLINE = "danger-outline"  # 危险样式（红色轮廓）
```

### pywifi 常量

```python
from pywifi import const

IFACE_DISCONNECTED = 0  # WiFi 未连接状态
```

---

## 错误码参考

### 网络检测错误

| 错误类型 | 错误消息 | 可能原因 |
|---------|---------|---------|
| WiFi 接口不存在 | "No interface found" | 没有无线网卡或驱动未安装 |
| WiFi 扫描失败 | 空扫描结果 | WiFi 适配器被禁用 |
| 以太网连接超时 | "Connection timed out" | 网络防火墙阻止 |
| Socket 错误 | 各种 socket 错误 | 网络配置问题 |

### UI 相关错误

| 错误类型 | 错误消息 | 可能原因 |
|---------|---------|---------|
| 图标加载失败 | 无错误提示 | logo.ico 文件不存在 |
| 窗口创建失败 | Tkinter 异常 | 系统资源不足 |

---

## 最佳实践

### 1. 网络检测使用

```python
# ✅ 推荐：在应用启动时检测
def check_network_on_startup(self):
    try:
        network_info = wifi_detection.get_network_info()
        if not network_info["any_connected"]:
            messagebox.showwarning("网络未连接", "请先连接网络")
            self.destroy()
    except Exception as e:
        print(f"网络检测出错：{str(e)}")
        # 即使出错也允许启动

# ❌ 不推荐：频繁检测网络
while True:
    network_info = wifi_detection.get_network_info()
    time.sleep(1)  # 避免频繁检测
```

### 2. 页面打开方式

```python
# ✅ 推荐：使用 Toplevel 创建独立窗口
def open_music_page():
    music_win = Music()
    music_win.mainloop()

# ❌ 不推荐：重复创建窗口
def open_music_page():
    for i in range(5):
        music_win = Music()  # 创建多个实例
```

### 3. 数据读取

```python
# ✅ 推荐：使用上下文管理器
import json

def load_software_data():
    with open('data/data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# ❌ 不推荐：忘记关闭文件
def load_software_data():
    f = open('data/data.json', 'r', encoding='utf-8')
    data = json.load(f)
    # 忘记关闭文件
```

---

## 版本历史

### v0.2.2 (当前版本)
- ✅ 修复网络检测逻辑
- ✅ 修改文档内容
- ✅ 添加日志输出

### v0.2.1
- ✅ 新增网络连接检测功能
- ✅ 添加更多文档
- ✅ 添加对应注释

### v0.2.0
- ✅ 实现基础 UI 框架
- ✅ 建立数据 JSON 文件
- ✅ 完成 6 个软件分类页面框架

### v0.1.0 (初始版本)
- ✅ 项目初始化
- ✅ 搭建基础架构

---

*最后更新时间：2026 年 3 月 15 日*  
*文档版本：v0.2.2*
