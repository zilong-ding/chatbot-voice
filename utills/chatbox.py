import os.path
import typing

from PyQt5.QtWidgets import QWidget

from utills.all import *

class ChatBox(QTextEdit):
    # def __init__(self):
    #     super().__init__()
    #     self.setStyleSheet("background-color: rgb(255, 255, 255);")
    #     self.setObjectName("textEdit")
    def __init__(self, parent: typing.Optional[QWidget] = ...):
        super().__init__(parent)
        self.file_path = 'history/history.txt'

    def save(self):
        # 获取文本编辑框中的内容
        text = self.toPlainText()

        # 弹出对话框，让用户选择保存文件的路径
        # file_path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")
        if not os.path.exists('history'):
            os.mkdir('history')
        # 如果用户选择了文件路径，则将文本写入文件中
        self.file_path = 'history/history.txt'
        if self.file_path:
            with open(self.file_path, "a") as f:
                f.write(text + '\n')

    def load(self):
        # 弹出对话框，让用户选择要加载的文件
        # file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text files (*.txt)")

        if not os.path.exists('history'):
            os.mkdir('history')

        # 如果用户选择了文件，则将文件内容读取到文本编辑框中
        if self.file_path:
            with open(self.file_path, "r") as f:
                text = f.read()
                self.setPlainText(text)