"""媒体播放器下载页面模块

提供媒体播放器软件下载的图形用户界面
"""
import ttkbootstrap as tk
from ttkbootstrap.constants import *
import os
import lib
import webbrowser

class Media(tk.Window):
    """媒体播放器下载窗口类，继承自 ttkbootstrap.Window
    
    用于显示媒体播放器软件相关的下载选项和功能
    """
    def __init__(self):
        # 调用父类构造函数初始化窗口
        try:
            lib.log_user_action("打开窗口", "媒体播放器下载窗口初始化", "MediaPage")
            tk.Window.__init__(self,
                               themename="litera",
                               title="媒体播放器下载",
                               size=(300, 300),
                               minsize=(300, 300),  # 窗口的最小宽高
                               resizable=None)
            
            # 设置图标路径
            # 获取项目根目录（向上三层）
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)  # 设置窗口图标
                lib.log_app_event("资源加载", "图标加载成功", f"MediaPage: {icon_path}")
            else:
                lib.log_warning("资源缺失", "图标文件不存在", "MediaPage", icon_path)
                print(f"警告：图标文件不存在 {icon_path}")
            
            lib.log_app_event("窗口就绪", "媒体播放器下载窗口初始化完成", "MediaPage")
        except Exception as e:
            lib.log_error("窗口初始化异常", str(e), "MediaPage")
            raise

        # 定义各个媒体平台的下载链接打开函数
        def open_bilibili():
            """打开哔哩哔哩下载页面"""
            lib.log_user_action("点击下载", "打开哔哩哔哩下载页面", "MediaPage")
            webbrowser.open("https://app.bilibili.com/")

        def open_douyin():
            """打开抖音下载页面"""
            lib.log_user_action("点击下载", "打开抖音下载页面", "MediaPage")
            webbrowser.open("https://www.douyin.com/")

        def open_qq_video():
            """打开腾讯视频下载页面"""
            lib.log_user_action("点击下载", "打开腾讯视频下载页面", "MediaPage")
            webbrowser.open("https://v.qq.com/download.html#windows")

        def open_iqiyi():
            """打开爱奇艺下载页面"""
            lib.log_user_action("点击下载", "打开爱奇艺下载页面", "MediaPage")
            webbrowser.open("https://www.iqiyi.com/appstore.html")

        def open_youku():
            """打开优酷下载页面"""
            lib.log_user_action("点击下载", "打开优酷下载页面", "MediaPage")
            webbrowser.open("https://www.youku.com/ku/product/index")

        # 创建哔哩哔哩下载按钮
        bilibili_dl_btn = tk.Button(self,
                                text="哔哩哔哩",
                                command=open_bilibili,
                                width=150)
        bilibili_dl_btn.pack(pady=10)

        # 创建抖音下载按钮
        douyin_dl_btn = tk.Button(self,
                                text="抖音",
                                command=open_douyin,
                                width=150)
        douyin_dl_btn.pack()

        # 创建腾讯视频下载按钮
        qq_video_dl_btn = tk.Button(self,
                                text="腾讯视频",
                                command=open_qq_video,
                                width=150)
        qq_video_dl_btn.pack(pady=10)

        # 创建爱奇艺下载按钮
        iqiyi_dl_btn = tk.Button(self,
                                text="爱奇艺",
                                command=open_iqiyi,
                                width=150)
        iqiyi_dl_btn.pack()

        # 创建优酷下载按钮
        youku_dl_btn = tk.Button(self,
                                text="优酷",
                                command=open_youku,
                                width=150)
        youku_dl_btn.pack(pady=10)

if __name__ == '__main__':
    media = Media()
    media.mainloop()
