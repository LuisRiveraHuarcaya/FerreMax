import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")





from PyQt5 import QtWidgets
from controller.Login_Controller import Login_Controller

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    login_cont = Login_Controller()
    login_cont.mostrar()
    sys.exit(app.exec_())
    