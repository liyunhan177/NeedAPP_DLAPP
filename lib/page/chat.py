"""聊天软件下载页面模块

提供聊天软件（社交应用）下载的图形用户界面
"""
import ttkbootstrap as tk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os

class Chat(tk.Window):
    """聊天软件下载窗口类，继承自 ttkbootstrap.Window
    
    用于显示聊天软件相关的下载选项和功能
    """
    def __init__(self):
        # 调用父类构造函数初始化窗口
        tk.Window.__init__(self,
                           themename="litera",
                           title="聊天软件下载",
                           size=(300, 300),
                           minsize=(300, 300),  # 窗口的最小宽高
                           resizable=None)

        # 获取项目根目录（向上三层）并设置图标
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)  # 设置窗口图标
        else:
            print(f"警告：图标文件不存在 {icon_path}")

if __name__ == '__main__':
    chat_app = Chat()
    chat_app.mainloop()
