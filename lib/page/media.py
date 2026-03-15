"""媒体播放器下载页面模块

提供媒体播放器软件下载的图形用户界面
"""
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os

class Media(tk.Toplevel):
    """媒体播放器下载窗口类，继承自 tkinter.Toplevel
    
    用于显示媒体播放器软件相关的下载选项和功能
    """
    def __init__(self):
        # 调用父类构造函数初始化窗口
        tk.Toplevel.__init__(self)
        self.title("播放器下载")
        self.geometry("300x300")  # 设置窗口大小
        self.resizable(False, False)  # 禁止调整窗口大小

        # 获取项目根目录（向上三层）并设置图标
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)  # 设置窗口图标
        else:
            print(f"警告：图标文件不存在 {icon_path}")

if __name__ == '__main__':
    media = Media()
    media.mainloop()

