import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget, QLineEdit, QPushButton
from PyQt5 import uic


# single_UI = uic.loadUiType('single_UI.ui')[0]


class single(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.singleUI()


    def singleUI(self):
        font1 = QtGui.QFont('나눔바른고딕', 10)
        font1.setBold(True)

        title = QLabel('단일 치환 암호화', self)
        title.move(290, 70)
        title.setFont(QtGui.QFont('나눔바른고딕', 25))

        keylbl = QLabel('암호키', self)
        keylbl.move(220, 170)

        key_edit = QLineEdit('', self)
        key_edit.resize(180, 25)
        key_edit.move(320, 160)

        self.plainbl = QLabel('평문', self)
        self.plainlbl.move(220, 220)

        self.plain_edit = QLineEdit('', self)
        self.plain_edit.resize(180, 25)
        self.plain_edit.move(320, 210)
        # 엔터 치면 발생하게 하는 메서드
        # self.plain_edit.returnPressed.connect(self.lineEditChanged)

        self.encrypt = QPushButton('암호문', self) #encrypt는 암호화라는 뜻
        self.encrypt.toggle()
        self.encrypt.resize(80, 25)
        self.encrypt.move(320, 260)
        self.encrypt.clicked.connect(self.changeTextFunction)

        self.decrypt = QPushButton('복호문', self)
        self.decrypt.toggle()
        self.decrypt.resize(80, 25)
        self.decrypt.move(420, 260)

        self.cipherlbl = QLabel('암호문', self)
        self.cipherlbl.move(220, 320)

        self.cipher_edit = QLineEdit('', self)
        self.cipher_edit.resize(180, 25)
        self.cipher_edit.move(320, 310)

        self.decryptlbl = QLabel('복호문', self)
        self.decryptlbl.move(220, 370)

        self.decrypt_edit = QLineEdit('', self)
        self.decrypt_edit.resize(180, 25)
        self.decrypt_edit.move(320, 360)

        self.resize(800, 500)
        self.setWindowTitle("단일 치환 암호화")
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def lineEditChanged(self):
    #     print(self.plain_edit.text())

    def changeTextFunction(self):
        # self.cipher_edit.setText(self.plain_edit.text())
        list = []
        for i in self.key_edit.text():
            list.append(i)

        for i in range(list):
            print(i)

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = single()
#     sys.exit(app.exec_())
