import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from database.Conexion import Conexion
from model.Roles import Roles

class User():
    def __init__(self):
        self.conexion = Conexion()

    def eliminarUsuario(self,dni):
        con = self.conexion.conectar()
        cursor = con.cursor()
        #Crear usuario
        sql = "Delete from Empleado where dni=?"
        cursor.execute(sql,dni)
        cursor.commit()
        cursor.close()
        con.close()

    def modificarUsuario(self,dni,nombres,apellidos,sexo,nacimiento,telefono,email,usuario,password,id_rol):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql="""Update Empleado SET dni=?,nombres=?,apellidos=?,sexo=?,fecha_nacimiento=?,
        telefono=?,email=?,usuario=?,password=?,id_rol=? where dni=?
        """
        cursor.execute(sql,dni,nombres,apellidos,sexo,nacimiento,telefono,
        email,usuario,password,id_rol,dni)
        cursor.commit()
        cursor.close()
        con.close()
    def crearUsuario(self,dni,nombres,apellidos,sexo,nacimiento,telefono,email,usuario,password,id_rol):
        con = self.conexion.conectar()
        cursor = con.cursor()
        #Crear usuario
        sql = "Insert into Empleado values(?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,dni,nombres,apellidos,sexo,str(nacimiento),telefono,email,usuario,password,id_rol)
        print("SQL: ",sql)
        cursor.commit()
        cursor.close()
        con.close()
    def mostrarUsuarios(self):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = """Select dni,nombres,apellidos,sexo,fecha_nacimiento,telefono,email,usuario,password,
        r.nombre from Empleado e inner join Rol  r on e.id_rol = r.id
        """
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        con.close()
        return resultado
    def resetearListas(self):
        Roles.Clientes = ""
        Roles.Empleados = ""
        Roles.Proveedores = ""
        Roles.Productos = ""
        Roles.Almacen = ""
        Roles.Ventas = ""
        Roles.Mantenimiento = ""
        print("Reseteando listas Clientes:", Roles.Clientes)
    def validarCredenciales(self,usuario,password):
        self.resetearListas()
        
        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Empleado where usuario = '{}' and password= '{}'".format(usuario,password))
        self.empleado = cursor.fetchall()
        #Empleado: usuario,password, rol
        print(self.empleado)
        if self.empleado:
            for usuario in self.empleado:
                print('Bienvenido '+ usuario[1])

                # SQL  que busca solo los permisos del id_ROL que se extraen del Usuario en otra consulta
                sql = """Select a.nombre, permiso
                from Permisos p
                INNER JOIN  Rol r ON p.id_rol = r.id
                INNER JOIN Area a ON a.id = p.id_area
                where id_rol = {}
                """.format(usuario[9])
                cursor.execute(sql)
                self.permisos = cursor.fetchall() # Se extraen todos los permisos[()] del Rol
                print("Permisos : ",self.permisos)
                for dato in self.permisos: #---- dato['Area',permiso] = ['Clientes',1]
                    print("Dato : ",dato)
                    if dato[0] == 'Clientes' : #----Verifica si tiene permisos en Area Clientes
                        Roles.Clientes = dato[1]
                    if dato[0] == 'Empleados' : #----Verifica si tiene permisos en Area Empleados
                        Roles.Empleados = dato[1]
                    if dato[0] == 'Proveedores' :
                        Roles.Proveedores = dato[1]
                    if dato[0] == 'Productos' : 
                        Roles.Productos = dato[1]
                    if dato[0] == 'Almacen' : 
                        Roles.Almacen = dato[1]
                    if dato[0] == 'Ventas' : 
                        Roles.Ventas = dato[1]
                    if dato[0] == 'Mantenimiento' : 
                        Roles.Mantenimiento = dato[1]
                    print(Roles.Clientes)
                    print(Roles.Empleados)
                    print(Roles.Proveedores)
                    print(Roles.Productos)
                    print(Roles.Almacen)
                    print(Roles.Ventas)
                    print(Roles.Mantenimiento)
            cursor.close()
            con.close()
            return True
        else:
            cursor.close()
            con.close()
            return False


        
