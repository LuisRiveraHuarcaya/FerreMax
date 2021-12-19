import sys
import os

from PyQt5 import QtWidgets
from controller.Almacen_Controller import Almacen_Controller
from controller.Caja_Controller import Caja_Controller
from controller.Clientes_Controller import Clientes_Controller
from controller.Proveedores_Controller import Proveedores_Controller

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from view.frm_principal import Principal_frm
from controller.Productos_Controller import Productos_Controller
from controller.Empleados_Controller import Empleados_Controller

class Principal_Controller():

    def __init__(self):
        self.frm_principal = Principal_frm()
        self.main_window = QtWidgets.QMainWindow()
        self.frm_principal.setupUi(self.main_window)
        self.almacen_controller = Almacen_Controller()
        self.productos_controller = Productos_Controller()
        self.empleados_controller = Empleados_Controller()
        self.caja_controller = Caja_Controller()
        self.proveedores_controller = Proveedores_Controller()
        self.clientes_controller = Clientes_Controller()
        self.setEvents()
    def mostrar(self):
        self.main_window.show()
    def ocultar(self):
        self.main_window.hide()
    def setEvents(self):
        self.frm_principal.btn_clientes.clicked.connect(self.clientes_controller.mostrar)
        self.frm_principal.btn_caja.clicked.connect(self.caja_controller.mostrar)
        self.frm_principal.btn_proveedores.clicked.connect(self.proveedores_controller.mostrar)
        self.frm_principal.btn_almacen.clicked.connect(self.almacen_controller.mostrar)
        self.frm_principal.btn_empleados.clicked.connect(self.empleados_controller.mostrar)
        self.frm_principal.btn_productos.clicked.connect(self.productos_controller.mostrar)