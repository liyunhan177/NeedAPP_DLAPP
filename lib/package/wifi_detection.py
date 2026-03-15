"""WiFi 和网络检测工具模块

提供 WiFi 和以太网连接状态的检测功能
使用 pywifi 库检测 WiFi 状态，使用 socket 检测以太网状态
"""
import pywifi
import socket

def check_wifi_status():
    """
    检测 WiFi 连接状态
    Returns:
        tuple: (是否连接，状态消息，连接信息字典)
            - 是否连接：bool 值，True 表示已连接，False 表示未连接
            - 状态消息：str，描述当前 WiFi 状态
            - 连接信息字典：包含 SSID 和信号强度，如果未连接则为 None
    """
    try:
        # 创建 PyWiFi 对象
        wifi = pywifi.PyWiFi()
        # 获取第一个网络接口
        iface = wifi.interfaces()[0]
        
        if iface.status() == pywifi.const.IFACE_DISCONNECTED:
            # WiFi 未连接
            return False, "WiFi 未连接", None
        else:
            # WiFi 已连接，获取网络信息
            profile = iface.scan_results()[0]  # 获取扫描结果中的第一个网络
            ssid = profile.ssid  # WiFi 名称
            signal = profile.signal  # WiFi 信号强度
            return True, f"WiFi 已连接：{ssid}", {"ssid": ssid, "signal": signal}
    except Exception as e:
        # 检测出错时返回错误信息
        return False, f"WiFi 检测出错：{str(e)}", None

def check_ethernet_status():
    """
    检测以太网连接状态
    通过尝试连接到公共 DNS 服务器（8.8.8.8）来判断网络连通性
    Returns:
        tuple: (是否连接，状态消息，连接信息字典)
            - 是否连接：bool 值，True 表示已连接，False 表示未连接
            - 状态消息：str，描述当前以太网状态
            - 连接信息字典：包含本地 IP 地址，如果未连接则为 None
    """
    try:
        # 方法 1: 使用 socket 检测网络连通性
        host = "8.8.8.8"  # Google DNS 服务器
        port = 53  # DNS 端口
        socket.setdefaulttimeout(2)  # 设置超时时间为 2 秒
        
        # 创建 TCP socket 并尝试连接
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))  # 返回 0 表示连接成功
        sock.close()
        
        if result == 0:
            # 网络连接成功，获取本地 IP 地址
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return True, f"以太网已连接 (IP: {local_ip})", {"ip": local_ip}
        else:
            # 网络连接失败
            return False, "以太网未连接", None
    except Exception as e:
        # 检测出错时返回错误信息
        return False, f"以太网检测出错：{str(e)}", None

def get_network_info():
    """
    获取网络连接信息（WiFi 和以太网）
    综合检测 WiFi 和以太网两种网络连接方式
    Returns:
        dict: 包含网络连接信息的字典，结构如下：
            {
                "wifi": {
                    "connected": bool,  # 是否连接
                    "message": str,  # 状态消息
                    "info": dict or None  # 详细信息（SSID、信号强度）
                },
                "ethernet": {
                    "connected": bool,  # 是否连接
                    "message": str,  # 状态消息
                    "info": dict or None  # 详细信息（IP 地址）
                },
                "any_connected": bool  # 是否有任何一种网络已连接
            }
    """
    # 分别检测 WiFi 和以太网状态
    wifi_connected, wifi_msg, wifi_info = check_wifi_status()
    ethernet_connected, ethernet_msg, ethernet_info = check_ethernet_status()
    
    # 构建结果字典
    result = {
        "wifi": {
            "connected": wifi_connected,
            "message": wifi_msg,
            "info": wifi_info
        },
        "ethernet": {
            "connected": ethernet_connected,
            "message": ethernet_msg,
            "info": ethernet_info
        },
        "any_connected": wifi_connected or ethernet_connected  # 任一网络已连接则为 True
    }
    
    return result

if __name__ == '__main__':
    result = get_network_info()
    print(f"WiFi 状态：{result['wifi']['message']}")
    print(f"以太网状态：{result['ethernet']['message']}")
    print(f"总体网络状态：{'已连接' if result['any_connected'] else '未连接'}")