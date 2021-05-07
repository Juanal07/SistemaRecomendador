from PyQt5.QtWidgets import QComboBox, QTableWidget, QTableWidgetItem

def insertarComboBox(combobox, usuarios):
    combobox.addItems(usuarios)

def insertarTabla(tabla, datos, filas):
    tabla.setRowCount(filas)
    for fila in range(0, len(datos)):
        for columna in range(0, len(datos[0])):
            tabla.setItem(fila, columna, QTableWidgetItem(datos[fila][columna]))
