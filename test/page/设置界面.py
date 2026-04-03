import ttkbootstrap as tk
from ttkbootstrap.constants import *
import os
import lib

class Settings(tk.Window):
    def __init__(self):
        tk.Window.__init__(self,
                           themename="litera",
                           title="设置",
                           size=(300, 300),
                           minsize=(300, 300),  # 窗口的最小宽高
                           maxsize=(300, 300),  # 窗口的最大宽高
                           resizable=None)

        notebook = tk.Notebook(self)
        notebook.pack(fill="both", expand=True)
        tab_general = tk.Frame(self)
        tab_customize = tk.Frame(self)
        tab_about = tk.Frame(self)
        notebook.add(tab_general, text="通用")
        notebook.add(tab_customize, text="个性化")
        notebook.add(tab_about, text="关于")

if __name__ == '__main__':
    settings = Settings()
    settings.mainloop()
