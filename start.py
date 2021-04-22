import sys
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
        self.backBtn.clicked.connect(self.singleBack_clicked)

    def singleBack_clicked(self):
        self.main_ui = uic.loadUi("start_UI.ui", self)
        self.singleBtn_clicked.connect(self.singleBtn_clicked)

    def multiple_clicked(self):
        self.main_ui = uic.loadUi("multiple_UI.ui", self)
        self.backBtn.clicked.connect(self.multiBack_clicked)

    def multiBack_clicked(self):
        self.main_ui = uic.loadUi("start_UI.ui", self)
        self.multipleBtn.clicked.connect(self.multiple_clicked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = StartClass()
    main_window.show()

    app.exec_()