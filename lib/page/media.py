import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Media(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("播放器下载")
        self.geometry("300x300")
        self.resizable(False, False)
        # 设置图标路径
        import os
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)
        else:
            print(f"警告: 图标文件不存在 {icon_path}")

if __name__ == '__main__':
    media = Media()
    media.mainloop()

