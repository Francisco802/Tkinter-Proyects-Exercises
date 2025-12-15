import sqlite3 as sql

def createDB():
    conn=sql.connect("database\\animes.db")
    conn.commit()
    conn.close()

def createTable():
    conn=sql.connect("database\\animes.db")
    cursor=conn.cursor()
    instruccion="""CREATE TABLE animesList(
                codigo integer,
                titulo text,
                duracion integer
                )"""
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertRow(nombre,followers,subs):
    conn=sql.connect("database\\animes.db")
    cursor=conn.cursor()
    instruccion=f"""INSERT INTO animesList
                VALUES ("{nombre},{followers},{subs}") 
                """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRows():
    conn=sql.connect("database\\animes.db")
    cursor=conn.cursor()
    instruccion=f"""SELECT *FROM animesList"""
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)    #Arreglo de tuplas

def insertRows(streamersList):
    conn=sql.connect("database\\animes.db")
    cursor=conn.cursor()
    instruccion=f"""INSERT INTO animes VALUES (?,?,?)"""
    cursor.executemany(instruccion,streamersList)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn=sql.connect("database\\animes.db")
    cursor=conn.cursor()
    instruccion=f"""SELECT *FROM animes ORDER BY
                {field} DESC
                """
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()

def search():
    conn=sql.connect("database\\animes.db")
    cursor=conn.cursor()
    instruccion=f"""SELECT *FROM animes WHERE
                name="Alex"
                """
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()

def updateFields():
    conn=sql.connect("database\\animes.db")
    cursor=conn.cursor()
    instruccion=f"""UPDATE animes SET followers 120000
                WHERE name like "name"
                """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def delate():
    conn=sql.connect("database\\animes.db")
    cursor=conn.cursor()
    instruccion=f"""DELATE FROM animes WHERE
                name = "name"
                """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    ...
    #>sqlite
    #createDB()
    #createTable()