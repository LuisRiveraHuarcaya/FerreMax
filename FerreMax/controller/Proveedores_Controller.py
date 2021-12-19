import sys
import os

from PyQt5 import QtWidgets

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")
from view.proveedores import Proveedores
from model.Roles import Roles
from model.Proveedores import Proveedores as MProveedor
class Proveedores_Controller():


    def __init__(self):
        self.proveedores_frm = Proveedores()
        self.widget = QtWidgets.QWidget()
        self.proveedores_frm.setupUi(self.widget)

        self.mod_proveedor = MProveedor()

        self.setEvents()

    def mostrar(self):
        self.setPermisos()
        self.widget.show()

    def ocultar(self):
        self.widget.hide()

    def setEvents(self):
        self.proveedores_frm.btn_crear.clicked.connect(self.crearProveedor)
        self.proveedores_frm.btn_modificar.clicked.connect(self.modificarProveedor)
        self.proveedores_frm.btn_eliminar.clicked.connect(self.eliminarProveedor)

        self.proveedores_frm.btn_buscar.clicked.connect(self.buscarProveedor)
        #No permite editar las filas de la tabla
        self.proveedores_frm.tabla_proveedores.setEditTriggers (QtWidgets.QAbstractItemView.NoEditTriggers)
        #Selecciona toda la fila de una tabla, sin esta opcion solo selecciona casillas individuales
        self.proveedores_frm.tabla_proveedores.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.proveedores_frm.tabla_proveedores.cellClicked.connect(self.getItemTabla)

    def setPermisos(self):
        if Roles.Proveedores == 1: #--Lectura
            self.proveedores_frm.groupBox.setEnabled(False)
        if Roles.Proveedores == 2: #--Escritura
            self.proveedores_frm.groupBox.setEnabled(True)

    def crearProveedor(self):
        ruc = self.proveedores_frm.txt_ruc.text()
        nombre = self.proveedores_frm.txt_nombre.text()
        email = self.proveedores_frm.txt_email.text()
        telefono = self.proveedores_frm.txt_telefono.text()
        direc = self.proveedores_frm.txt_direccion.text()

        if self.validarCampos(ruc,nombre,email,telefono,direc):

            self.mod_proveedor.crearProveedor(ruc,nombre,email,telefono,direc)
            self.buscarProveedor() #Muestra todos los proveedores en tabla
        else:
            self.mensajeValidacionFail()


    def modificarProveedor(self):
        ruc = self.proveedores_frm.txt_ruc.text()
        nombre = self.proveedores_frm.txt_nombre.text()
        email = self.proveedores_frm.txt_email.text()
        telefono = self.proveedores_frm.txt_telefono.text()
        direc = self.proveedores_frm.txt_direccion.text()

        if self.validarCampos(ruc,nombre,email,telefono,direc):
            self.mod_proveedor.modificarProveedor(ruc,nombre,email,telefono,direc)
            self.buscarProveedor()
        else:
            self.mensajeValidacionFail()
    
    def eliminarProveedor(self):
        ruc = self.proveedores_frm.txt_ruc.text()

        if not ruc=="" or ruc.isspace():
            self.mod_proveedor.eliminarProveedor(ruc)
            self.buscarProveedor()
        else: #--Mostrar mensaje de validacion 
            QtWidgets.QMessageBox.information(self.widget, "Validacion de campos", """Debe ingresar un RUC""",
            QtWidgets.QMessageBox.Ok)

    def getItemTabla(self):
        #Devuelve datos de cada indice de columna 
        ruc = self.proveedores_frm.tabla_proveedores.selectedIndexes()[0].data()
        nomb = self.proveedores_frm.tabla_proveedores.selectedIndexes()[1].data()
        email = self.proveedores_frm.tabla_proveedores.selectedIndexes()[2].data()
        telefono = self.proveedores_frm.tabla_proveedores.selectedIndexes()[3].data()
        direccion = self.proveedores_frm.tabla_proveedores.selectedIndexes()[4].data()

        self.proveedores_frm.txt_ruc.setText(ruc)
        self.proveedores_frm.txt_nombre.setText(nomb)
        self.proveedores_frm.txt_email.setText(email)
        self.proveedores_frm.txt_telefono.setText(telefono)
        self.proveedores_frm.txt_direccion.setText(direccion)


    def buscarProveedor(self):

        lista = self.mod_proveedor.mostrarProveedores()
        self.proveedores_frm.tabla_proveedores.setRowCount(0)
        print(lista)
        for row_numb , row_data in enumerate(lista):
            self.proveedores_frm.tabla_proveedores.insertRow(row_numb)
            for colum_num, data in enumerate(row_data):
                self.proveedores_frm.tabla_proveedores.setItem(row_numb,colum_num, QtWidgets.QTableWidgetItem(str(data)))

    def mensajeValidacionFail(self):
        QtWidgets.QMessageBox.information(self.widget, "Validacion de campos", """Por favor llene todos los campos""",
        QtWidgets.QMessageBox.Ok)

    def validarCampos(self,r,n,e,t,d):
        # Validacion de vacios : c==""      Validacion de espacios:  c.isspace()
        if r=="" or n=="" or e=="" or t=="" or d=="" or r.isspace() or n.isspace() or e.isspace() or t.isspace() or d.isspace():
            return False
        else:
            return True  #---campos ok