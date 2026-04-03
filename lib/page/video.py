"""视频软件下载页面模块

提供视频类软件下载的图形用户界面
"""
import ttkbootstrap as tk
from ttkbootstrap.constants import *
import os
import lib
import webbrowser

class Video(tk.Window):
    """视频软件下载窗口类，继承自 ttkbootstrap.Window
    
    用于显示视频软件相关的下载选项和功能
    """
    def __init__(self):
        # 调用父类构造函数初始化窗口
        try:
            lib.log_user_action("打开窗口", "视频软件下载窗口初始化", "VideoPage")
            tk.Window.__init__(self,
                               themename="litera",
                               title="视频软件下载",
                               size=(300, 300),
                               minsize=(300, 300),  # 窗口的最小宽高
                               resizable=None)
            
            # 设置图标路径
            # 获取项目根目录（向上三层）
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)  # 设置窗口图标
                lib.log_app_event("资源加载", "图标加载成功", f"VideoPage: {icon_path}")
            else:
                lib.log_warning("资源缺失", "图标文件不存在", "VideoPage", icon_path)
                print(f"警告：图标文件不存在 {icon_path}")
            
            lib.log_app_event("窗口就绪", "视频软件下载窗口初始化完成", "VideoPage")
        except Exception as e:
            lib.log_error("窗口初始化异常", str(e), "VideoPage")
            raise

        # 定义各个视频播放器的下载链接打开函数
        def open_potplayer():
            """打开 PotPlayer 下载页面"""
            lib.log_user_action("点击下载", "打开 PotPlayer 下载页面", "VideoPage")
            webbrowser.open("https://potplayer.tv/?lang=zh_CN")

        def open_vlc():
            """打开 VLC 下载页面"""
            lib.log_user_action("点击下载", "打开 VLC 下载页面", "VideoPage")
            webbrowser.open("https://www.videolan.org/vlc/index.html")

        def open_kmplayer():
            """打开 KMPlayer 下载页面"""
            lib.log_user_action("点击下载", "打开 KMPlayer 下载页面", "VideoPage")
            webbrowser.open("https://www.kmplayer.com/home")

        def open_storm_player():
            """打开暴风影音下载页面"""
            lib.log_user_action("点击下载", "打开暴风影音下载页面", "VideoPage")
            webbrowser.open("http://www.baofeng.com/")

        # 创建 PotPlayer 下载按钮
        potplayer_dl_btn = tk.Button(self,
                                text="PotPlayer",
                                command=open_potplayer,
                                width=150)
        potplayer_dl_btn.pack(pady=10)

        # 创建 VLC 下载按钮
        vlc_dl_btn = tk.Button(self,
                                text="VLC",
                                command=open_vlc,
                                width=150)
        vlc_dl_btn.pack()

        # 创建 KMPlayer 下载按钮
        kmplayer_dl_btn = tk.Button(self,
                                text="KMPlayer",
                                command=open_kmplayer,
                                width=150)
        kmplayer_dl_btn.pack(pady=10)

        # 创建暴风影音下载按钮
        storm_player_dl_btn = tk.Button(self,
                                text="暴风影音",
                                command=open_storm_player,
                                width=150)
        storm_player_dl_btn.pack()

if __name__ == '__main__':
    video = Video()
    video.mainloop()
