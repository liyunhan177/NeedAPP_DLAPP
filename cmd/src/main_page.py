import time
import os
import json

class Use_cmd_ver():
    def __init__(self):
        os.system("CLS")

        with open('../../data/data.json', encoding='utf-8') as f:
            data = json.loads(f.read())
            print("0.退出")
            for key, software_info in data.items():
                print(f"{software_info['num']} {software_info['title']}")

        app_num = input("请输入需要下载的应用编号：")

        # 验证输入是否为有效数字
        try:
            app_num = int(app_num)
        except ValueError:
            print("错误：请输入有效的数字！")
            time.sleep(2)
            return

        # 处理退出选项
        if app_num == 0:
            print("正在退出程序...")
            exit()

        # 查找对应的应用信息
        selected_software = None
        for key, software_info in data.items():
            if software_info['num'] == app_num:
                selected_software = software_info
                break

        # 检查是否找到对应应用
        if selected_software is None:
            print("错误：未找到编号为 {} 的应用！".format(app_num))
            print("请检查输入的编号是否正确。")
            time.sleep(2)
            return

        # 显示应用信息并询问是否下载
        print("{}的官网是 {}".format(selected_software['title'], selected_software['url']))
        dlyn = input("是否下载?(y/n)")

        if dlyn.lower() == "y":
            print("正在打开下载页面...")
            os.system("start " + selected_software['url'])
            time.sleep(3)
            print("页面已打开，请在浏览器中完成下载。")
        else:
            print("已取消下载。")

if __name__ == '__main__':
    Use_cmd_ver()
