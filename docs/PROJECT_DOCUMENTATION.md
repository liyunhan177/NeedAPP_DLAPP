# NeedAPP_DLAPP 项目开发文档

## 项目概述

### 项目名称
NeedAPP_DLAPP - 常用软件及工具下载器

### 项目简介
一个基于 Python 和 Tkinter 的图形界面应用程序，旨在为用户提供方便快捷的软件下载服务。用户可以通过直观的图形界面选择需要下载的软件类型，并直接从官方网站进行下载。

### 版本信息
- **当前版本**: 0.4.0（详见 CHANGELOG_TEMPLATE.md）
- **开发语言**: Python
- **运行平台**: Windows
- **GUI 框架**: ttkbootstrap (基于 Tkinter)

---

## 技术架构

### 核心技术栈
1. **Python**: 主要编程语言
2. **Tkinter**: Python 标准 GUI 库
3. **ttkbootstrap**: 基于 Tkinter 的现代化 UI 主题库
4. **pywifi**: WiFi 网络检测库
5. **logging**: Python 日志库

### 项目结构

```
NeedAPP_DLAPP/
├── src/                      # 源代码目录
│   ├── main_page.py         # 主程序入口和主界面
│   └── __init__.py
├── lib/                      # 功能模块库
│   ├── page/                # 页面模块
│   │   ├── music.py         # 音乐软件下载页面
│   │   ├── video.py         # 视频软件下载页面
│   │   ├── input.py         # 输入法下载页面
│   │   ├── browser.py       # 浏览器下载页面
│   │   ├── media.py         # 媒体播放器下载页面
│   │   ├── chat.py          # 聊天软件下载页面
│   │   └── __init__.py
│   ├── package/             # 功能包
│   │   └── wifi_detection.py  # WiFi 检测工具
│   └── __init__.py
├── data/                     # 数据文件
│   └── data.json            # 软件信息数据
├── res/                      # 资源文件
│   ├── IMG/                 # 图片资源
│   │   ├── logo.ico         # 应用图标
│   │   └── UI/              # UI 相关图片
│   └── sound/               # 音频资源
├── test/                     # 测试文件
├── log/                       # 日志文件
├── docs/                     # 文档目录
├── pyproject.toml           # 项目配置文件
└── README.md                # 项目说明文档
```

---

## 核心模块说明

### 1. 主程序模块 (`src/main_page.py`)

#### 类：`Main(tk.Tk)`
主应用程序窗口类，负责：
- 创建和初始化主窗口
- 网络状态检测
- 各个功能页面的入口管理

#### 主要方法
- `__init__()`: 初始化主窗口，创建 UI 组件
- `check_network_on_startup()`: 启动时检测网络状态

#### 功能特性
- 支持 6 大软件类别的快速访问
- 启动时自动检测 WiFi 和以太网连接状态
- 未连接网络时显示友好提示并自动关闭
- 窗口固定大小 (300x300)，不可调整

### 2. 页面模块 (`lib/page/`)

每个页面模块都实现了特定类型软件的下载界面：

#### 模块列表
- **music.py**: 音乐软件下载页面 (QQ 音乐、网易云音乐等)
- **video.py**: 视频软件下载页面 (PotPlayer、VLC 等)
- **input.py**: 输入法下载页面 (搜狗、百度、QQ 等)
- **browser.py**: 浏览器下载页面 (Edge、Chrome 等)
- **media.py**: 媒体播放器下载页面 (Bilibili、抖音等)
- **chat.py**: 聊天软件下载页面 (微信、QQ、钉钉等)

#### 统一设计模式
所有页面类均继承自 `tk.Toplevel`，具有：
- 统一的窗口尺寸 (300x300)
- 固定的图标和样式
- 独立的软件列表展示

### 3. 网络检测模块 (`lib/package/wifi_detection.py`)

#### 核心函数

**`check_wifi_status()`**
- 功能：检测 WiFi 连接状态
- 返回：(是否连接，状态消息，连接信息)
- 使用 pywifi 库扫描 WiFi 网络

**`check_ethernet_status()`**
- 功能：检测以太网连接状态
- 方法：通过 socket 连接公共 DNS (8.8.8.8:53)
- 返回：(是否连接，状态消息，IP 信息)

**`get_network_info()`**
- 功能：综合获取 WiFi 和以太网状态
- 返回：包含详细网络信息的字典

### 4. 数据存储 (`data/data.json`)

#### 数据结构
采用 JSON 格式存储软件信息，按类别组织：

```json
{
  "category": {
    "software_id": {
      "num": 序号，
      "title": "软件名称",
      "url": "官方下载链接"
    }
  }
}
```

#### 支持的软件类别
1. **chat** (聊天软件): 微信、Tim、QQ、钉钉、飞书
2. **browser** (浏览器): Edge、Chrome、360、Firefox 等
3. **input** (输入法): 搜狗、百度、QQ、讯飞、Rime 等
4. **music** (音乐软件): QQ 音乐、网易云、酷狗等
5. **video** (视频播放): PotPlayer、VLC、KMPlayer 等
6. **media** (媒体平台): Bilibili、抖音、腾讯视频等

---

## 功能特性

### 已实现功能
✅ 项目初始化与基础架构搭建  
✅ 软件分类展示  
✅ 网络状态自动检测  
✅ 软件官网跳转功能  
✅ 模块化页面设计  
✅ 友好的错误处理

### 待实现功能
⬜ 本地安装包下载功能  
⬜ 软件下载进度显示  
⬜ 数据库存储（替代 JSON）  
⬜ 软件版本更新检测  
⬜ 用户自定义软件源  
⬜ 批量下载管理  
⬜ 界面美化与主题切换  
⬜ 项目打包为 exe  

---

## 安装与运行

### 环境要求
- Python 3.x
- Windows 操作系统
- 网络连接（WiFi 或以太网）

### 依赖安装
```bash
pip install pywifi ttkbootstrap
```

### 运行方式
```bash
python src/main_page.py
```

---

## 设计规范

### 代码规范
- 变量命名：驼峰命名法 (camelCase)
- 类命名：大驼峰命名法 (PascalCase)
- 函数注释：使用文档字符串 (docstring)
- 错误处理：使用 try-except 捕获异常

### UI 设计规范
- 按钮样式：outline 风格
- 按钮宽度：38 字符
- 间距设置：padx=5, pady=10

### 文件组织规范
- 所有页面模块放在 `lib/page/` 目录
- 工具模块放在 `lib/package/` 目录
- 资源文件统一放在 `res/` 目录
- 数据文件存放在 `data/` 目录

---

## 测试与调试

### 网络检测测试
```python
from lib.package import wifi_detection

result = wifi_detection.get_network_info()
print(f"WiFi: {result['wifi']['message']}")
print(f"以太网：{result['ethernet']['message']}")
```

### 页面模块测试
每个页面模块都支持独立运行测试：
```python
# 测试音乐页面
python lib/page/music.py
```

---

## 常见问题

### Q1: 图标加载失败
**原因**: 图标文件路径不存在  
**解决**: 检查 `res/IMG/logo.ico` 是否存在

### Q2: WiFi 检测出错
**原因**: pywifi 需要管理员权限或无线网卡驱动  
**解决**: 以管理员身份运行或检查网卡驱动

### Q3: 依赖安装失败
**原因**: pip 源问题或网络问题  
**解决**: 使用国内镜像源
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pywifi ttkbootstrap
```

---

## 开发计划

详细的版本更新日志和开发计划请查看 `CHANGELOG_TEMPLATE.md`

### 短期目标
- [ ] 完善所有页面模块的 UI 设计
- [ ] 实现软件直接下载功能
- [ ] 添加下载进度条
- [ ] 优化错误提示机制

### 中期目标
- [ ] 引入 SQLite 数据库管理软件信息
- [ ] 添加软件搜索功能
- [ ] 支持软件版本检测
- [ ] 增加软件评分和评论

### 长期目标
- [ ] 实现多线程下载
- [ ] 支持断点续传
- [ ] 添加软件管理功能
- [ ] 打包为独立 exe 程序
- [ ] 支持插件扩展系统

---

## 贡献指南

### 提交 Issue
遇到问题或有新想法时，欢迎提交 Issue

### 提交 PR
1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 代码规范
- 遵循 PEP 8 Python 代码规范
- 添加必要的注释和文档字符串
- 确保代码可测试性

---

## 许可证

本项目仅供个人学习和研究使用

---

## 联系方式

- **作者**: liyunhan177
- **GitHub**: [@liyunhan177](https://github.com/liyunhan177)
- **Bilibili**: [UID: 571556798](https://space.bilibili.com/571556798)

---

## 致谢

感谢所有为本项目做出贡献的开发者和用户！

特别感谢：
- ttkbootstrap 团队提供的优秀 UI 框架
- pywifi 团队提供的网络检测工具
- 所有提供软件下载源的合作方

---

*最后更新时间：2026 年 3 月 15 日*
