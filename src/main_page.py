import sys, pathlib
import lib as lib
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import tkinter as tk
import logging

# 初始化日志记录器
logger = lib.setup_logger("NeedAPP_DLAPP", logging.INFO)

# 将项目根目录添加到系统路径，以便正确导入模块
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

class Main(tk.Tk):
    """
    主应用程序类，继承自 tkinter.Tk
    负责创建主窗口、初始化界面组件和网络检测
    """
    def __init__ (self):
        # 调用父类构造函数初始化主窗口
        tk.Tk.__init__(self)
        self.title("常用软件下载")
        self.geometry("300x300")
        self.resizable(False, False)  # 禁止调整窗口大小
        
        # 设置应用程序图标
        icon_path = pathlib.Path(__file__).resolve().parents[1] / "res" / "IMG" / "logo.ico"
        try:
            self.iconbitmap(str(icon_path))
        except Exception:
            pass  # 如果图标加载失败，不显示错误，继续执行

        # 启动时检测网络状态（WiFi 和以太网）
        self.check_network_on_startup()

        # 定义各个软件类别的打开窗口函数
        def music_open():
            """打开音乐软件下载窗口"""
            music_win = lib.music_page()
            music_win.mainloop()

        def video_open():
            """打开视频软件下载窗口"""
            video_win = lib.video_page()
            video_win.mainloop()

        def input_open():
            """打开输入法下载窗口"""
            input_win = lib.input_page()
            input_win.mainloop()

        def browser_open():
            """打开浏览器下载窗口"""
            browser_win = lib.browser_page()
            browser_win.mainloop()

        def media_open():
            """打开媒体播放器下载窗口"""
            media_win = lib.media_page()
            media_win.mainloop()

        def chat_open():
            """打开聊天软件下载窗口"""
            chat_win = lib.chat_page()
            chat_win.mainloop()

        # 创建音乐软件按钮
        music_app = ttk.Button(self,
                                text="音乐软件",
                                command=music_open,  # 点击时调用 music_open 函数
                                bootstyle="outline",  # 使用轮廓样式
                                width=38)
        music_app.grid(row=0, column=0, pady=10,  padx=5)

        # 创建视频软件按钮
        video_app = ttk.Button(self,
                                text="视频软件",
                                command=video_open,
                                bootstyle="outline",
                                width=38)
        video_app.grid(row=1, column=0)

        # 创建输入法按钮
        input_app = ttk.Button(self,
                                text="输入法",
                                command=input_open,
                                bootstyle="outline",
                                width=38)
        input_app.grid(row=2, column=0, pady=10)

        # 创建浏览器按钮
        browser_app = ttk.Button(self,
                                text="浏览器",
                                command=browser_open,
                                bootstyle="outline",
                                width=38)
        browser_app.grid(row=3, column=0)

        # 创建媒体播放器按钮
        media_app = ttk.Button(self,
                                text="媒体播放器",
                                command=media_open,
                                bootstyle="outline",
                                width=38)
        media_app.grid(row=4, column=0, pady=10)

        # 创建聊天软件按钮
        chat_app = ttk.Button(self,
                               text="聊天软件",
                               command=chat_open,
                               bootstyle="outline",
                               width=38)
        chat_app.grid(row=5, column=0)

        # 创建退出按钮
        exit_func = ttk.Button(self,
                               text="退出",
                               command=self.destroy,  # 关闭窗口
                               bootstyle="danger-outline",  # 使用危险样式（红色）
                               width=38)
        exit_func.grid(row=6, column=0, pady=10)
    
    def check_network_on_startup(self):
        """
        启动时检测网络状态（WiFi 和以太网）
        未连接任何网络则提醒并关闭应用，确保用户有良好的使用体验
        """
        try:
            network_info = lib.wifi_detection.get_network_info()
            
            if not network_info["any_connected"]:
                # 两种网络都未连接，显示警告信息
                msg = "检测到您未连接任何网络！\n\n"
                msg += f"WiFi 状态：{network_info['wifi']['message']}\n"
                msg += f"以太网状态：{network_info['ethernet']['message']}\n\n"
                msg += "为了获得更好的使用体验，请先连接网络。\n\n应用将自动关闭。"
                messagebox.showwarning("网络未连接", msg)
                self.destroy()
                sys.exit(0)
            else:
                # 至少有一种网络已连接 - 显示主界面，记录网络状态信息
                logger.info("=== 网络连接状态 ===")
                logger.info(f"WiFi: {network_info['wifi']['message']}")
                logger.info(f"以太网：{network_info['ethernet']['message']}")
                if network_info['wifi']['info']:
                    logger.info(f"WiFi SSID: {network_info['wifi']['info'].get('ssid', 'N/A')}")
                    logger.info(f"WiFi 信号强度：{network_info['wifi']['info'].get('signal', 'N/A')} dBm")
                if network_info['ethernet']['info']:
                    logger.info(f"以太网 IP: {network_info['ethernet']['info'].get('ip', 'N/A')}")
                logger.info("\n✓ 网络已连接，正在启动应用...")
        except Exception as e:
            # 检测出错时仍然允许应用启动，记录错误信息
            logger.error(f"网络检测出错：{str(e)}")
            logger.warning("继续启动应用...")

if __name__ == '__main__':
    app = Main()
    app.mainloop()

