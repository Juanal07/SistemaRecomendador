from interface_ui import *
import os
import sys
from PyQt5 import QtWidgets, uic, QtMultimedia
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from funciones import *


data = [['1','2'],
        ['3','4'],
        ['1','2'],
        ['1','3'],
        ['1','3'],
        ['1','3'],
        ['1','3']]

Usuarios = ['1','2','3','4','5','6','7','8']


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        insertarComboBox(self.boxUsuarioPrediccion, Usuarios)
        self.btnRecomendar.clicked.connect(lambda: insertarTabla(self.tableWidget, data, int(self.textRanking.text())))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()