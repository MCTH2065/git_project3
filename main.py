import sqlite3
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget


class Prog(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('coffee')
        self.tb = QTableWidget(self)
        self.tb.resize(1070, 270)
        self.tb.setRowCount(4)
        self.tb.setColumnCount(7)
        self.tb.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.data = self.cur.execute("""SELECT * FROM data""").fetchall()
        self.tb.setHorizontalHeaderLabels(('ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                           'описание вкуса', 'цена', 'объем упаковки'))
        for i in range(4):
            self.tb.setRowHeight(i, 60)
            for j in range(7):
                self.tb.setColumnWidth(j, 150)
                print(self.data[i][j])
                self.tb.setItem(i, j, QTableWidgetItem(str(self.data[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Prog()
    ex.show()
    sys.exit(app.exec())
