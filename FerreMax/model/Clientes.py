import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from database.Conexion import Conexion

class Clientes():
    #Tenemos que exportar Clase Conexion del paquete : Controlador
    def __init__(self):
        self.conexion = Conexion()

    def mostrarClientes(self):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = "Select * from Cliente"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        con.close()

        return result
    def crearCliente(self,dni,nombres,apellidos,telefono,direccion):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = "INSERT INTO Cliente values (?,?,?,?,?)"
        cursor.execute(sql,dni,nombres,apellidos,telefono,direccion)
        con.commit()
        cursor.close()
        con.close()
    
    def modificarCliente(self,dni,nombres,apellidos,telefono,direccion):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = "UPDATE Cliente SET nombre=?,apellidos=?, telefono=?,direccion=? where dni=?"
        cursor.execute(sql,nombres,apellidos,telefono,direccion,dni)
        con.commit()
        cursor.close()
        con.close()

    def eliminarCliente(self,dni):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = "DELETE from Cliente where dni=?"
        cursor.execute(sql,dni)
        con.commit()
        cursor.close()
        con.close()