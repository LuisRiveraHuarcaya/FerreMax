import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from database.Conexion import Conexion

class Permisos():
    def __init__(self):
        self.conexion = Conexion()
    def crearRol(self,id_rol,nombre_rol): #Crear- Rol

        sql="""Select * from Rol where id=?
        """
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(sql,id_rol)
        result = cursor.fetchall()
        print("Result : ",result)
        if not result:
            print("Crear")
            sql="""Insert into Rol values(?,?)
            """
            con = self.conexion.conectar()
            cursor = con.cursor()
            cursor.execute(sql,id_rol,nombre_rol)
            cursor.commit()
            cursor.close()
            con.close()
        
            return True #No se encontro Rol existente en BD
        else:
            cursor.close()
            con.close()
            return False #Rol ya existe en la BD

    def crearPermisos(self,id_rol,id_area, indice): #id_rol, id_area, indice
        #Indices/Permisos: 0 Lectura, 1 Escritura
        if indice ==0: #----Lectura
            self.sqlPermisos(id_rol,id_area,indice)
        if indice == 1: #-------Escritura
            self.sqlPermisos(id_rol,id_area,indice)
        
    def sqlPermisos(self,id_rol,id_area,indice):
        #Permisos: id_rol, id_area, permiso
        sql="""Insert into Permisos values(?,?,?)
        """
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(sql,id_rol,id_area,indice)
        con.commit()
        cursor.close()
        con.close()
    def modificarPermisos(self,id_rol,id_area,permiso):
        #SQL [0,1,0]
        #Para agregar permisos a todas las Areas solo cambiar id_Area por cada Campo Check
        #id_rol, id_area, leer, insertar, modificar
        sql="""UPDATE Permisos SET id_rol={} id_area={} permiso={}
        """.format(id_rol,id_area,permiso)
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        cursor.close()
        con.close()
    def mostrarPermisos(self):
        #Muestra todos los registros de los productos
        sql="""Select r.nombre, a.nombre, permiso 
        from Permisos per INNER JOIN Area a ON per.id_area = a.id
        INNER JOIN Rol r ON r.id = per.id_rol"""
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        con.close()
        return result

    def cargarRolesCBOX(self):
        #Carga todos los nombre de Roles creados
        sql="""Select nombre 
        from Rol"""
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        con.close()
        return result