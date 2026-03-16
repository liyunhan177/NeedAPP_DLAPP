# 从 page 目录导入所有页面模块
from .page import input, music, video, browser, media, chat
# 从 package 目录导入 WiFi 检测模块
from .package import wifi_detection
# 导入日志模块
from .package import logger

# 定义模块的公共接口，导出所有页面和工具模块
__all__ = ["input", "music", "video",
           "wifi_detection","browser", "media", "chat", "logger",
           "log_user_click", "log_user_action", "log_app_event",
           "log_error", "log_warning", "log_download_status", "log_performance"]

# 为各个页面类创建别名，方便外部调用
music_page = music.Music  # 音乐软件页面类
video_page = video.Video  # 视频软件页面类
input_page = input.Input  # 输入法页面类
browser_page = browser.Browser  # 浏览器页面类
media_page = media.Media  # 媒体播放器页面类
chat_page = chat.Chat  # 聊天软件页面类
wifi_det = wifi_detection.check_wifi_status  # WiFi 状态检测函数
get_logger = logger.get_default_logger  # 获取日志记录器
setup_logger = logger.setup_logger  # 配置日志记录器

# 便捷日志记录函数
log_user_click = logger.log_user_click  # 记录用户点击
log_user_action = logger.log_user_action  # 记录用户操作
log_app_event = logger.log_app_event  # 记录应用事件
log_error = logger.log_error  # 记录错误信息
log_warning = logger.log_warning  # 记录警告信息
log_download_status = logger.log_download_status  # 记录下载状态
log_performance = logger.log_performance  # 记录性能数据

__version__ = "0.0.1"  # 库版本号
__author__ = "liyunhan177"  # 作者名
__license__ = "liyunhan11111@163.com"  # 许可证信息（使用邮箱）
