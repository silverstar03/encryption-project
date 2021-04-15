import subprocess
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class start(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        font1 = QtGui.QFont('나눔바른고딕', 40)
        font1.setBold(True)

        self.title = QLabel("암호화 프로그램", self)
        self.title.setFont(font1)
        self.title.move(230, 100)

        self.singleBtn = QPushButton('단일 치환', self)
        self.singleBtn.move(220, 260)
        self.singleBtn.resize(150, 50)
        self.singleBtn.clicked.connect(self.singleBtn_clicked)

        self.multipleBtn = QPushButton('다중 문자 치환', self)
        self.multipleBtn.move(420, 260)
        self.multipleBtn.resize(150, 50)
        self.multipleBtn.clicked.connect(self.multiple_clicked)

        self.setWindowTitle("암호화 프로그램")
        self.resize(800, 500)
        self.show()

    def singleBtn_clicked(self):
        subprocess.call("single.py", shell=True)

    def multiple_clicked(self):
        subprocess.call("multiple.py", shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = start()

    sys.exit(app.exec_())