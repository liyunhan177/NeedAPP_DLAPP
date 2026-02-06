import tkinter as tk
from tkinter import messagebox

class Video(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("音乐软件下载")
        self.geometry("300x300")
        self.resizable(False, False)
        self.iconbitmap(r"..\res\IMG\logo.ico")

if __name__ == '__main__':
    video = Video()
    video.mainloop()

