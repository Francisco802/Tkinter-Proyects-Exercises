import sqlite3 as sql
#ctrl + shift + t -> buscar sqlite -> open database
# buscador anadir ">" + sqlite

animeDB ="assets\\database\\animes.db"

class dataBse():

    def createDB(self):
        conn=sql.connect(animeDB)
        conn.commit()
        conn.close()

    def createTable(self):
        conn=sql.connect(animeDB)
        cursor=conn.cursor()
        instruccion="""CREATE TABLE animesList(
                    codigo integer,
                    titulo text,
                    duracion integer
                    )"""
        cursor.execute(instruccion)
        conn.commit()
        conn.close()

    def insertRow(self,code,title,caps):
        conn=sql.connect(animeDB)
        cursor=conn.cursor()
        instruccion=f"""INSERT INTO animesList
                    VALUES ({code},"{title}",{caps}) 
                    """
        cursor.execute(instruccion)
        conn.commit()
        conn.close()

    def readRows(self):
        conn=sql.connect(animeDB)
        cursor=conn.cursor()
        instruccion=f"""SELECT *FROM animesList"""
        cursor.execute(instruccion)
        datos=cursor.fetchall()
        conn.commit()
        conn.close()
        print(datos)    #Arreglo de tuplas

    def insertRows(self,animedata):
        conn=sql.connect(animeDB)
        cursor=conn.cursor()
        instruccion=f"""INSERT INTO animesList VALUES (?,?,?)"""
        cursor.executemany(instruccion,animedata)
        conn.commit()
        conn.close()

    def readOrdered(self,field):
        conn=sql.connect(animeDB)
        cursor=conn.cursor()
        instruccion=f"""SELECT *FROM animes ORDER BY
                    {field} DESC
                    """
        cursor.execute(instruccion)
        datos=cursor.fetchall()
        conn.commit()
        conn.close()

    def search(self,code):
        conn=sql.connect(animeDB)
        cursor=conn.cursor()
        instruccion=f"""SELECT *FROM animesList WHERE
                    codigo={code}
                    """
        cursor.execute(instruccion)
        datos=cursor.fetchall()
        conn.commit()
        conn.close()
        return datos

    def updateFields(self,code,caps):
        conn=sql.connect(animeDB)
        cursor=conn.cursor()
        instruccion=f"""UPDATE animesList SET duracion = {caps}
                    WHERE codigo = {code}
                    """
        cursor.execute(instruccion)
        conn.commit()
        conn.close()

    def delate(self,code):
        conn=sql.connect(animeDB)
        cursor=conn.cursor()
        instruccion=f"""DELETE FROM animesList WHERE
                    codigo = {code}
                    """
        cursor.execute(instruccion)
        conn.commit()
        conn.close()


if __name__ == "__main__":
    bd = dataBse
    #bd.createDB()
    #bd.createTable()