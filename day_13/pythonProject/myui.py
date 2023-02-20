import os.path
import sys, os

from datetime import datetime
from PySide2 import QtWidgets, QtCore, QtUiTools


class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.load()
        self.setUi()
        self.ui.show()

        # load ui
    def load(self):
        # load ui
        # def load_ui():
        ui_path = os.path.expanduser('~/myapp.ui')
        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        # 버튼 클릭 시 연결되는 것들
    def setUi(self):

        self.ui.pushButton_zero.clicked.connect(self.button_0)
        self.ui.pushButton_1.clicked.connect(self.button_1)
        self.ui.pushButton_2.clicked.connect(self.button_2)
        self.ui.pushButton_3.clicked.connect(self.button_3)
        self.ui.pushButton_4.clicked.connect(self.button_4)
        self.ui.pushButton_5.clicked.connect(self.button_5)
        self.ui.pushButton_6.clicked.connect(self.button_6)
        self.ui.pushButton_7.clicked.connect(self.button_7)
        self.ui.pushButton_8.clicked.connect(self.button_8)
        self.ui.pushButton_9.clicked.connect(self.button_9)
        self.ui.pushButton_sum.clicked.connect(self.plus)
        self.ui.enter.clicked.connect(self.button_enter)
        self.ui.bt_del.clicked.connect(self.del_num)

        self.ui.enter.clicked.connect(self.button_enter)
        self.ui.enter.clicked.connect(self.button_enter)

        # self.ui.date.clicked.connect(self.today_date())

    def button_0(self):
        self.ui.input.setText("0")

    def button_1(self):
        self.ui.input.setText("1")

    def button_2(self):
        self.ui.input.setText("2")

    def button_3(self):
        self.ui.input.setText("3")

    def button_4(self):
        self.ui.input.setText("4")

    def button_5(self):
        self.ui.input.setText("5")

    def button_6(self):
        self.ui.input.setText("6")

    def button_7(self):
        self.ui.input.setText("7")

    def button_8(self):
        self.ui.input.setText("8")

    def button_9(self):
        self.ui.input.setText("9")

    # def button_sum(self):
    #     self.ui.input.setText("+")

    def button_enter(self):
        self.ui.input.setText("=")

    def number(self, num):
        input_num = self.lnput.text() #input 값 iunput num 에 저장
        self.ui.input.setText(input_num + num) #기존값 + 새로운 입력값

    #del
    def del_num(self):
        input_num = self.ui.input.text() # input 가져옴
        self.ui.input.setText(input_num[:-1]) # input 에 있는 인덱스 0부터 마지막 인덱스 전 까지가져옴


    #사칙연산 여러 번 눌리지 않도록 조건, input 제일끝에 사칙연산 있는지 확인후 있으면 지우고 새로 추가 없으면 그냥 추가


    def plus(self):
        input_num = self.ui.input.text()
        if ((input_num[-1] == "+") | (input_num[-1] == "-") | (input_num[-1] == "*") | (input_num[-1] == "/")):
            self.ui.input.setText(input_num[:-1])
        self.number("+")

    #eval(계산식) eval 함수로 구함.
    def result(self):
        input_num = self.ui.input.text()
        self.number("=")
        try:
            ans = eval(input_num)
            self.ui.result.setText(str(ans))
        except Exception as e:
            print(e)


    def input(self):
        input_num = self.ui.input.text()
        self.number("enter")
        try:
            ans = eval(input_num)
            self.ui.input.setText(str(ans))

        except Exception as e:
            print(e)




    # def reset_clicked(self):  # tab1 text clear
    #     print("close")
    #     self.ui.close()

    # def today_date(self):
    #     date_today = datetime.today()
    #     self.ui.inputMethodHints(date_today())

    # def action_sum:

    # def action_sub:
    # def action_div:
    # def action_mult:
    # def action_reset:
    # def action_enter


def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication()
    myapp = MyApp()
    # myapp.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
