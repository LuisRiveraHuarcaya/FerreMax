import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from view.login import Login_frm
from controller.Principal_Controller import Principal_Controller

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from model.Roles import Roles
from model.User import User

class Login_Controller():

    def __init__(self):
        self.login_frm = Login_frm()
        self.principal_controller = Principal_Controller()
        self.mod_user = User()
        self.setEvents()

    def setEvents(self):
        self.login_frm.btn_ingresar.clicked.connect(self.validarUsuario)
        self.login_frm.btn_cancelar.clicked.connect(self.login_frm.close)
        self.login_frm.btn_limpiar.clicked.connect(self.limpiar)
    def mostrar(self):
        self.login_frm.show()
    def ocultar(self):
        self.login_frm.hide()

    def setPermisos(self):
        if not Roles.Clientes: #Si lista CLIENTES esta vacio entonces bloquear acceso
            self.principal_controller.frm_principal.btn_clientes.setEnabled(False)
            self.principal_controller.frm_principal.menu_Clientes.setEnabled(False)
        if not Roles.Empleados:
            self.principal_controller.frm_principal.btn_empleados.setEnabled(False)
        if not Roles.Proveedores:
            self.principal_controller.frm_principal.btn_proveedores.setEnabled(False)
        if not Roles.Productos:
            self.principal_controller.frm_principal.btn_productos.setEnabled(False)
        if not Roles.Almacen:
            self.principal_controller.frm_principal.btn_almacen.setEnabled(False)
        if not Roles.Ventas:
            self.principal_controller.frm_principal.btn_caja.setEnabled(False)
        if not Roles.Mantenimiento:
            self.principal_controller.frm_principal.btn_mantenimiento.setEnabled(False)
            self.principal_controller.frm_principal.menu_Mantenimiento.setEnabled(False)

    def ingresar(self):
        # Se agregan las restricciones antes de mostrar Frame Principal
        self.setPermisos()

        self.login_frm.hide()  # esconde la ventana
        self.login_frm.close() # cierra la ventana
        self.principal_controller.mostrar()
    def validarUsuario(self):
        self.usuario = self.login_frm.txt_usuario.text()
        self.password = self.login_frm.txt_password.text()

        #Validando credenciales des Modelo User
        if self.mod_user.validarCredenciales(self.usuario,self.password):
            self.ingresar()
        else:
            print('Usuario no encontrado')
            QMessageBox.warning(self.login_frm, "No se encontro usuario", """Por favor ingrese credenciales validas""",
            QMessageBox.Ok)

    def limpiar(self):
        self.login_frm.txt_usuario.clear()
        self.login_frm.txt_password.clear()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #frm_login = QtWidgets.QWidget()
    #frm = Login_frm()
    c = Login_Controller()
    c.login_frm.show()
    sys.exit(app.exec_())
