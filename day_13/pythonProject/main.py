import sys

from PySide2 import QtWidgets, QtCore


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # super 기존의 부모가 가지고있는것들(인자)들 을 가져온다. 오버라이드하기위해
        self.setWindowTitle("my app")
        self.setFixedSize(QtCore.QSize(500, 500))
        # self.setBaseSize(Qtcore.QSize(300, 300))
        self.my_button = QtWidgets.QPushButton("This is button_close", self) # , self :qt의 문법이다
        self.my_button.clicked.connect(self.my_button_clicked)

    def my_button_clicked(self):
        print("close")
        self.close()


def main():
    app = QtWidgets.QApplication()
    myapp = MyApp()
    myapp.show()  # show 는 창을 띄워주는 역할
    sys.exit(app.exec_())  # 닫아지면 끝내라?!


if __name__ == '__main__':
    main()
