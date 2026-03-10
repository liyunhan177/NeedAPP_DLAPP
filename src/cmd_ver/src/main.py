import time
import os

__version__ = "0.0.1"

class Cmd_ver():
    def __init__(self):
        os.system("CLS")
        print("""
        ------------------
        |  欢迎使用该软件   |
        |  版本: {}    |
        | 作者: liyunhan  |
        ------------------
        """.format(__version__))

        time.sleep(0.7)
        start = input("按回车键继续...")

        if __name__ == '__main__':
            if start == "":
                os.system("CLS")
                os.system("python main_page.py")

        if __name__ != '__main__':
            if start == "":
                os.system("CLS")
                os.system("python src/cmd_ver/src/main_page.py")

if __name__ == '__main__':
    Cmd_ver()
