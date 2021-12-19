import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from view.almacen import Almacen_frm

class Almacen_Controller():

    def __init__(self):
        self.frm_almacen = Almacen_frm()
        #self.frm_almacen = Almacen_frm
    def mostrar(self):
        self.frm_almacen.show()
    def ocultar(self):
        self.frm_almacen.hide()
