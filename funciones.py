from PyQt5.QtWidgets import QComboBox, QTableWidget, QTableWidgetItem
import algoritmo
import query

def insertarComboBox(combobox, usuarios):
    combobox.addItems(usuarios)

def insertarComboBoxDupla(combobox, user):
    peliculas=query.noVotadasCombo(user)
    combobox.addItems(peliculas)

def insertarTabla(tabla, datos, filas):
    tabla.setRowCount(filas)
    for fila in range(0, len(datos)):
        for columna in range(0, len(datos[0])):
            tabla.setItem(fila, columna, QTableWidgetItem(datos[fila][columna]))

def insertarRecomendaciones(tabla, usuario, umbral):
    noValoradas = query.noVotadas(usuario)
    # tabla.setRowCount(noValoradas)
    recomendaciones = algoritmo.recomendacionesUmbral(usuario, umbral)
    for fila in range(0, len(noValoradas)):
        for columna in range(0, 1):
            tabla.setItem(fila, columna, QTableWidgetItem(recomendaciones[fila][columna]))

def mostrarPrediccion(prediccion, usuario, pelicula):
    prediccion.setText("")
    prediccion.setText(str(algoritmo.prediccion(usuario, pelicula, )))
