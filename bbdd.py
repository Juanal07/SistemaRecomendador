import csv
import sqlite3

def insertarDatos():
    try:
        con = sqlite3.connect('bbdd/movielens.db')
    except:
        print("No conectado")
    cur = con.cursor()
    cont = 0
    with open('ml-latest-small\movies.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            print(', '.join(row))
            if cont == 0:
                cont += 1
            else:
                movieId = int(row[0])
                title = row[1]
                genres = row[2]

                cur.execute("INSERT INTO movie VALUES(?,?,?)", (movieId,title,genres))
            
    con.commit()
    
    cont = 0
    with open('ml-latest-small\/ratings.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            print(', '.join(row))
            if cont == 0:
                cont += 1
            else:
                userId = int(row[0])
                movieId = int(row[1])
                rating = float(row[2])
                timestamp = int(row[3])

                cur.execute("INSERT INTO rating(userId,movieId,rating,timestamp) VALUES(?,?,?,?)", (userId,movieId,rating,timestamp))
    con.commit()


    con.close()
