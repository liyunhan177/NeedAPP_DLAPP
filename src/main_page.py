import sys, pathlib
import lib as lib
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

class Main(tk.Tk):
    def __init__ (self):
        tk.Tk.__init__(self)
        self.title("常用软件下载")
        self.geometry("400x300")
        self.resizable(False, False)
        
        icon_path = pathlib.Path(__file__).resolve().parents[1] / "res" / "IMG" / "logo.ico"
        try:
            self.iconbitmap(str(icon_path))
        except Exception:
            pass

        def music_open():
            music_win = lib.music_page()
            music_win.mainloop()

        def video_open():
            video_win = lib.video_page()
            video_win.mainloop()

        def input_open():
            input_win = lib.input_page()
            input_win.mainloop()

        def browser_open():
            browser_win = lib.browser_page()
            browser_win.mainloop()

        def media_open():
            media_win = lib.media_page()
            media_win.mainloop()

        music_app = ttk.Button(self,
                                text="音乐软件",
                                command=music_open,
                                bootstyle="outline",
                                width=13)
        music_app.grid(row=0, column=0, pady=10,  padx=5)

        video_app = ttk.Button(self,
                                text="视频软件",
                                command=video_open,
                                bootstyle="outline",
                                width=13)
        video_app.grid(row=1, column=0)

        input_app = ttk.Button(self,
                                text="输入法",
                                command=input_open,
                                bootstyle="outline",
                                width=13)
        input_app.grid(row=2, column=0, pady=10)

        browser_app = ttk.Button(self,
                                text="浏览器",
                                command=browser_open,
                                bootstyle="outline",
                                width=13)
        browser_app.grid(row=3, column=0)

        media_app = ttk.Button(self,
                                text="媒体播放器",
                                command=media_open,
                                bootstyle="outline",
                                width=13)
        media_app.grid(row=4, column=0, pady=10)

if __name__ == '__main__':
    app = Main()
    app.mainloop()

