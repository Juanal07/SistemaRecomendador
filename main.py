# import funciones as f
import os
import sys
from PyQt5 import QtWidgets, uic, QtMultimedia
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from funciones import prueba1

data = {'col1':['1','2','3','4'],
        'col2':['1','2','1','3'],
        'col3':['1','1','2','1']}

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()

        #Iniciamos la primera ventana
        uic.loadUi('Interface.ui',self)

        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.btnRecomendar.clicked.connect(self.prueba)

    def prueba(self):
        a = prueba1()
        print(a)
        self.textprueba.setText("La vida es como una caja de bombones")
        print("hello world")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())