import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from PyQt5 import QtCore, QtGui, QtWidgets


class Login_frm(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(437, 300)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridGroupBox_3 = QtWidgets.QGroupBox(self)
        self.gridGroupBox_3.setGeometry(QtCore.QRect(10, 80, 241, 121))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.gridGroupBox_3.setFont(font)
        self.gridGroupBox_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.gridGroupBox_3.setAcceptDrops(False)
        self.gridGroupBox_3.setAutoFillBackground(False)
        self.gridGroupBox_3.setStyleSheet("")
        self.gridGroupBox_3.setObjectName("gridGroupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridGroupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.txt_usuario = QtWidgets.QLineEdit(self.gridGroupBox_3)
        self.txt_usuario.setObjectName("txt_usuario")

        self.gridLayout_4.addWidget(self.txt_usuario, 0, 2, 1, 1)

        self.txt_password = QtWidgets.QLineEdit(self.gridGroupBox_3)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")

        self.gridLayout_4.addWidget(self.txt_password, 1, 2, 1, 1)
        
        self.cbx_cargo = QtWidgets.QComboBox(self.gridGroupBox_3)
        self.cbx_cargo.setToolTip("")
        self.cbx_cargo.setStatusTip("")
        self.cbx_cargo.setWhatsThis("")
        self.cbx_cargo.setAccessibleName("")
        self.cbx_cargo.setCurrentText("Administrador")
        self.cbx_cargo.setObjectName("cbx_cargo")
        self.cbx_cargo.addItem("")
        self.cbx_cargo.addItem("")
        self.cbx_cargo.addItem("")
        self.gridLayout_4.addWidget(self.cbx_cargo, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridGroupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridGroupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridGroupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.horizontalGroupBox_2 = QtWidgets.QGroupBox(self)
        self.horizontalGroupBox_2.setGeometry(QtCore.QRect(10, 220, 381, 71))
        self.horizontalGroupBox_2.setObjectName("horizontalGroupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_ingresar = QtWidgets.QPushButton(self.horizontalGroupBox_2)
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.horizontalLayout_2.addWidget(self.btn_ingresar)
        self.btn_limpiar = QtWidgets.QPushButton(self.horizontalGroupBox_2)
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.horizontalLayout_2.addWidget(self.btn_limpiar)
        self.btn_cancelar = QtWidgets.QPushButton(self.horizontalGroupBox_2)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_2.addWidget(self.btn_cancelar)
        self.lbl_logo = QtWidgets.QLabel(self)
        self.lbl_logo.setGeometry(QtCore.QRect(230, 20, 171, 51))
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("resource/image/logo_ferremax.jpg"))
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setObjectName("lbl_logo")
        self.lbl_icono_usuario = QtWidgets.QLabel(self)
        self.lbl_icono_usuario.setGeometry(QtCore.QRect(270, 70, 131, 131))
        self.lbl_icono_usuario.setText("")
        self.lbl_icono_usuario.setPixmap(QtGui.QPixmap("resource/image/vendedora.png"))
        self.lbl_icono_usuario.setScaledContents(True)
        self.lbl_icono_usuario.setObjectName("lbl_icono_usuario")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_7.setText(_translate("self", "Control de Acceso"))
        self.gridGroupBox_3.setTitle(_translate("self", "Credenciales:"))
        self.cbx_cargo.setItemText(0, _translate("self", "Administrador"))
        self.cbx_cargo.setItemText(1, _translate("self", "Cajera"))
        self.cbx_cargo.setItemText(2, _translate("self", "Vendedor"))
        self.label_8.setText(_translate("self", "Usuario:"))
        self.label_9.setText(_translate("self", "Contraseña:"))
        self.label_10.setText(_translate("self", "Cargo:"))
        self.horizontalGroupBox_2.setTitle(_translate("self", "Acciones:"))
        self.btn_ingresar.setText(_translate("self", "Ingresar"))
        self.btn_limpiar.setText(_translate("self", "Limpiar"))
        self.btn_cancelar.setText(_translate("self", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login_frm()
    login.show()
    sys.exit(app.exec_())
