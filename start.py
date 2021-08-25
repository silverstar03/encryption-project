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
        self.encryptBtn.clicked.connect(self.multiplechangeTextFunction)
        self.decryptBtn.clicked.connect(self.multiplereturnTextFunction)

    def multiplechangeTextFunction(self):

        self.a2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.key2 = self.key_edit2.text() #암호키 받아오기
        self.plain2 = self.plain_edit2.text()  #평문 받아오기

        # 암호키 중복 제거 후 배열에 넣기
        self.result2 = "".join(OrderedDict.fromkeys(self.key2))

        self.key_list2 = []
        for i in self.result2:
            self.key_list2.append(i)

        print(self.key_list2)

        # z입력하면 q로 바꾸어 처리하기
        for i in range(len(self.key_list2)):
            if self.key_list2[i] == 'z':
                self.key_list2[i] = 'q'

        print(self.key_list2)

        # 암호판 만들기
        for i in range(len(self.a2)):
            if self.a2[i] in self.key_list2:
                continue
            else:
                self.key_list2.append(self.a2[i])
        print(self.a2)
        print(self.key_list2)  # 암호판

        # 2차원 배열 암호판 만들기
        self.list_2d = [[0 for col in range(5)] for row in range(5)]
        self.cnt = 0
        for i in range(len(self.list_2d)):
            for j in range(len(self.list_2d[i])):
                self.list_2d[i][j] = self.key_list2[self.cnt]
                self.cnt += 1

        print(self.list_2d)  # 2차원 배열 암호판


        # 평문 공백 제거
        self.plain3 = self.plain2.replace(" ", "")
        print(self.plain3)

        # x가 필요한 위치에 x 넣기
        self.x_add_list = []
        flag = 1

        self.x_add_list.append(self.plain3[0])
        for i in range(1, len(self.plain3)):
            if self.plain3[i - 1] != self.plain3[i]:
                self.x_add_list.append(self.plain3[i])
            elif self.plain3[i - 1] == self.plain3[i] and i % 2 == flag:
                self.x_add_list.append('x')
                self.x_add_list.append(self.plain3[i])
                flag = (1 + flag) % 2
            else:
                self.x_add_list.append(self.plain3[i])
        if len(self.x_add_list) % 2 == 1:
            self.x_add_list.append('x')

        print(self.x_add_list)

        self.x_add_str = ''.join(self.x_add_list)
        print(self.x_add_str)

        # 문자열 두칸씩 나누기
        self.list4 = []
        for i in range(0, len(self.x_add_str), 2):
            self.list4.append(self.x_add_str[i:i + 2])
        self.x_add_str2 = " ".join(self.list4)
        print(self.x_add_str2)

        #암호문 만들기

        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.encArr = []
        self.encResult = ""

        for i in range(len(self.list4)):
            temp = [0, 0]

            for j in range(len(self.list_2d)):
                for k in range(len(self.list_2d[j])):
                    if self.list_2d[j][k] == self.list4[i][0]:
                        self.x1 = j
                        self.y1 = k
                    if self.list_2d[j][k] == self.list4[i][1]:
                        self.x2 = j
                        self.y2 = k

            # 행이 같은 경우
            if self.x1 == self.x2:
                temp[0] = self.list_2d[self.x1][(self.y1 + 1) % 5]
                temp[1] = self.list_2d[self.x2][(self.y2 + 1) % 5]
            # 열이 같은 경우
            elif self.y1 == self.y2:
                temp[0] = self.list_2d[(self.x1 + 1) % 5][self.y1]
                temp[1] = self.list_2d[(self.x1 + 1) % 5][self.y2]
            # 행과 열이 모두 다른 경우
            else:
                temp[0] = self.list_2d[self.x2][self.y1]
                temp[1] = self.list_2d[self.x1][self.y2]

            self.encArr.append(temp)

        for i in range(len(self.encArr)):
            self.encResult += self.encArr[i][0] + self.encArr[i][1] + " "
        print(self.encResult)

        self.multiple_cipher_edit.setText(self.x_add_str2)
        self.cipher_edit.setText(self.encResult)

    def multiplereturnTextFunction(self):
        self.decrypt_edit.setText(self.plain2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = StartClass()
    main_window.show()

    app.exec_()