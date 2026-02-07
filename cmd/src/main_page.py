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

        if app_num == 0:
            exit()

if __name__ == '__main__':
    Use_cmd_ver()
