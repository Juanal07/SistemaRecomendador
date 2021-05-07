from interface_ui import *
import os
import sys
from PyQt5 import QtWidgets, uic, QtMultimedia
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()