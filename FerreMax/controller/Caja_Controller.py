import sys
import os

from PyQt5 import QtWidgets

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")
from view.caja import Caja


class Caja_Controller():


    def __init__(self):
        self.caja_frm = Caja()
        self.widget = QtWidgets.QMainWindow()
        self.caja_frm.setupUi(self.widget)

    def mostrar(self):
        self.widget.show()
    def ocultar(self):
        self.widget.hide()