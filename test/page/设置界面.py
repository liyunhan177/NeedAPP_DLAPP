import ttkbootstrap as tk
from ttkbootstrap.constants import *
import os
import lib

class Settings(tk.Window):
    def __init__(self):
        try:
            lib.log_user_action("打开窗口", "设置窗口初始化", "BrowserPage")
            tk.Window.__init__(self,
                               themename="litera",
                               title="设置",
                               size=(300, 300),
                               minsize=(300, 300),  # 窗口的最小宽高
                               resizable=None)

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


if __name__ == '__main__':
    settings = Settings()
    settings.mainloop()
