import pywifi

def get_wifi_info():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    profile = iface.scan_results()[0]
    ssid = profile.ssid
    signal = profile.signal

    if iface.status() == pywifi.const.IFACE_DISCONNECTED:
        print("WiFi未连接")
        wifi_state = "未连接"

    else:
        print("WiFi已连接")
        wifi_state = "已连接"
        print(f"SSID: {ssid}")
        print(f"信号强度: {signal} dBm")


if __name__ == '__main__':
    get_wifi_info()