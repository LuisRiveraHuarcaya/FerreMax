import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from database.Conexion import Conexion

class Proveedores():
    #Tenemos que exportar Clase Conexion del paquete : Controlador
    def __init__(self):
        self.conexion = Conexion()

    def getID_proveedor(self,name):
        sql="Select ruc from Proveedor where nombre = ?"
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(sql, name)
        result = cursor.fetchone()
        cursor.close()
        con.close()
        print("Obteniendo id proveedor: ", result[0])
        return result[0]

    def getNames_proveedor(self):
        sql="Select nombre from Proveedor"
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        con.close()
        return result
    def mostrarProveedores(self):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = "Select * from Proveedor"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        con.close()

        return result
    def crearProveedor(self,ruc,nombre,email,telefono,direccion):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = "INSERT INTO Proveedor values(?,?,?,?,?)"
        cursor.execute(sql,ruc,nombre,email,telefono,direccion)
        con.commit()
        cursor.close()
        con.close()

    def modificarProveedor(self,ruc,nombre,email,telefono,direccion): #No valida RUC dos veces por que al intentar editar, no encuentra RUC nuevo en BD xD
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = "UPDATE Proveedor SET nombre=?,email=?,telefono=?,direccion=? where ruc=?"
        cursor.execute(sql,nombre,email,telefono,direccion,ruc)
        con.commit()
        cursor.close()
        con.close()

    def eliminarProveedor(self,ruc):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = "DELETE from Proveedor where ruc=?"
        cursor.execute(sql,ruc)
        con.commit()
        cursor.close()
        con.close()
        pass