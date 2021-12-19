
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Almacen_frm(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("frm_Almacen")
        self.resize(400, 300)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.txt_buscar = QtWidgets.QLineEdit(self)
        self.txt_buscar.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.txt_buscar.setObjectName("txt_buscar")
        self.cbx_busqueda = QtWidgets.QComboBox(self)
        self.cbx_busqueda.setGeometry(QtCore.QRect(150, 40, 211, 22))
        self.cbx_busqueda.setObjectName("cbx_busqueda")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("frm_Almacen", "Form"))
        self.label.setText(_translate("frm_Almacen", "Buscar producto:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    almacen = Almacen_frm()
    almacen.show()
    sys.exit(app.exec_())
