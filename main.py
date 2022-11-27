import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.import_db('coffee.sqlite')
        self.load_table()

    def import_db(self, db):
        table = sqlite3.connect(db)
        curcor = table.cursor()
        self.result = curcor.execute('''SELECT * FROM coffee''').fetchall()

    def load_table(self):
        self.table.setRowCount(len(self.result))
        self.table.setColumnCount(len(self.result[0]))
        self.table.setHorizontalHeaderLabels(['ID', 'название кофе', 'степень обжарки', 'молотый/в зёрнах', 'описание вкуса', 'цена', 'объём упаковки'])
        for i in range(len(self.result)):
            for j in range(len(self.result[i])):
                print(i, j, self.result[i][j])
                self.table.setItem(i, j, QTableWidgetItem(str(self.result[i][j])))
        self.table.setContentsMargins(0, 0, 0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())