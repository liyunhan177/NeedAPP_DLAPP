# 开发者指南

本文档为 NeedAPP_DLAPP 项目的开发者提供详细的开发指导和最佳实践。

---

## 目录

1. [开发环境配置](#开发环境配置)
2. [代码规范](#代码规范)
3. [架构设计](#架构设计)
4. [扩展开发](#扩展开发)
5. [调试技巧](#调试技巧)
6. [测试指南](#测试指南)
7. [打包发布](#打包发布)

---

## 开发环境配置

### 1. Python 环境

**要求**:
- Python 3.8 或更高版本
- 推荐使用虚拟环境

**配置步骤**:

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境（Windows）
.venv\Scripts\activate

# 激活虚拟环境（Linux/Mac）
source .venv/bin/activate
```

### 2. 安装依赖

```bash
# 基础依赖
pip install pywifi ttkbootstrap

# 开发工具（可选）
pip install pytest black pylint autopep8
```

### 3. IDE 配置

#### VS Code

推荐安装扩展：
- Python
- Pylance
- Python Indent
- autoDocstring

配置文件 (`.vscode/settings.json`):
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.linting.enabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

#### PyCharm

配置解释器：
1. File → Settings → Project → Python Interpreter
2. 选择 `.venv/Scripts/python.exe`

---

## 代码规范

### 命名规范

#### 文件命名
- ✅ 正确：`main_page.py`, `wifi_detection.py`
- ❌ 错误：`MainPage.py`, `wifidetection.py`

**规则**:
- 使用小写字母和下划线
- 见名知意，表达清晰

#### 类命名
```python
# 使用大驼峰命名法（PascalCase）
class Main(tk.Tk):
    pass

class MusicPage(tk.Toplevel):
    pass
```

#### 函数和变量命名
```python
# 使用小写字母和下划线（snake_case）
def check_network_on_startup(self):
    network_info = get_network_info()
    
music_app_button = ttk.Button(...)
```

#### 常量命名
```python
# 全部大写，单词间用下划线分隔
DEFAULT_WINDOW_SIZE = "300x300"
MAX_RETRY_COUNT = 3
```

### 注释规范

#### 模块文档字符串
```python
"""模块简介

详细描述模块的功能、用途和依赖关系
"""
import ...
```

#### 类文档字符串
```python
class ClassName:
    """类的简短描述
    
    详细描述类的功能、属性和方法
    """
```

#### 函数文档字符串
```python
def function_name(param1, param2):
    """函数的功能描述
    
    Args:
        param1: 参数 1 的描述
        param2: 参数 2 的描述
    
    Returns:
        返回值的描述
    
    Raises:
        ExceptionType: 异常情况的描述
    """
```

#### 行内注释
```python
# 单行注释使用 # 加空格

# 多行注释
# 第一行
# 第二行

x = 5  # 行尾注释保持至少两个空格
```

### 代码格式

#### 导入顺序
```python
# 1. 标准库
import sys
import os
from tkinter import *

# 2. 第三方库
import ttkbootstrap as ttk
import pywifi

# 3. 本地应用模块
import lib
from src import main_page
```

#### 空行规范
```python
# 类和函数之间空两行
class Class1:
    pass


class Class2:
    pass


# 函数内部逻辑空一行
def my_function():
    line1 = 1
    line2 = 2
    
    return result
```

#### 行长度
- 最大行长：79 字符（推荐）
- 最大容忍行长：99 字符

---

## 架构设计

### 项目架构原则

#### 1. 单一职责原则
每个模块只负责一个明确的功能领域：
- `main_page.py`: 主界面和程序入口
- `lib/page/*.py`: 各个软件下载页面
- `lib/package/wifi_detection.py`: 网络检测工具

#### 2. 开闭原则
对扩展开放，对修改关闭：
- 添加新软件类别时，只需添加新文件
- 不需要修改现有代码结构

#### 3. 依赖倒置
高层模块不依赖低层模块：
- 主程序通过抽象接口调用功能模块
- 便于替换实现

### 目录结构规范

```
project/
├── src/              # 应用程序主代码
│   ├── __init__.py
│   └── main_page.py
│
├── lib/              # 可复用的功能库
│   ├── page/         # UI 页面组件
│   └── package/      # 工具包
│
├── data/             # 数据文件
│   └── data.json
│
├── res/              # 资源文件
│   ├── IMG/
│   └── sound/
│
├── test/             # 测试代码
│   └── test_func/
│
└── docs/             # 文档
    ├── README.md
    ├── API_REFERENCE.md
    └── DEVELOPER_GUIDE.md
```

---

## 扩展开发

### 添加新的软件类别

#### 步骤 1: 创建页面文件

在 `lib/page/` 目录创建 `new_category.py`:

```python
"""新类别下载页面模块

提供新类别软件的下载界面
"""
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os


class NewCategory(tk.Toplevel):
    """新类别下载窗口类
    
    用于显示新类别软件相关的下载选项和功能
    """
    def __init__(self):
        # 调用父类构造函数
        tk.Toplevel.__init__(self)
        self.title("新类别下载")
        self.geometry("300x300")
        self.resizable(False, False)
        
        # 设置图标
        project_root = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)
        else:
            print(f"警告：图标文件不存在 {icon_path}")
        
        # TODO: 添加你的界面逻辑
        # 示例：添加一个标签
        label = ttk.Label(self, text="新类别软件列表")
        label.pack(pady=20)


if __name__ == '__main__':
    app = NewCategory()
    app.mainloop()
```

#### 步骤 2: 注册模块

编辑 `lib/__init__.py`:

```python
# 添加导入
from .page import new_category

# 添加到 __all__
__all__ = ["input", "music", "video",
           "nowifi", "wifi_detection","browser", "media", "chat",
           "new_category"]  # 新增

# 创建别名
new_category_page = new_category.NewCategory  # 新增
```

#### 步骤 3: 添加主界面按钮

编辑 `src/main_page.py`:

```python
def __init__(self):
    # ... 现有代码 ...
    
    def new_open():
        """打开新类别下载窗口"""
        new_win = lib.new_category_page()
        new_win.mainloop()
    
    new_app = ttk.Button(self,
                         text="新类别",
                         command=new_open,
                         bootstyle="outline",
                         width=38)
    new_app.grid(row=X, column=0, pady=10)  # 调整行号
```

#### 步骤 4: 添加数据配置

编辑 `data/data.json`:

```json
{
    "new_category": {
        "software1": {
            "num": 1,
            "title": "软件 1",
            "url": "https://example.com/software1"
        },
        "software2": {
            "num": 2,
            "title": "软件 2",
            "url": "https://example.com/software2"
        }
    }
}
```

---

### 添加新的网络检测方式

#### 示例：添加移动网络检测

创建 `lib/package/mobile_network.py`:

```python
"""移动网络检测模块

检测 4G/5G 移动网络连接状态
"""
import socket


def check_mobile_network():
    """检测移动网络连接
    
    Returns:
        tuple: (connected, message, info)
    """
    try:
        # 尝试连接
        host = "8.8.8.8"
        port = 53
        socket.setdefaulttimeout(3)
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            return True, "移动网络已连接", {"type": "4G/5G"}
        else:
            return False, "移动网络未连接", None
    except Exception as e:
        return False, f"移动网络检测出错：{str(e)}", None
```

更新 `get_network_info()`:

```python
def get_network_info():
    """获取网络连接信息"""
    wifi_connected, wifi_msg, wifi_info = check_wifi_status()
    ethernet_connected, eth_msg, eth_info = check_ethernet_status()
    mobile_connected, mobile_msg, mobile_info = check_mobile_network()
    
    result = {
        "wifi": {...},
        "ethernet": {...},
        "mobile": {
            "connected": mobile_connected,
            "message": mobile_msg,
            "info": mobile_info
        },
        "any_connected": wifi_connected or ethernet_connected or mobile_connected
    }
    
    return result
```

---

## 调试技巧

### 1. 使用打印调试

```python
def check_network_on_startup(self):
    print("=== 开始网络检测 ===")
    network_info = lib.wifi_detection.get_network_info()
    print(f"WiFi 状态：{network_info['wifi']['message']}")
    print(f"以太网状态：{network_info['ethernet']['message']}")
    print(f"总体状态：{'已连接' if network_info['any_connected'] else '未连接'}")
```

### 2. 使用断点调试

在 IDE 中设置断点：
```python
def problematic_function():
    x = calculate_value()  # 在此行设置断点
    print(f"计算结果：{x}")
    return x
```

### 3. 异常捕获和日志

```python
import traceback

try:
    result = risky_operation()
except Exception as e:
    print(f"发生错误：{e}")
    print("详细堆栈:")
    traceback.print_exc()
```

### 4. 使用 logging 模块

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# 使用日志
logger.debug("调试信息")
logger.info("一般信息")
logger.warning("警告信息")
logger.error("错误信息")
```

---

## 测试指南

### 单元测试示例

创建测试文件 `test/test_network.py`:

```python
import unittest
from lib.package import wifi_detection


class TestNetworkDetection(unittest.TestCase):
    """网络检测功能测试"""
    
    def test_check_wifi_status_returns_tuple(self):
        """测试 WiFi 检测返回元组"""
        result = wifi_detection.check_wifi_status()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
    
    def test_get_network_info_returns_dict(self):
        """测试网络信息返回字典"""
        result = wifi_detection.get_network_info()
        self.assertIsInstance(result, dict)
        self.assertIn("wifi", result)
        self.assertIn("ethernet", result)
        self.assertIn("any_connected", result)
    
    def test_any_connected_is_boolean(self):
        """测试 any_connected 是布尔值"""
        result = wifi_detection.get_network_info()
        self.assertIsInstance(result["any_connected"], bool)


if __name__ == '__main__':
    unittest.main()
```

### 运行测试

```bash
# 运行单个测试文件
python -m unittest test.test_network

# 运行所有测试
python -m unittest discover test
```

---

## 打包发布

### 使用 PyInstaller

#### 1. 安装 PyInstaller

```bash
pip install pyinstaller
```

#### 2. 创建 spec 文件

```bash
pyi-makespec --onefile --windowed src/main_page.py
```

#### 3. 编辑 spec 文件

编辑生成的 `main_page.spec`:

```python
a = Analysis(
    ['src/main_page.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('data/data.json', 'data'),
        ('res', 'res'),
    ],
    hiddenimports=['lib.page.music', 'lib.page.video', ...],  # 所有页面
    ...
)
```

#### 4. 构建

```bash
pyinstaller main_page.spec
```

#### 5. 测试可执行文件

```bash
dist/main_page.exe
```

### 优化建议

1. **减小体积**:
   - 使用 UPX 压缩
   - 排除不必要的模块

2. **添加图标**:
   ```bash
   pyinstaller --icon=res/IMG/logo.ico ...
   ```

3. **版本信息**:
   创建 `version.txt`:
   ```
   VSVersionInfo(
     ffi=FixedFileInfo(
       filevers=(0, 2, 0, 0),
       prodvers=(0, 2, 0, 0),
       mask=0x3f,
       flags=0x0,
       OS=0x40004,
       fileType=0x1,
       subtype=0x0,
       date=(0, 0)
     ),
     kids=[...],
   )
   ```

---

## 性能优化

### 1. 延迟加载

```python
class Main(tk.Tk):
    def __init__(self):
        # 先初始化基本界面
        tk.Tk.__init__(self)
        self.setup_ui()
        
        # 延迟进行网络检测
        self.after(100, self.check_network_on_startup)
```

### 2. 异步操作

```python
import threading

def async_network_check():
    """在后台线程中进行网络检测"""
    network_info = lib.wifi_detection.get_network_info()
    # 更新 UI（需要在主线程）
    self.after(0, lambda: self.update_ui(network_info))

thread = threading.Thread(target=async_network_check)
thread.start()
```

### 3. 缓存数据

```python
from functools import lru_cache

@lru_cache(maxsize=1)
def get_cached_network_info():
    """缓存网络检测结果"""
    return lib.wifi_detection.get_network_info()
```

---

## Git 工作流

### 分支管理

```bash
# 主分支
git checkout main

# 开发分支
git checkout -b develop

# 功能分支
git checkout -b feature/new-category
```

### 提交规范

```bash
# 格式：<type>(<scope>): <subject>

# 示例
git commit -m "feat(page): 添加新的音乐软件下载页面"
git commit -m "fix(network): 修复 WiFi 检测的异常处理"
git commit -m "docs(readme): 更新 README 文档"
git commit -m "refactor(ui): 重构主界面布局代码"
```

**类型说明**:
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建工具、依赖管理等

---

## 常见问题

### Q1: 如何调试 GUI 界面问题？

**A**: 
1. 使用 `print()` 输出关键信息
2. 使用 IDE 的调试器
3. 启用 tkinter 的事件追踪：
```python
app = Main()
app.tk.call('tk', 'busy', 'hold', app._w)
app.mainloop()
```

### Q2: pywifi 在某些设备上无法工作？

**A**: 
1. 确保安装了 Npcap（Windows）
2. 以管理员权限运行
3. 添加异常处理，优雅降级

### Q3: 如何处理中文路径问题？

**A**:
```python
# 使用 pathlib 处理路径
from pathlib import Path
icon_path = Path(__file__).parent / "res" / "IMG" / "logo.ico"
self.iconbitmap(str(icon_path))
```

---

## 贡献流程

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 资源链接

- [Python 官方文档](https://docs.python.org/zh-cn/3/)
- [tkinter 文档](https://docs.python.org/zh-cn/3/library/tkinter.html)
- [ttkbootstrap 文档](https://github.com/israel-dryer/ttkbootstrap)
- [pywifi 文档](https://github.com/clipcard/pywifi)
- [PEP 8 代码风格指南](https://peps.python.org/pep-0008/)

---

*最后更新：2026 年 3 月 15 日*
