# 从 page 目录导入所有页面模块
from .page import input, music, video, nowifi, browser, media, chat
# 从 package 目录导入 WiFi 检测模块
from .package import wifi_detection

# 定义模块的公共接口，导出所有页面和工具模块
__all__ = ["input", "music", "video",
           "wifi_detection","browser", "media", "chat"]

# 为各个页面类创建别名，方便外部调用
music_page = music.Music  # 音乐软件页面类
video_page = video.Video  # 视频软件页面类
input_page = input.Input  # 输入法页面类
browser_page = browser.Browser  # 浏览器页面类
media_page = media.Media  # 媒体播放器页面类
chat_page = chat.Chat  # 聊天软件页面类
wifi_det = wifi_detection.check_wifi_status  # WiFi 状态检测函数

__version__ = "0.0.1"  # 库版本号
__author__ = "liyunhan177"  # 作者名
__license__ = "liyunhan11111@163.com"  # 许可证信息（使用邮箱）
