from PySide2.QtWidgets import QApplication, QDialog
import sys
import resources

loader = QtUiTools.QUiLoader()
class MainWindow(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        self.ui = loader.load(':/ui/main.ui', None)
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


class func():

    def add(x, y):
        return (x + y)

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    def pow(x, y):
        return x ** y


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icon/counter.ico'))
    main = MainWindow()
    sys.exit(app.exec_())