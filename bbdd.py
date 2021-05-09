import csv
import sqlite3

def insertarDatos():
    #Conexion con el archivo de base de datos
    try:
        con = sqlite3.connect('bbdd/movielens.db')
    except:
        print("No conectado")
    cur = con.cursor()

    cont = 0 #evitar linea 1 del csv
    #comprobamos si la tabla ya tiene datos insertados
    conteo = cur.execute('SELECT * FROM movie')
    # print(len(conteo.fetchall()))
    if len(conteo.fetchall())<=0:
        #se procede a la insercion de los datos tras leer el csv
        with open('ml-latest-small\movies.csv', newline='', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                print(', '.join(row)) #devolvemos la linea leida
                if cont == 0: #para evitar la primera línea del csv
                    cont += 1
                else: #parseamos la columna e insertamos
                    movieId = int(row[0])
                    title = row[1]
                    genres = row[2]

                    cur.execute("INSERT INTO movie VALUES(?,?,?)", (movieId,title,genres))
                
        con.commit() #reflejamos los datos en el archivo .db
    
    #comprobamos si la tabla ya tiene datos insertados
    conteo = cur.execute('SELECT * FROM rating')
    # print(len(conteo.fetchall()))
    if len(conteo.fetchall())<=0:
        cont = 0 #evitar linea 1 del csv
        #se procede a la insercion de los datos tras leer el csv
        with open('ml-latest-small\/ratings.csv', newline='', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                print(', '.join(row)) #devolvemos la linea leida
                if cont == 0: #para evitar la primera línea del csv
                    cont += 1
                else: #parseamos la columna e insertamos
                    userId = int(row[0])
                    movieId = int(row[1])
                    rating = float(row[2])
                    timestamp = int(row[3])

                    cur.execute("INSERT INTO rating(userId,movieId,rating,timestamp) VALUES(?,?,?,?)", (userId,movieId,rating,timestamp))
        con.commit() #reflejamos los datos en el archivo .db

    con.close() #cerramos la conexion con la bbdd

def votadas(uid):
    try:
        con = sqlite3.connect('bbdd/movielens.db')
    except:
        print("No conectado")
    cur = con.cursor()
    conteo = cur.execute('SELECT movieId FROM rating WHERE rating.userId = ?',(uid,))
    lista = []
    for (movieId) in cur:
        lista.append(movieId[0])
        # print(movieId)
    con.close()
    return lista

def noVotadas(uid):
    try:
        con = sqlite3.connect('bbdd/movielens.db')
    except:
        print("No conectado")
    cur = con.cursor()
    cur.execute('select movieId from rating WHERE rating.userId <> ? EXCEPT SELECT movieId FROM rating WHERE rating.userId = ?', (uid,uid))
    lista = []
    for (movieId) in cur:
        lista.append(movieId[0])
        # print(movieId)
    con.close()
    return lista

def sameEnery(mid1, mid2):
    try:
        con = sqlite3.connect('bbdd/movielens.db')
    except:
        print("No conectado")
    cur = con.cursor()
    cur.execute('SELECT rating FROM rating WHERE movieId=? AND userId IN (SELECT userId FROM rating WHERE movieId=?)', (mid1,mid2))
    lista = []
    for (item) in cur:
        lista.append(item[0])
        # print(movieId)
    con.close()
    return lista
