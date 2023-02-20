import os.path
import sys, os

from datetime import datetime
from PySide2 import QtWidgets, QtCore, QtUiTools


class MyApp(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyApp).__init__()
        # load ui
        ui_path = os.path.expanduser('~/main.ui')
        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        self.ui.show()
        self.setup_ui()

    def setup_ui(self):
        self.ui.action_Quit.triggered.connect(app.quit)
        self.ui.pushButton_add.clicked.connect(self.add)
        self.ui.pushButton_sub.clicked.connect(self.sub)
        self.ui.pushButton_mul.clicked.connect(self.mul)
        self.ui.pushButton_div.clicked.connect(self.div)
        self.ui.pushButton_pow.clicked.connect(self.pow)

   def add(self):
        x = float(self.ui.lineEdit_x.text())
        y = float(self.ui.lineEdit_y.text())
        z = func.add(x, y)
        self.ui.lineEdit_z.setText(str(z))

    def sub(self):
        x = float(self.ui.lineEdit_x.text())
        y = float(self.ui.lineEdit_y.text())
        z = func.sub(x, y)
        self.ui.lineEdit_z.setText(str(z))

    def mul(self):
        x = float(self.ui.lineEdit_x.text())
        y = float(self.ui.lineEdit_y.text())
        z = func.mul(x, y)
        self.ui.lineEdit_z.setText(str(z))

    def div(self):
        x = float(self.ui.lineEdit_x.text())
        y = float(self.ui.lineEdit_y.text())
        z = func.div(x, y)
        self.ui.lineEdit_z.setText(str(z))

    def pow(self):
        x = float(self.ui.lineEdit_x.text())
        y = float(self.ui.lineEdit_y.text())
        z = func.pow(x, y)
        self.ui.lineEdit_z.setText(str(z))


class func:
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    def pow(x, y):
        return x ** y

    # def number(self, num):
    #     input_num = self.lnput.text()  # input 값 저장
    #     self.input.setTexT(input_num + num)  # 기존값 + 입력값

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


# # def main():
#     QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
#
#     app = QtWidgets.QApplication()
#     sw = MyApp()
#
#     sys.exit(app.exec_())


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

    app = QtWidgets.QApplication(sys.argv)
    main = MyApp()

    sys.exit(app.exec_())

