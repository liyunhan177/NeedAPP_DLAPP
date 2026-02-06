from lib.page.music import Music as music
from lib.page.video import Video as video
from lib.page.input import Input as input
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

class Main(tk.Tk):
    def __init__ (self):
        tk.Tk.__init__(self)
        self.title("常用软件下载")
        self.geometry("400x300")
        self.resizable(False, False)
        self.iconbitmap(r"..\res\IMG\logo.ico")

        def music_open():
            music_win = music()
            music_win.mainloop()

        def video_open():
            video_win = video()
            video_win.mainloop()

        def input_open():
            input_win = input()
            input_win.mainloop()

        music_app = ttk.Button(self,
                               text="音乐软件",
                               command=music_open,
                               bootstyle="outline",
                               width=13)
        music_app.grid(row=0, column=0, pady=10)

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

if __name__ == '__main__':
    app = Main()
    app.mainloop()