import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('App')
        self.btn_left.clicked.connect(self.left)  # 3 задание
        self.btn_right.clicked.connect(self.right)  # 3 задание
        self.btn_up.clicked.connect(self._up)  # 3 задание
        self.btn_down.clicked.connect(self._down)  # 3 задание
        self.button_up.clicked.connect(self.up)  # 2 задание
        self.button_down.clicked.connect(self.down)  # 2 задание


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
