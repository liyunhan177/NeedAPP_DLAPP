import pywifi
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

def get_wifi_info():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    if iface.status() == pywifi.const.IFACE_DISCONNECTED:
        print("WiFi未连接")
    else:
        print("WiFi已连接")

if __name__ == '__main__':
    get_wifi_info()