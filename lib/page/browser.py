"""浏览器下载页面模块

提供浏览器软件下载的图形用户界面
"""
import ttkbootstrap as tk
from ttkbootstrap.constants import *
import os
import lib
import webbrowser as web

class Browser(tk.Window):
    """浏览器下载窗口类，继承自 ttkbootstrap.Window
    
    用于显示浏览器软件相关的下载选项和功能
    """
    def __init__(self):
        # 调用父类构造函数初始化窗口
        try:
            lib.log_user_action("打开窗口", "浏览器下载窗口初始化", "BrowserPage")
            tk.Window.__init__(self,
                               themename="litera",
                               title="浏览器下载",
                               size=(300,300),
                               minsize=(300, 300),  # 窗口的最小宽高
                               resizable=None)
            
            # 设置图标路径
            # 获取项目根目录（向上三层）
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)  # 设置窗口图标
                lib.log_app_event("资源加载", "图标加载成功", f"BrowserPage: {icon_path}")
            else:
                lib.log_warning("资源缺失", "图标文件不存在", "BrowserPage", icon_path)
                print(f"警告：图标文件不存在 {icon_path}")
            
            lib.log_app_event("窗口就绪", "浏览器下载窗口初始化完成", "BrowserPage")
        except Exception as e:
            lib.log_error("窗口初始化异常", str(e), "BrowserPage")
            raise

        def open_edge():
            web.open("https://www.microsoft.com/zh-cn/edge/download?form=MA13FJ")

        def open_chrome():
            web.open("https://www.google.cn/intl/zh-CN/chrome/")

        def open_firefox():
            web.open("https://www.mozilla.org/zh-CN/firefox/new/")

        def open_tsz_security():
            web.open("https://browser.360.cn/")

        def open_tsz_extreme():
            web.open("https://browser.360.cn/ee/")

        def open_qq_browser():
            web.open("https://browser.qq.com/")

        edge_dl_btn = tk.Button(self,
                                text="Edge",
                                command=open_edge,
                                width=150)
        edge_dl_btn.pack(pady=10)

        chrome_dl_btn = tk.Button(self,
                                text="Chrome",
                                command=open_chrome,
                                width=150)
        chrome_dl_btn.pack()

        firefox_dl_btn = tk.Button(self,
                                text="Firefox",
                                command=open_firefox,
                                width=150)
        firefox_dl_btn.pack(pady=10)

        # tsz为360的英文缩写
        tsz_security_dl_btn = tk.Button(self,
                                text="360安全浏览器",
                                command=open_tsz_security,
                                width=150)
        tsz_security_dl_btn.pack()

        tsz_extreme_dl_btn = tk.Button(self,
                                text="360极速浏览器",
                                command=open_tsz_extreme,
                                width=150)
        tsz_extreme_dl_btn.pack(pady=10)

        qq_browser_dl_btn = tk.Button(self,
                                      text="QQ浏览器",
                                      command=open_qq_browser,
                                      width=150)
        qq_browser_dl_btn.pack()

if __name__ == '__main__':
    browser = Browser()
    browser.mainloop()
