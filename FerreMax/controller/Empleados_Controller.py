import sys
import os
from typing import MutableSequence
#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")


from view.empleados import Empleados
from PyQt5.QtWidgets import QWidget
from model.Permisos import Permisos
from model.User import User
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Empleados_Controller():

    def __init__(self):
        self.frm_gestionUsuario = Empleados()
        self.widget_gestionUsuario = QWidget()
        self.frm_gestionUsuario.setupUi(self.widget_gestionUsuario)
        self.mod_permisos = Permisos() # Modelo_mod_permisos BD
        self.mod_user = User() #Mod User BD
        self.setEventos()

    def setEventos(self):
        #self.frm_gestionUsuario.chk_almacen.clicked.connect()
        self.frm_gestionUsuario.btn_crear_rol.clicked.connect(self.crearRol)
        self.frm_gestionUsuario.btn_buscar_rol.clicked.connect(self.mostrarPermisos)

        self.frm_gestionUsuario.pantalla_tab.currentChanged.connect(self.cargarRolesCBOX)

        self.frm_gestionUsuario.btn_crear_usuario.clicked.connect(self.crearUsuario)
        self.frm_gestionUsuario.btn_buscar_usuario.clicked.connect(self.mostrarUsuarios)
        self.frm_gestionUsuario.btn_modificar_usuario.clicked.connect(self.modificarUsuario)
        self.frm_gestionUsuario.btn_eliminar_usuario.clicked.connect(self.eliminarUsuario)

        #No permite editar las filas de la tabla
        self.frm_gestionUsuario.tabla_usuarios.setEditTriggers (QtWidgets.QAbstractItemView.NoEditTriggers)
        #Selecciona toda la fila de una tabla, sin esta opcion solo selecciona casillas individuales
        self.frm_gestionUsuario.tabla_usuarios.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.frm_gestionUsuario.tabla_usuarios.cellClicked.connect(self.getItemsTabla)

    def mostrar(self):
        #Antes de mostrar vista, cargar roles CBOx
        self.cargarRolesCBOX()
        self.widget_gestionUsuario.show()
    def ocultar(self):
        self.widget_gestionUsuario.hide()
    def cargarRolesCBOX(self):
        #Obtener lista de Roles y mostrar en el ComboBox
        print("Cargar roles")
        lista = self.mod_permisos.cargarRolesCBOX()
        self.frm_gestionUsuario.cbx_rol_usuario.clear()
        for item in lista:
            self.frm_gestionUsuario.cbx_rol_usuario.addItem(item[0])
        
    def mostrarUsuarios(self):
        usuarios = self.mod_user.mostrarUsuarios() #--Devuelve result de todos los Usuarios
        self.frm_gestionUsuario.tabla_usuarios.setRowCount(0)

        for row_numb , row_data in enumerate(usuarios):
            self.frm_gestionUsuario.tabla_usuarios.insertRow(row_numb)
            for colum_num, data in enumerate(row_data):
                self.frm_gestionUsuario.tabla_usuarios.setItem(row_numb,colum_num, QtWidgets.QTableWidgetItem(str(data)))

    def mostrarPermisos(self): #---Muestra todos Roles y Permisos tabla
        mod_permisos = self.mod_permisos.mostrarPermisos()
        self.frm_gestionUsuario.tabla_roles.setRowCount(0)

        for row_numb , row_data in enumerate(mod_permisos):
            self.frm_gestionUsuario.tabla_roles.insertRow(row_numb)
            if row_data[2]== 1: #Cambia valor True por: Leer
                row_data[2] = "Leer"
            if row_data[2]== 2: #Cambia valor de permisos False por: Leer/Escribir
                row_data[2] = "Leer-Escribir"
            for colum_num, data in enumerate(row_data):
                print("Data: ",data)
                self.frm_gestionUsuario.tabla_roles.setItem(row_numb,colum_num, QtWidgets.QTableWidgetItem(str(data)))

    def getItemsTabla(self):
        #Devuelve datos de cada indice de columna de la Tabla 
        dni = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[0].data()
        nomb = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[1].data()
        ape = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[2].data()
        sexo = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[3].data()
        fecha = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[4].data()
        date = QtCore.QDate.fromString(fecha,'yyyy-MM-dd')

        telefono = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[5].data()
        email = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[6].data()
        usuario = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[7].data()
        password = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[8].data()
        rol = self.frm_gestionUsuario.tabla_usuarios.selectedIndexes()[9].data()
        print(date)

        self.frm_gestionUsuario.txt_dni.setText(dni)
        self.frm_gestionUsuario.txt_nombres.setText(nomb)
        self.frm_gestionUsuario.txt_apellidos.setText(ape)
        se = self.frm_gestionUsuario.cbx_sexo_usuario.findText(sexo)
        self.frm_gestionUsuario.cbx_sexo_usuario.setCurrentIndex(se)
        self.frm_gestionUsuario.date_nacimiento_usuario.setDate(date)
        self.frm_gestionUsuario.txt_telefono.setText(telefono)
        self.frm_gestionUsuario.txt_email.setText(email)
        self.frm_gestionUsuario.txt_usuario.setText(usuario)
        self.frm_gestionUsuario.txt_password.setText(password)
        i_rol =self.frm_gestionUsuario.cbx_rol_usuario.findText(rol)
        self.frm_gestionUsuario.cbx_rol_usuario.setCurrentIndex(i_rol)
    
    def modificarUsuario(self):
        lista = self.getDatosFormularioUsuario()

        if self.validarCampos(lista[0],lista[1],lista[2],lista[6],lista[7],lista[8],lista[9]):
            self.mod_user.modificarUsuario(lista[0],lista[1],lista[2],
            lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9])

            self.mostrarUsuarios()
        else:
            self.mensajeValidacionFail()
    def crearUsuario(self):
        lista = self.getDatosFormularioUsuario()
        #Respuesta 0: dni ya existe, 1:campo usuario ya existe, 2: registro exitoso
        #dni,nom,ape,tel,email,usu,pass
        if self.validarCampos(lista[0],lista[1],lista[2],lista[6],lista[7],lista[8],lista[9]):
            self.mod_user.crearUsuario(lista[0],lista[1],lista[2],
            lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9])

            self.mostrarUsuarios()
        else:
            self.mensajeValidacionFail()
    def eliminarUsuario(self):
        dni = self.frm_gestionUsuario.txt_dni.text()

        if not dni=="" or dni.isspace():
            self.mod_user.eliminarUsuario(dni)
            
            self.mostrarUsuarios()
        else:
            QtWidgets.QMessageBox.information(self.widget_gestionUsuario, "Validacion de campos", """Por favor llene todos los campos""",
            QtWidgets.QMessageBox.Ok)

    def getDatosFormularioUsuario(self):
        dni =  self.frm_gestionUsuario.txt_dni.text()
        nombres =  self.frm_gestionUsuario.txt_nombres.text()
        apellidos =  self.frm_gestionUsuario.txt_apellidos.text()
        sexo =  self.frm_gestionUsuario.cbx_sexo_usuario.currentText()
        date =  self.frm_gestionUsuario.date_nacimiento_usuario.date() # fecha.toPyDate() --convierte a formato String
        fecha = date.toPyDate()
        telefono =  self.frm_gestionUsuario.txt_telefono.text()
        email =  self.frm_gestionUsuario.txt_email.text()
        usuario =  self.frm_gestionUsuario.txt_usuario.text()
        password =  self.frm_gestionUsuario.txt_password.text()
        rol = self.frm_gestionUsuario.cbx_rol_usuario.currentIndex()
        rol = rol + 1
        return [dni,nombres,apellidos,sexo,fecha,telefono,email,usuario,password,rol]

    def crearRol(self):
        chk_clientes = self.frm_gestionUsuario.chk_clientes
        chk_empleados = self.frm_gestionUsuario.chk_empleados
        chk_proveedores = self.frm_gestionUsuario.chk_proveedores
        chk_productos = self.frm_gestionUsuario.chk_productos
        chk_almacen = self.frm_gestionUsuario.chk_almacen
        chk_ventas = self.frm_gestionUsuario.chk_ventas
        chk_mantenimiento = self.frm_gestionUsuario.chk_mantenimiento

        txt_rol = self.frm_gestionUsuario.txt_nombre_rol.text()

        id_rol = self.frm_gestionUsuario.txt_id_rol.text() #Obtiene el ID del TextField

        if self.validarCamposRol(id_rol,txt_rol):
            if self.mod_permisos.crearRol(int(id_rol),txt_rol):
                #Clientes
                if chk_clientes.isChecked():
                    indice = self.frm_gestionUsuario.cbx_permisos_clientes.currentIndex()
                    self.mod_permisos.crearPermisos(int(id_rol),1,indice)
                #Empleados
                if chk_empleados.isChecked():
                    indice = self.frm_gestionUsuario.cbx_permisos_empleados.currentIndex()
                    self.mod_permisos.crearPermisos(int(id_rol),2,indice)
                #Proveedores
                if chk_proveedores.isChecked():
                    indice = self.frm_gestionUsuario.cbx_permisos_proveedores_2.currentIndex()
                    self.mod_permisos.crearPermisos(int(id_rol),3,indice)
                #Productos: ID
                if chk_productos.isChecked():
                    indice = self.frm_gestionUsuario.cbx_permisos_productos.currentIndex()
                    self.mod_permisos.crearPermisos(int(id_rol),4,indice)
                #Almacen: ID
                if chk_almacen.isChecked():
                    indice = self.frm_gestionUsuario.cbx_permisos_almacen.currentIndex()
                    self.mod_permisos.crearPermisos(int(id_rol),5,indice)
                #Ventas: ID
                if chk_ventas.isChecked():
                    indice = self.frm_gestionUsuario.cbx_permisos_ventas.currentIndex()
                    self.mod_permisos.crearPermisos(int(id_rol),6,indice)
                #Mantenimiento: ID
                if chk_mantenimiento.isChecked():
                    #Mantenimiento tiene de indice 1 por defecto
                    self.mod_permisos.crearPermisos(int(id_rol),7,1)
                print("Se creo el rol y los permisos")
            else:
                print("Rol ya existe en la BD")
        else:
            self.mensajeValidacionFail()

    def modificarRol(self):
        pass
        
    def mensajeValidacionFail(self):
        QtWidgets.QMessageBox.information(self.widget_gestionUsuario, "Validacion de campos", """Por favor llene todos los campos""",
        QtWidgets.QMessageBox.Ok)

    def validarCamposRol(self,id,n):
        if id =="" or n=="" or id.isspace() or n.isspace():
            return False
        else:
            return True

    def validarCampos(self,dni,n,a,t,e,us,ps):
        #dni,nom,ape,tel,email,usu,pass
        if dni=="" or n=="" or a=="" or t=="" or e=="" or us=="" or ps=="" or dni.isspace() or n.isspace() or a.isspace() or t.isspace() or e.isspace() or us.isspace() or ps.isspace():
            return False
        else:
            return True  #---campos ok