import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget, QLineEdit, QPushButton

from start import start

class single(QWidget):

    def __init__(self):
        super().__init__()
        self.multipleUI()

    def multipleUI(self):
        font1 = QtGui.QFont('나눔바른고딕', 10)
        font1.setBold(True)

        self.title = QLabel('다중 문자 치환 암호화', self)
        self.title.move(290, 70)
        self.title.setFont(QtGui.QFont('나눔바른고딕', 25))

        self.keylbl = QLabel('암호키', self)
        self.keylbl.move(220, 170)

        self.key_edit = QLineEdit('', self)
        self.key_edit.resize(180, 25)
        self.key_edit.move(320, 160)

        self.plainlbl = QLabel('평문', self)
        self.plainlbl.move(220, 220)

        self.plain_edit = QLineEdit('', self)
        self.plain_edit.resize(180, 25)
        self.plain_edit.move(320, 210)

        self.encrypt = QPushButton('암호문', self) #encrypt는 암호화라는 뜻
        self.encrypt.toggle()
        self.encrypt.resize(80, 25)
        self.encrypt.move(320, 260)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = single()
    sys.exit(app.exec_())