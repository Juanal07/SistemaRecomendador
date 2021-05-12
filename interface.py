from interface_ui import *
import os
import sys
from PyQt5 import QtWidgets, uic, QtMultimedia
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from funciones import *
from query import *


data = [['1','2'],
        ['3','4'],
        ['1','2'],
        ['1','3'],
        ['1','3'],
        ['1','3'],
        ['1','3']]

usuarios = getUsers()
peliculas = getMovies()




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        insertarComboBox(self.boxUsuariosRanking, usuarios)
        insertarComboBox(self.boxUsuarioPrediccion, usuarios)
        insertarComboBoxDupla(self.boxPliculas, peliculas)
        # self.btnRecomendar.clicked.connect(lambda: insertarTabla(self.tableWidget, data, int(self.textRanking.text())))
        self.btnRecomendar.clicked.connect(lambda: insertarRecomendaciones(self.tableWidget, self.boxUsuariosRanking.currentText(), float(self.textSimilitud.text())))
        self.btnPredecir.clicked.connect(lambda: mostrarPrediccion(self.textPrediccion, int(self.boxUsuarioPrediccion.currentText()), int(self.boxPliculas.currentText())))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()