from .page import input, music, video, nowifi, browser, media
from .package import wifi_detection

__all__ = ["input", "music", "video",
           "nowifi", "wifi_detection","browser", "media"]

music_page = music.Music
video_page = video.Video
input_page = input.Input
nowifi_page = nowifi
browser_page = browser.Browser
media_page = media.Media

__version__ = "0.0.1"
__author__ = "liyunhan177"
__license__ = "liyunhan11111@163.com"
