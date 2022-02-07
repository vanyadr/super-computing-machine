import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from main_ui import Ui_MainWindow

import script


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
        self.search_btn.clicked.connect(self.search)
        self.lst = ['схема', 'спутник', 'гибрид']
        self.comboBox.addItems(self.lst)
        self.comboBox.activated[str].connect(self.combo_checker)

    def combo_checker(self):
        curr = self.comboBox.currentText()
        d = {'схема': 'map', 'спутник': 'sat', 'гибрид': 'sat, skl'}
        a = self.search_lineEdit.text()
        ll, spn = script.get_ll_span(a)
        ll_spn = f"ll={ll}&spn={spn[0]},{spn[1]}"
        script.create_map(ll_spn, d[curr], add_params=f"pt={ll}")

    def search(self):
        a = self.search_lineEdit.text()
        ll, spn = script.get_ll_span(a)
        ll_spn = f"ll={ll}&spn={spn[0]},{spn[1]}"
        script.create_map(ll_spn, "map", add_params=f"pt={ll}")
        pixmap = QPixmap('map.png')
        self.map.setPixmap(pixmap)

    def left(self):
        pass

    def right(self):
        pass

    def _up(self):
        pass

    def _down(self):
        pass

    def down(self):
        pass

    def up(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
