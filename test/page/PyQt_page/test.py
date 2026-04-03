import sys  # 系统模块，用于控制程序退出
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QFileDialog, QTextEdit)

# 创建一个主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法

        self.setWindowTitle("文件对话框示例")  # 设置窗口标题

        # 创建一个按钮
        self.button = QPushButton("打开文件", self)
        self.button.clicked.connect(self.open_file)  # 连接按钮点击事件

        # 创建一个文本编辑框，用于显示文件内容
        self.text_edit = QTextEdit(self)

        # 设置窗口布局
        self.setCentralWidget(self.button)  # 初始显示按钮

    # 打开文件的函数
    def open_file(self):
        # 弹出文件对话框，让用户选择文件
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "文本文件 (*.txt);;所有文件 (*)")

        # 检查用户是否选择了文件
        if file_name:
            # 打开文件并读取内容
            with open(file_name, 'r', encoding='utf-8') as f:
                file_content = f.read()  # 读取文件内容

            # 将文件内容显示在文本编辑框中
            self.text_edit.setText(file_content)
            self.setCentralWidget(self.text_edit)  # 切换显示文本编辑框

# 创建应用程序对象
app = QApplication(sys.argv)

# 创建主窗口对象
window = MainWindow()
window.show()

# 进入应用程序事件循环
sys.exit(app.exec_())
