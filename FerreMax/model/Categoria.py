import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from database.Conexion import Conexion

class Categoria():
    def __init__(self):
        self.conexion = Conexion()

    def getID_categoria(self,name):
        sql="Select id from Categoria where nombre = ?"
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(sql, name)
        result = cursor.fetchone()
        cursor.close()
        con.close()
        print("Obteniendo id categoria: ", result[0])
        return result[0]
        
    def getNames_categorias(self):
        sql="""Select nombre 
        from Categoria"""
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        con.close()
        return result