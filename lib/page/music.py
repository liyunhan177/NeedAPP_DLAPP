"""音乐软件下载页面模块

提供音乐类软件下载的图形用户界面
"""
import ttkbootstrap as tk
from ttkbootstrap.constants import *
import os
import lib
import webbrowser

class Music(tk.Window):
    """音乐软件下载窗口类，继承自 ttkbootstrap.Window
    
    用于显示音乐软件相关的下载选项和功能
    """
    def __init__(self):
        # 调用父类构造函数初始化窗口
        try:
            lib.log_user_action("打开窗口", "音乐软件下载窗口初始化", "MusicPage")
            tk.Window.__init__(self,
                               themename="litera",
                               title="音乐软件下载",
                               size=(300, 300),
                               minsize=(300, 300),  # 窗口的最小宽高
                               resizable=None)
            
            # 设置图标路径
            # 获取项目根目录（向上三层）
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            icon_path = os.path.join(project_root, "res", "IMG", "logo.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)  # 设置窗口图标
                lib.log_app_event("资源加载", "图标加载成功", f"MusicPage: {icon_path}")
            else:
                lib.log_warning("资源缺失", "图标文件不存在", "MusicPage", icon_path)
                print(f"警告：图标文件不存在 {icon_path}")
            
            lib.log_app_event("窗口就绪", "音乐软件下载窗口初始化完成", "MusicPage")
        except Exception as e:
            lib.log_error("窗口初始化异常", str(e), "MusicPage")
            raise

        # 定义各个音乐软件的下载链接打开函数
        def open_qq_music():
            """打开 QQ 音乐下载页面"""
            lib.log_user_action("点击下载", "打开 QQ 音乐下载页面", "MusicPage")
            webbrowser.open("https://y.qq.com/download/index.html")

        def open_netease_cloud():
            """打开网易云音乐下载页面"""
            lib.log_user_action("点击下载", "打开网易云音乐下载页面", "MusicPage")
            webbrowser.open("https://music.163.com/#/download")

        def open_kugou():
            """打开酷狗音乐下载页面"""
            lib.log_user_action("点击下载", "打开酷狗音乐下载页面", "MusicPage")
            webbrowser.open("https://download.kugou.com/")

        def open_kuwo():
            """打开酷我音乐下载页面"""
            lib.log_user_action("点击下载", "打开酷我音乐下载页面", "MusicPage")
            webbrowser.open("http://www.kuwo.cn/down/index.html")

        def open_migu_music():
            """打开咪咕音乐下载页面"""
            lib.log_user_action("点击下载", "打开咪咕音乐下载页面", "MusicPage")
            webbrowser.open("https://music.migu.cn/v3/static/client/index.html")

        def open_qianqian():
            """打开千千音乐下载页面"""
            lib.log_user_action("点击下载", "打开千千音乐下载页面", "MusicPage")
            webbrowser.open("https://music.taihe.com/download")

        # 创建 QQ 音乐下载按钮
        qq_music_dl_btn = tk.Button(self,
                                text="QQ 音乐",
                                command=open_qq_music,
                                width=150)
        qq_music_dl_btn.pack(pady=10)

        # 创建网易云音乐下载按钮
        netease_cloud_dl_btn = tk.Button(self,
                                text="网易云音乐",
                                command=open_netease_cloud,
                                width=150)
        netease_cloud_dl_btn.pack()

        # 创建酷狗音乐下载按钮
        kugou_dl_btn = tk.Button(self,
                                text="酷狗音乐",
                                command=open_kugou,
                                width=150)
        kugou_dl_btn.pack(pady=10)

        # 创建酷我音乐下载按钮
        kuwo_dl_btn = tk.Button(self,
                                text="酷我音乐",
                                command=open_kuwo,
                                width=150)
        kuwo_dl_btn.pack()

        # 创建咪咕音乐下载按钮
        migu_music_dl_btn = tk.Button(self,
                                text="咪咕音乐",
                                command=open_migu_music,
                                width=150)
        migu_music_dl_btn.pack(pady=10)

        # 创建千千音乐下载按钮
        qianqian_dl_btn = tk.Button(self,
                                text="千千音乐",
                                command=open_qianqian,
                                width=150)
        qianqian_dl_btn.pack()

if __name__ == '__main__':
    music = Music()
    music.mainloop()
