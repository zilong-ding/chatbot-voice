# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# def window():
#    app = QApplication(sys.argv)
#    w = QWidget()
#    b = QLabel(w)
#    b.setText("Hello World!")
#    w.setGeometry(100,100,200,50)
#    b.move(50,20)
#    w.setWindowTitle("PyQt5")
#    w.show()
#    sys.exit(app.exec_())
# if __name__ == '__main__':
#    window()


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        # self.resize(200, 50)
        self.setGeometry(1000,100,400,200)
        self.setWindowTitle("PyQt5")
        self.label = QLabel(self)
        self.label.setText("Hello World")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50, 20)


def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
