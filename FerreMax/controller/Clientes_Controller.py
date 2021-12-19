import sys
import os
from typing import ValuesView

from PyQt5 import QtWidgets

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")
from view.clientes import Clientes
from model.Roles import Roles
from model.Clientes import Clientes as MClientes

class Clientes_Controller():


    def __init__(self):
        self.clientes_frm = Clientes()
        self.widget = QtWidgets.QWidget()
        self.clientes_frm.setupUi(self.widget)
        self.mod_cliente = MClientes()
        self.setEvents()

    def mostrar(self):
        self.setPermisos()
        self.widget.show()
    def ocultar(self):
        self.widget.hide()
    def setEvents(self):
        self.clientes_frm.pushButton.clicked.connect(self.crearCliente) #btn_crear
        self.clientes_frm.pushButton_2.clicked.connect(self.modificarCliente) #--btn_modificar
        self.clientes_frm.pushButton_3.clicked.connect(self.eliminarCliente) #btn_eliminar

        self.clientes_frm.pushButton_4.clicked.connect(self.buscarCliente)#btn_buscar
        
        #No permite editar las filas de la tabla
        self.clientes_frm.tableWidget.setEditTriggers (QtWidgets.QAbstractItemView.NoEditTriggers)
        #Selecciona toda la fila de una tabla, sin esta opcion solo selecciona casillas individuales
        self.clientes_frm.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.clientes_frm.tableWidget.cellClicked.connect(self.getItemTabla)

    def getItemTabla(self):
        #Devuelve datos de cada indice de columna 
        dni = self.clientes_frm.tableWidget.selectedIndexes()[0].data()
        nomb = self.clientes_frm.tableWidget.selectedIndexes()[1].data()
        apellidos = self.clientes_frm.tableWidget.selectedIndexes()[2].data()
        telefono = self.clientes_frm.tableWidget.selectedIndexes()[3].data()
        direccion = self.clientes_frm.tableWidget.selectedIndexes()[4].data()

        self.clientes_frm.lineEdit.setText(dni)
        self.clientes_frm.lineEdit_2.setText(nomb)
        self.clientes_frm.lineEdit_3.setText(apellidos)
        self.clientes_frm.lineEdit_4.setText(telefono)
        self.clientes_frm.lineEdit_5.setText(direccion)

    def crearCliente(self):
        dni = self.clientes_frm.lineEdit.text() #dni
        nombre = self.clientes_frm.lineEdit_2.text() #nombres
        apellidos = self.clientes_frm.lineEdit_3.text() #apellidos
        telefono = self.clientes_frm.lineEdit_4.text() #telefono
        direccion = self.clientes_frm.lineEdit_5.text() #direccion
        
        if self.validarCampos(dni,nombre,apellidos,telefono,direccion):
            self.mod_cliente.crearCliente(dni,nombre,apellidos,telefono,direccion)
            self.buscarCliente()
        else:
            self.mensajeValidacionFail()

    def modificarCliente(self):
        dni = self.clientes_frm.lineEdit.text() #dni
        nombre = self.clientes_frm.lineEdit_2.text() #nombres
        apellidos = self.clientes_frm.lineEdit_3.text() #apellidos
        telefono = self.clientes_frm.lineEdit_4.text() #telefono
        direccion = self.clientes_frm.lineEdit_5.text() #direccion

        if self.validarCampos(dni,nombre,apellidos,telefono,direccion):
            self.mod_cliente.modificarCliente(dni,nombre,apellidos,telefono ,direccion)
            self.buscarCliente()
        else:
            self.mensajeValidacionFail()

    def eliminarCliente(self):
        dni = self.clientes_frm.lineEdit.text() #dni
        
        if not dni=="" or dni.isspace():
            self.mod_cliente.eliminarCliente(dni)
            self.buscarCliente()
        else:
            QtWidgets.QMessageBox.information(self.widget, "Validacion de campos", """Debe ingresar un DNI""",
            QtWidgets.QMessageBox.Ok)
    
    def buscarCliente(self):
        lista = self.mod_cliente.mostrarClientes()  #Devuelve Lista[] de Clientes

        self.clientes_frm.tableWidget.setRowCount(0)

        for row_numb , row_data in enumerate(lista):
            self.clientes_frm.tableWidget.insertRow(row_numb)
            for colum_num, data in enumerate(row_data):
                self.clientes_frm.tableWidget.setItem(row_numb,colum_num, QtWidgets.QTableWidgetItem(str(data)))

    def setPermisos(self):
        if Roles.Clientes == 1: #--Lectura
            self.clientes_frm.groupBox.setEnabled(False)
        if Roles.Clientes == 2: #--Escritura
            self.clientes_frm.groupBox.setEnabled(True)

    def mensajeValidacionFail(self):
        QtWidgets.QMessageBox.information(self.widget, "Validacion de campos", """Por favor llene todos los campos""",
        QtWidgets.QMessageBox.Ok)

    def validarCampos(self,dni,n,a,t,d):
        # Validacion de vacios : c==""      Validacion de espacios:  c.isspace()
        if dni=="" or n=="" or a=="" or t=="" or d=="" or dni.isspace() or n.isspace() or a.isspace() or t.isspace() or d.isspace():
            return False
        else:
            return True  #---campos ok