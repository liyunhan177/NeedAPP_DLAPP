from .page import input, music, video, nowifi, browser, media, chat
from .package import wifi_detection

__all__ = ["input", "music", "video",
           "nowifi", "wifi_detection","browser", "media", "chat"]

music_page = music.Music
video_page = video.Video
input_page = input.Input
nowifi_page = nowifi
browser_page = browser.Browser
media_page = media.Media
chat_page = chat.Chat

__version__ = "0.0.1"
__author__ = "liyunhan177"
__license__ = "liyunhan11111@163.com"
