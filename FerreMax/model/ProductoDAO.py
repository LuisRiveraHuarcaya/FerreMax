import sys
import os

#Codigo para que VSCode acepte la ruta para Ejecutar
myDir = os.getcwd()
sys.path.append(myDir)

#Establece ruta relativa, para acceder a los paquetes
sys.path.append("../")

from database.Conexion import Conexion
from model.Proveedores import Proveedores
from model.Categoria import Categoria
class ProductoDao():
    #Tenemos que exportar Clase Conexion del paquete : Controlador
    def __init__(self):
        self.conexion = Conexion()
        self.mod_proveedor = Proveedores()
        self.mod_categoria = Categoria()
    def listar(self):
        self.sql = """  Select codigo,p.nombre,c.nombre,precio_compra,
        pv.nombre,precio_venta,stock 
        from Producto p inner join Categoria c ON p.id_categoria = c.id 
        inner join Proveedor pv ON pv.ruc = p.ruc_proveedor"""

        con = self.conexion.conectar()
        cursor = con.cursor()
        cursor.execute(self.sql)
        result = cursor.fetchall()
        cursor.close()
        con.close()
        return result
    def crearProducto(self,cod,nombre,id_categoria,pc,ruc_prov,pv,stock):
        con = self.conexion.conectar()
        cursor = con.cursor()

        ruc_prov = self.mod_proveedor.getID_proveedor(ruc_prov)
        id_categoria = int(id_categoria) + 1
        #id_categoria = self.mod_categoria.getID_categoria(id_categoria)
        print("Ruc provedor -->",ruc_prov)
        sql = "INSERT INTO Producto values(?,?,?,?,?,?,?)"#.format(cod,nombre,precio_compra,precio_venta,int(stock),ruc_prov,int(id_categoria))
        #sql = "INSERT INTO Producto values ({},{},{},{},{},{},{})".format(cod,nombre,id_categoria,pc,ruc_prov,pv,stock)
        cursor.execute(sql,cod,nombre,id_categoria,pc,ruc_prov,pv,stock)
        #cursor.execute(sql)
        con.commit()
        cursor.close()
        con.close()

    def modificarProducto(self,cod,nombre,id_categoria,pc,ruc_prov,pv,stock):

        ruc_prov = self.mod_proveedor.getID_proveedor(ruc_prov)
        print("RUC prov Modificador",ruc_prov)
        id_categoria = int(id_categoria) + 1

        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = """UPDATE Producto SET nombre=?, id_categoria=?, precio_compra=?,
        ruc_proveedor=?,precio_venta=?, stock=? WHERE codigo=?"""
        cursor.execute(sql,nombre,id_categoria,pc,ruc_prov,pv,stock,cod)
        con.commit()
        cursor.close()
        con.close()
    def eliminarProducto(self,cod):
        con = self.conexion.conectar()
        cursor = con.cursor()
        sql = "Delete from Producto where codigo =?"
        cursor.execute(sql,cod)
        con.commit()
        cursor.close()
        con.close()