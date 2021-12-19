import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from view.frm_productos import Productos_frm
from PyQt5 import QtCore, QtWidgets
from model.ProductoDAO import ProductoDao
from model.Roles import Roles
from model.Proveedores import Proveedores
from model.Categoria import Categoria

class Productos_Controller():

    def __init__(self):
        self.producto_dao = ProductoDao()
        self.widget = QtWidgets.QWidget()
        self.productos_frm = Productos_frm()
        self.productos_frm.setupUi(self.widget)

        self.mod_proveedor = Proveedores()
        self.mod_categoria = Categoria()

        self.setEvents()
    def mostrar(self):
        #Validar los permisos antes de mostrar, RESTRICCIONES DE USUARIO
        self.setPermisos()
        self.productos_frm.txt_codigo.setEnabled(False)
        self.cargarProveedores() #Carga los proveedores cada ves que es visible
        self.cargarCategorias()
        self.widget.show()

    def ocultar(self):
        self.widget.hide()

    def setPermisos(self):
        #Verifica permisos Lectura o Escritura
        if Roles.Productos == 1:  # Permisos de Lectura
            self.productos_frm.gpBox_formulario.setEnabled(False)
            self.productos_frm.btn_insertar_foto.setEnabled(False)
        if Roles.Productos == 2: # Permisos de escritura
            self.productos_frm.gpBox_formulario.setEnabled(True)
    def setEvents(self):
        self.productos_frm.checkBox.stateChanged.connect(self.desbloquearCodigo) #---CBOX_desbloquear_codigo
        self.productos_frm.btn_buscar.clicked.connect(self.buscarProductos) #----btn_buscar
        self.productos_frm.btn_agregar.clicked.connect(self.crearProducto) #-----btn_agregar
        self.productos_frm.btn_modificar.clicked.connect(self.modificarProducto) #----btn_modificar
        self.productos_frm.btn_eliminar.clicked.connect(self.eliminarProducto) #----btn_eliminar
        
        #No permite editar las filas de la tabla
        self.productos_frm.tabla_productos.setEditTriggers (QtWidgets.QAbstractItemView.NoEditTriggers)
        #Selecciona toda la fila de una tabla, sin esta opcion solo selecciona casillas individuales
        self.productos_frm.tabla_productos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.productos_frm.tabla_productos.cellClicked.connect(self.getItemTabla)
    
    def cargarProveedores(self): #Carga los proveedores al ComboBox
        lista = self.mod_proveedor.getNames_proveedor()
        self.productos_frm.cbx_proveedor.clear()  #---Limpia el combobox
        for item in lista:#----Recorre el arreglo con todos los proveedores
            self.productos_frm.cbx_proveedor.addItem(item[0])

    def cargarCategorias(self): #Carga Categorias al ComboBox
        lista = self.mod_categoria.getNames_categorias()
        self.productos_frm.cbx_categoria.clear()  #---Limpia el combobox
        for item in lista:#----Recorre el arreglo con todos los proveedores
            self.productos_frm.cbx_categoria.addItem(item[0])

    def buscarProductos(self):
        #Traer ProductDAO
        productos = self.producto_dao.listar() #--Devuelve result de todos los productos
        self.productos_frm.tabla_productos.setRowCount(0)

        for row_numb , row_data in enumerate(productos):
            self.productos_frm.tabla_productos.insertRow(row_numb)
            for colum_num, data in enumerate(row_data):
                self.productos_frm.tabla_productos.setItem(row_numb,colum_num, QtWidgets.QTableWidgetItem(str(data)))
    def crearProducto(self):
        cod= self.productos_frm.txt_codigo.text()
        nombre = self.productos_frm.txt_nombre.text()
        cat = self.productos_frm.cbx_categoria.currentIndex()
        pc = self.productos_frm.txt_precio_compra.text()
        prov = self.productos_frm.cbx_proveedor.currentText() #Devoler nombre para buscarlo en BD y obtener ruc
        pv = self.productos_frm.txt_precio_venta.text()
        stock = self.productos_frm.txt_stock.text()
        
        #Validar campos vacios antes de Crear producto
        if self.validarCampos(cod,nombre,pc,pv,stock):
            self.producto_dao.crearProducto(cod,nombre,cat,pc,prov,pv,stock) # Modificar esto-----------------------------------
            self.buscarProductos()
            #self.buscarProductos()
        else:
            QtWidgets.QMessageBox.information(self.widget, "Validacion de campos", """Por favor llene todos los campos""",
            QtWidgets.QMessageBox.Ok)

    def eliminarProducto(self):
        cod= self.productos_frm.txt_codigo.text()

        if not cod =="" or cod.isspace():
            self.producto_dao.eliminarProducto(cod)
            self.buscarProductos()
        else:
            QtWidgets.QMessageBox.information(self.widget, "Validacion de campos", """Debe ingresar un Codigo""",
            QtWidgets.QMessageBox.Ok)
    def modificarProducto(self):
        cod= self.productos_frm.txt_codigo.text()
        nombre = self.productos_frm.txt_nombre.text()
        cat = self.productos_frm.cbx_categoria.currentIndex()
        pc = self.productos_frm.txt_precio_compra.text()
        prov = self.productos_frm.cbx_proveedor.currentText() #Devoler nombre para buscarlo en BD y obtener ruc
        pv = self.productos_frm.txt_precio_venta.text()
        stock = self.productos_frm.txt_stock.text()

        #Validar campos vacios antes de Modificar producto
        if self.validarCampos(cod,nombre,pc,pv,stock):
            print(cod,nombre,cat,pc,prov,pv)
            self.producto_dao.modificarProducto(cod,nombre,cat,pc,prov ,pv,stock)
            self.buscarProductos()
        else:
            QtWidgets.QMessageBox.information(self.widget, "Validacion de campos", """Por favor llene todos los campos""",
            QtWidgets.QMessageBox.Ok)

    def validarCampos(self,c,n,pc,pv,st):
        # Validacion de vacios : c==""      Validacion de espacios:  c.isspace()
        if c=="" or n=="" or pc=="" or pv=="" or st=="" or c.isspace() or n.isspace() or pc.isspace() or pv.isspace() or st.isspace():
            return False
        else:
            return True  #---campos ok  
            
    def desbloquearCodigo(self,estado):
        if estado:
            self.productos_frm.txt_codigo.setEnabled(True)
        else:
            self.productos_frm.txt_codigo.setEnabled(False)

    def getItemTabla(self): #Acciona cuando selecciona item tabla
        #Devuelve datos de cada indice de columna 
        cod = self.productos_frm.tabla_productos.selectedIndexes()[0].data()
        nomb = self.productos_frm.tabla_productos.selectedIndexes()[1].data()
        cat = self.productos_frm.tabla_productos.selectedIndexes()[2].data()
        pc = self.productos_frm.tabla_productos.selectedIndexes()[3].data()
        prov = self.productos_frm.tabla_productos.selectedIndexes()[4].data()
        pv = self.productos_frm.tabla_productos.selectedIndexes()[5].data()
        stock = self.productos_frm.tabla_productos.selectedIndexes()[6].data()
        #print("Has clickeado en {} {} {} {} {} {}".format(cod,nomb,cat,pc,prov,pv))

        #Mostrar en TextLine
        self.productos_frm.txt_codigo.setText(cod)
        self.productos_frm.txt_nombre.setText(nomb)
        ic =self.productos_frm.cbx_categoria.findText(cat)
        self.productos_frm.cbx_categoria.setCurrentIndex(ic)
        self.productos_frm.txt_precio_compra.setText(pc)
        ip = self.productos_frm.cbx_proveedor.findText(prov)
        self.productos_frm.cbx_proveedor.setCurrentIndex(ip)
        self.productos_frm.txt_precio_venta.setText(pv)
        self.productos_frm.txt_stock.setText(stock)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Productos_Controller()
    c.productos_frm.show()
    sys.exit(app.exec_())
