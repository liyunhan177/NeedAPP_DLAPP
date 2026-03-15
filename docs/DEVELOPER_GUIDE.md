# 开发者指南

## 快速开始

### 环境搭建

#### 1. 系统要求
- **操作系统**: Windows 10/11
- **Python 版本**: Python 3.8+
- **必需依赖**: 
  - pywifi
  - ttkbootstrap
  - logging

#### 2. 克隆项目
```bash
git clone https://github.com/liyunhan177/NeedAPP_DLAPP.git
cd NeedAPP_DLAPP
```

#### 3. 创建虚拟环境（推荐）
```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat
```

#### 4. 安装依赖
```bash
pip install pywifi ttkbootstrap
```

#### 5. 验证安装
```bash
python src/main_page.py
```

---

## 开发流程

### 添加新的软件类别

#### 步骤 1: 在 data.json 中添加数据

编辑 `data/data.json`，添加新的软件类别：

```json
{
  "office": {
    "microsoft_office": {
      "num": 1,
      "title": "Microsoft Office",
      "url": "https://www.microsoft.com/zh-cn/microsoft-365"
    },
    "wps": {
      "num": 2,
      "title": "WPS Office",
      "url": "https://www.wps.cn/"
    }
  }
}
```

#### 步骤 2: 创建新的页面模块

在 `lib/page/` 目录下创建新文件，例如 `office.py`：

```python
"""办公软件下载页面模块"""
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
import webbrowser
import os

class Office(tk.Toplevel):
    """办公软件下载窗口类"""
    
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("办公软件下载")
        self.geometry("300x400")  # 根据软件数量调整高度
        self.resizable(False, False)
        
        # 设置图标
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)
        
        # 加载数据
        self.load_data()
        
        # 创建 UI
        self.create_widgets()
    
    def load_data(self):
        """加载软件数据"""
        try:
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            data_path = os.path.join(project_root, "data", "data.json")
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.software_list = data.get('office', [])
        except Exception as e:
            messagebox.showerror("错误", f"加载数据失败：{str(e)}")
            self.software_list = []
    
    def create_widgets(self):
        """创建界面组件"""
        for software in self.software_list:
            btn = ttk.Button(
                self,
                text=software['title'],
                command=lambda url=software['url']: self.open_website(url),
                bootstyle="outline",
                width=38
            )
            btn.pack(pady=5, padx=10)
    
    def open_website(self, url):
        """打开官方网站"""
        webbrowser.open(url)

if __name__ == '__main__':
    office = Office()
    office.mainloop()
```

#### 步骤 3: 在主程序中注册新页面

编辑 `src/main_page.py`，在 `__init__` 方法中添加：

```python
def office_open():
    """打开办公软件下载窗口"""
    office_win = lib.office_page()
    office_win.mainloop()

# 添加按钮
office_app = ttk.Button(
    self,
    text="办公软件",
    command=office_open,
    bootstyle="outline",
    width=38
)
office_app.grid(row=7, column=0, pady=10)  # 选择合适的行列位置
```

---

### 修改现有软件列表

#### 直接编辑 data.json

```json
{
  "music": {
    "new_music_app": {  // 添加新软件
      "num": 7,
      "title": "新音乐应用",
      "url": "https://example.com/"
    }
  }
}
```

**注意事项**:
- 保持 `num` 字段递增
- 确保 URL 是官方网站
- 使用有意义的键名（如 `qq_music`, `netease_cloud`）

---

## UI 定制指南

### 修改主题颜色

ttkbootstrap 支持多种内置主题：

```python
import ttkbootstrap as ttk
from ttkbootstrap.themes import get_themes

# 查看可用主题
themes = get_themes()
print(themes)  # ['litera', 'minty', 'pulse', 'flatly', ...]

# 在 Main 类构造函数中设置主题
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style = ttk.Style(theme='darkly')  # 设置主题
        # ... 其他初始化代码
```

### 自定义按钮样式

```python
# 标准轮廓样式
btn = ttk.Button(self, text="按钮", bootstyle="outline")

# 主色调按钮
btn = ttk.Button(self, text="按钮", bootstyle="primary")

# 成功样式
btn = ttk.Button(self, text="按钮", bootstyle="success-outline")

# 危险样式
btn = ttk.Button(self, text="退出", bootstyle="danger-outline")

# 警告样式
btn = ttk.Button(self, text="警告", bootstyle="warning-outline")
```

### 调整布局

当前使用 grid 布局，可以调整为 pack 或 place：

```python
# Grid 布局（当前使用）
btn.grid(row=0, column=0, pady=10, padx=5)

# Pack 布局
btn.pack(pady=10, padx=5, fill=tk.X)

# Place 布局（绝对定位）
btn.place(x=50, y=100, width=200, height=40)
```

---

## 功能扩展

### 实现下载功能

#### 基础下载器

```python
import requests
import threading

def download_file(url, save_path):
    """下载文件"""
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        with open(save_path, 'wb') as f:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    # 更新进度条
                    progress = (downloaded / total_size) * 100
                    print(f"下载进度：{progress:.2f}%")
        
        return True
    except Exception as e:
        print(f"下载失败：{str(e)}")
        return False

# 在线程中使用，避免阻塞 UI
def start_download(url, save_path):
    thread = threading.Thread(target=download_file, args=(url, save_path))
    thread.start()
```

#### 带进度条的下载

```python
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class DownloadWindow(tk.Toplevel):
    def __init__(self, url, filename):
        tk.Toplevel.__init__(self)
        self.title("下载中...")
        self.geometry("400x150")
        
        self.label = ttk.Label(self, text=f"正在下载：{filename}")
        self.label.pack(pady=10)
        
        self.progress = ttk.Progressbar(
            self, 
            orient=tk.HORIZONTAL, 
            length=300, 
            mode='determinate'
        )
        self.progress.pack(pady=10)
        
        self.status_label = ttk.Label(self, text="准备开始...")
        self.status_label.pack(pady=10)
        
        # 开始下载线程
        thread = threading.Thread(
            target=self.download_with_progress, 
            args=(url, filename)
        )
        thread.start()
    
    def download_with_progress(self, url, filename):
        """带进度的下载"""
        try:
            response = requests.get(url, stream=True)
            total = int(response.headers.get('content-length', 0))
            
            with open(filename, 'wb') as f:
                downloaded = 0
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        # 更新进度条（需要在主线程中执行）
                        if total > 0:
                            progress = (downloaded / total) * 100
                            self.progress['value'] = progress
                            self.status_label.config(
                                text=f"已下载：{downloaded/1024/1024:.2f}MB / "
                                     f"{total/1024/1024:.2f}MB ({progress:.1f}%)"
                            )
            
            self.status_label.config(text="下载完成！")
            messagebox.showinfo("成功", "文件下载完成！")
            
        except Exception as e:
            self.status_label.config(text="下载失败")
            messagebox.showerror("错误", f"下载失败：{str(e)}")
```

---

### 添加搜索功能

```python
class SearchablePage(tk.Toplevel):
    def __init__(self, category):
        tk.Toplevel.__init__(self)
        self.title(f"{category}软件下载")
        self.geometry("400x500")
        
        self.category = category
        self.software_list = []
        
        # 搜索框
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(
            self, 
            textvariable=self.search_var,
            font=('Arial', 12)
        )
        self.search_entry.pack(pady=10, padx=10, fill=tk.X)
        
        # 搜索按钮
        search_btn = ttk.Button(
            self,
            text="搜索",
            command=self.search_software,
            bootstyle="primary"
        )
        search_btn.pack(pady=5)
        
        # 软件列表框
        self.listbox_frame = ttk.Frame(self)
        self.listbox_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.load_data()
        self.display_software(self.software_list)
    
    def load_data(self):
        """加载数据"""
        with open('data/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.software_list = data.get(self.category, [])
    
    def display_software(self, software_list):
        """显示软件列表"""
        # 清空现有内容
        for widget in self.listbox_frame.winfo_children():
            widget.destroy()
        
        for software in software_list:
            btn = ttk.Button(
                self.listbox_frame,
                text=f"{software['title']} - {software['url']}",
                command=lambda url=software['url']: self.open_website(url),
                bootstyle="outline"
            )
            btn.pack(pady=2, fill=tk.X)
    
    def search_software(self):
        """搜索软件"""
        keyword = self.search_var.get().lower()
        if not keyword:
            self.display_software(self.software_list)
            return
        
        filtered = [
            s for s in self.software_list 
            if keyword in s['title'].lower() or keyword in s['url'].lower()
        ]
        self.display_software(filtered)
```

---

## 测试指南

### 单元测试示例

```python
import unittest
from lib.package import wifi_detection

class TestNetworkDetection(unittest.TestCase):
    
    def test_wifi_detection_return_type(self):
        """测试 WiFi 检测返回类型"""
        result = wifi_detection.check_wifi_status()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
    
    def test_ethernet_detection_return_type(self):
        """测试以太网检测返回类型"""
        result = wifi_detection.check_ethernet_status()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
    
    def test_get_network_info_structure(self):
        """测试网络信息结构"""
        result = wifi_detection.get_network_info()
        
        self.assertIn('wifi', result)
        self.assertIn('ethernet', result)
        self.assertIn('any_connected', result)
        
        self.assertIn('connected', result['wifi'])
        self.assertIn('message', result['wifi'])
        self.assertIn('info', result['wifi'])

if __name__ == '__main__':
    unittest.main()
```

### 手动测试清单

#### UI 测试
- [ ] 主窗口正常显示
- [ ] 所有按钮可点击
- [ ] 图标正确加载
- [ ] 窗口大小固定
- [ ] 各子页面正常打开

#### 功能测试
- [ ] WiFi 断开时显示警告
- [ ] WiFi 连接时正常启动
- [ ] 以太网连接检测正常
- [ ] 官网跳转功能正常
- [ ] 数据加载无错误

#### 边界测试
- [ ] 无网络时行为
- [ ] 数据文件缺失时行为
- [ ] 图标文件缺失时行为
- [ ] 异常网络环境处理

---

## 调试技巧

### 打印调试信息

```python
import sys

# 启用详细输出
DEBUG = True

def debug_print(*args):
    if DEBUG:
        print("[DEBUG]", *args, file=sys.stderr)

# 使用示例
debug_print("加载数据:", data)
```

### 使用日志模块

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# 使用示例
logger.info("应用启动")
logger.debug(f"网络状态：{network_info}")
logger.error(f"发生错误：{str(e)}")
```

---

## 打包发布

### 使用 PyInstaller 打包

#### 1. 安装 PyInstaller
```bash
pip install pyinstaller
```

#### 2. 创建 spec 文件
```bash
pyi-makespec --windowed --icon=res/IMG/logo.ico src/main_page.py
```

#### 3. 编辑 main_page.spec
```python
a = Analysis(
    ['src/main_page.py'],
    datas=[
        ('data/data.json', 'data'),
        ('res/IMG/logo.ico', 'res/IMG'),
    ],
    # ... 其他配置
)
```

#### 4. 打包
```bash
pyinstaller main_page.spec
```

#### 5. 测试打包结果
```bash
# 在 dist 目录运行生成的 exe
.\dist\main_page\main_page.exe
```

---

## 性能优化建议

### 1. 延迟加载数据
```python
# 不要一次性加载所有数据
def load_data_on_demand(self, category):
    """按需加载特定类别数据"""
    with open('data/data.json', 'r', encoding='utf-8') as f:
        all_data = json.load(f)
    return all_data.get(category, [])
```

### 2. 使用缓存
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def get_software_data(category):
    """缓存软件数据"""
    with open('data/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get(category, [])
```

### 3. 异步加载图片
```python
def load_image_async(image_path):
    """异步加载图片"""
    from PIL import Image, ImageTk
    
    def load():
        img = Image.open(image_path)
        return ImageTk.PhotoImage(img)
    
    thread = threading.Thread(target=load)
    thread.start()
    return thread
```

---

## 常见问题解决

### Q1: pywifi 导入错误
**问题**: `ModuleNotFoundError: No module named 'pywifi'`

**解决**:
```bash
pip install pywifi
# 或使用国内镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pywifi
```

### Q2: WiFi 检测权限不足
**问题**: 需要管理员权限才能扫描 WiFi

**解决**:
- 以管理员身份运行程序
- 或在设备管理器中启用无线网卡

### Q3: 中文乱码
**问题**: JSON 文件读取出现乱码

**解决**:
```python
# 确保使用 UTF-8 编码
with open('data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

### Q4: 图标不显示
**问题**: iconbitmap 调用失败

**解决**:
```python
try:
    self.iconbitmap(str(icon_path))
except Exception:
    pass  # 优雅地忽略错误
```

---

## 贡献代码规范

### 代码风格
- 遵循 PEP 8 规范
- 使用 4 空格缩进
- 行宽不超过 100 字符
- 函数和类添加文档字符串

### Git 提交规范
```bash
# 功能添加
git commit -m "feat: 添加办公软件下载功能"

# Bug 修复
git commit -m "fix: 修复 WiFi 检测崩溃问题"

# 文档更新
git commit -m "docs: 更新 API 参考文档"

# 代码重构
git commit -m "refactor: 优化数据加载逻辑"

# 性能优化
git commit -m "perf: 使用缓存提升加载速度"
```

---

## 资源链接

### 官方文档
- [Python 官方文档](https://docs.python.org/zh-cn/3/)
- [Tkinter 文档](https://docs.python.org/zh-cn/3/library/tkinter.html)
- [ttkbootstrap 文档](https://ttkbootstrap.readthedocs.io/)
- [pywifi 文档](https://pypi.org/project/pywifi/)
- [JSON 文档](https://www.json.org/json-zh.html)
- [logging 文档](https://docs.python.org/zh-cn/3/library/logging.html)

### 相关工具
- [PyInstaller](https://www.pyinstaller.org/)
- [Pillow (图像处理)](https://pillow.readthedocs.io/)
- [Requests (HTTP 库)](https://requests.readthedocs.io/)

---

*最后更新时间：2026 年 3 月 15 日*
