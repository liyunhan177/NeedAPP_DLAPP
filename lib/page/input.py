"""输入法下载页面模块

提供输入法软件下载的图形用户界面
"""
import ttkbootstrap as tk
from ttkbootstrap.constants import *
import os
import lib
import webbrowser

class Input(tk.Window):
    """输入法下载窗口类，继承自 ttkbootstrap.Window
    
    用于显示输入法软件相关的下载选项和功能
    """
    def __init__(self):
        # 调用父类构造函数初始化窗口
        try:
            lib.log_user_action("打开窗口", "输入法下载窗口初始化", "InputPage")
            tk.Window.__init__(self,
                               themename="litera",
                               title="输入法下载",
                               size=(300, 300),
                               minsize=(300, 300),  # 窗口的最小宽高
                               resizable=None)
            
            # 设置图标路径
            # 获取项目根目录（向上三层）
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)  # 设置窗口图标
                lib.log_app_event("资源加载", "图标加载成功", f"InputPage: {icon_path}")
            else:
                lib.log_warning("资源缺失", "图标文件不存在", "InputPage", icon_path)
                print(f"警告：图标文件不存在 {icon_path}")
            
            lib.log_app_event("窗口就绪", "输入法下载窗口初始化完成", "InputPage")
        except Exception as e:
            lib.log_error("窗口初始化异常", str(e), "InputPage")
            raise

        # 定义各个输入法的下载链接打开函数
        def open_sogou():
            """打开搜狗输入法下载页面"""
            lib.log_user_action("点击下载", "打开搜狗输入法下载页面", "InputPage")
            webbrowser.open("https://pinyin.sogou.com/")

        def open_baidu():
            """打开百度输入法下载页面"""
            lib.log_user_action("点击下载", "打开百度输入法下载页面", "InputPage")
            webbrowser.open("https://srf.baidu.com/input/")

        def open_xunfei():
            """打开讯飞输入法下载页面"""
            lib.log_user_action("点击下载", "打开讯飞输入法下载页面", "InputPage")
            webbrowser.open("https://srf.xunfei.cn/index.html#/")

        def open_rime():
            """打开 Rime 输入法下载页面"""
            lib.log_user_action("点击下载", "打开 Rime 输入法下载页面", "InputPage")
            webbrowser.open("https://rime.im/")

        # 创建搜狗输入法下载按钮
        sogou_dl_btn = tk.Button(self,
                                text="搜狗输入法",
                                command=open_sogou,
                                width=150)
        sogou_dl_btn.pack(pady=10)

        # 创建百度输入法下载按钮
        baidu_dl_btn = tk.Button(self,
                                text="百度输入法",
                                command=open_baidu,
                                width=150)
        baidu_dl_btn.pack()

        # 创建讯飞输入法下载按钮
        xunfei_dl_btn = tk.Button(self,
                                text="讯飞输入法",
                                command=open_xunfei,
                                width=150)
        xunfei_dl_btn.pack()

        # 创建 Rime 输入法下载按钮
        rime_dl_btn = tk.Button(self,
                                text="小狼毫 (Rime)",
                                command=open_rime,
                                width=150)
        rime_dl_btn.pack(pady=10)

if __name__ == '__main__':
    input_app = Input()
    input_app.mainloop()
