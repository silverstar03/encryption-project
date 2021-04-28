import sys
from collections import OrderedDict

from PyQt5.QtWidgets import *
from PyQt5 import uic

main_ui = uic.loadUiType("start_UI.ui")[0]


class StartClass(QMainWindow, main_ui):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.singleBtn.clicked.connect(self.singleBtn_clicked)
        self.multipleBtn.clicked.connect(self.multiple_clicked)

    def singleBtn_clicked(self):
        self.main_ui = uic.loadUi("single_UI.ui", self)
        self.encrypt.clicked.connect(self.singlechangeTextFunction)
        self.decrypt.clicked.connect(self.singlereturnTextFunction)
        # self.backBtn.clicked.connect(self.singleBack_clicked)

    def singleBack_clicked(self):
        self.main_ui = uic.loadUi("start_UI.ui", self)
        # self.singleBtn_clicked.connect(self.singleBtn_clicked)

    def singlechangeTextFunction(self):
        self.a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.key = self.key_edit.text() #암호키 받아오기
        self.plain = self.plain_edit.text()  #평문 받아오기

        # 암호키 중복 제거 후 배열에 넣기
        self.result = "".join(OrderedDict.fromkeys(self.key))
        self.key_list = []
        for i in self.result:
            self.key_list.append(i)

        self.last = self.a.index(self.key_list[-1])  # 제일 마지막에 들어오는 알파벳 인덱스 가져오기

        # 암호판 만들기
        # 마지막 알파벳부터 z까지
        for i in range(self.last + 1, len(self.a)):
            if self.a[i] in self.key_list:
                continue
            else:
                self.key_list.append(self.a[i])

        # a부터 마지막 알파벳 전까지
        for i in range(self.last):
            if self.a[i] in self.key_list:
                continue
            else:
                self.key_list.append(self.a[i])

        print('알파벳 : ', self.a)
        print('암호판 : ', self.key_list)

        self.plain_list = []
        # 평문 배열에 넣기
        for i in self.plain:
            self.plain_list.append(i)

        print('평문 : ', self.plain_list)  # 평문

        self.cipher_list = []
        for i in self.plain_list:
            if i != ' ':
                num = self.a.index(i)
                self.cipher_list.append(self.key_list[num])
            else:
                self.cipher_list.append(i)

        print('암호문 : ', self.cipher_list)  # 암호문
        self.cipher_str = ''.join(self.cipher_list)
        self.cipher_edit.setText(self.cipher_str)

    def singlereturnTextFunction(self):
        #복호문
        self.decrypt_list = []
        for i in self.cipher_list:
            if i != ' ':
                num = self.key_list.index(i)
                self.decrypt_list.append(self.a[num])
            else:
                self.decrypt_list.append(i)
        print('복호문 : ', self.decrypt_list)

        self.decrypt_str = ''.join(self.decrypt_list)
        self.decrypt_edit.setText(self.decrypt_str)


    def multiple_clicked(self):
        self.main_ui = uic.loadUi("multiple_UI.ui", self)
        # self.backBtn.clicked.connect(self.multiBack_clicked)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = StartClass()
    main_window.show()

    app.exec_()