import sys
import os

from PyQt5 import QtWidgets

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")
from view.caja import Caja


from view.empleados import Gestion_Usuarios

class Control():

    def __init__(self):
        self.frm = Gestion_Usuarios()
        self.widget = QtWidgets.QWidget()
        self.frm.setupUi(self.widget)
        self.setEvents()

    def setEvents(self):
        self.frm.btn_crear_usuario.clicked.connect(self.getFecha)
    
    def getFecha(self):
        fecha = self.frm.date_nacimiento_usuario.date()
        print(fecha.toPyDate())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cont = Control()
    cont.widget.show()
    sys.exit(app.exec_())