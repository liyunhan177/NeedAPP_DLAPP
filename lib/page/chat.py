"""聊天软件下载页面模块

提供聊天软件（社交应用）下载的图形用户界面
"""
import ttkbootstrap as tk
from ttkbootstrap.constants import *
import os
import lib
import webbrowser

class Chat(tk.Window):
    """聊天软件下载窗口类，继承自 ttkbootstrap.Window
    
    用于显示聊天软件相关的下载选项和功能
    """
    def __init__(self):
        # 调用父类构造函数初始化窗口
        try:
            lib.log_user_action("打开窗口", "聊天软件下载窗口初始化", "ChatPage")
            tk.Window.__init__(self,
                               themename="litera",
                               title="聊天软件下载",
                               size=(300, 300),
                               minsize=(300, 300),  # 窗口的最小宽高
                               resizable=None)
            
            # 设置图标路径
            # 获取项目根目录（向上三层）
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)  # 设置窗口图标
                lib.log_app_event("资源加载", "图标加载成功", f"ChatPage: {icon_path}")
            else:
                lib.log_warning("资源缺失", "图标文件不存在", "ChatPage", icon_path)
                print(f"警告：图标文件不存在 {icon_path}")
            
            lib.log_app_event("窗口就绪", "聊天软件下载窗口初始化完成", "ChatPage")
        except Exception as e:
            lib.log_error("窗口初始化异常", str(e), "ChatPage")
            raise

        # 定义各个聊天软件的下载链接打开函数
        def open_wechat():
            """打开微信下载页面"""
            lib.log_user_action("点击下载", "打开微信下载页面", "ChatPage")
            webbrowser.open("https://weixin.qq.com/")

        def open_tim():
            """打开 Tim 下载页面"""
            lib.log_user_action("点击下载", "打开 Tim 下载页面", "ChatPage")
            webbrowser.open("https://tim.qq.com/")

        def open_qq():
            """打开 QQ 下载页面"""
            lib.log_user_action("点击下载", "打开 QQ 下载页面", "ChatPage")
            webbrowser.open("https://im.qq.com/")

        def open_dingtalk():
            """打开钉钉下载页面"""
            lib.log_user_action("点击下载", "打开钉钉下载页面", "ChatPage")
            webbrowser.open("https://www.dingtalk.com/download?spm=a213l2.13146415.0.0.7f151ef7QjOSlr")

        def open_feishu():
            """打开飞书下载页面"""
            lib.log_user_action("点击下载", "打开飞书下载页面", "ChatPage")
            webbrowser.open("https://www.feishu.cn/download")

        # 创建微信下载按钮
        wechat_dl_btn = tk.Button(self,
                                text="微信",
                                command=open_wechat,
                                width=150)
        wechat_dl_btn.pack(pady=10)

        # 创建 Tim 下载按钮
        tim_dl_btn = tk.Button(self,
                                text="Tim",
                                command=open_tim,
                                width=150)
        tim_dl_btn.pack()

        # 创建 QQ 下载按钮
        qq_dl_btn = tk.Button(self,
                                text="QQ",
                                command=open_qq,
                                width=150)
        qq_dl_btn.pack(pady=10)

        # 创建钉钉下载按钮
        dingtalk_dl_btn = tk.Button(self,
                                text="钉钉",
                                command=open_dingtalk,
                                width=150)
        dingtalk_dl_btn.pack()

        # 创建飞书下载按钮
        feishu_dl_btn = tk.Button(self,
                                text="飞书",
                                command=open_feishu,
                                width=150)
        feishu_dl_btn.pack(pady=10)

if __name__ == '__main__':
    chat_app = Chat()
    chat_app.mainloop()
