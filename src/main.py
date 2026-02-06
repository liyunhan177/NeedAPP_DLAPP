from lib.page.music import Music as music
from lib.page.video import Video as video
import tkinter as tk

class Main(tk.Tk):
    def __init__ (self):
        tk.Tk.__init__(self)
        self.title("常用软件下载")
        self.geometry("300x300")
        self.resizable(False, False)
        self.iconbitmap(r"..\res\IMG\logo.ico")

if __name__ == '__main__':
    app = Main()
    app.mainloop()