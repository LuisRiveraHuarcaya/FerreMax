------------------------BASE DATOS NUEVA------------------------
use master
go

--Validar la existencia de la base de datos
if exists(Select name from sys.databases where name='FerreMax')
	Begin
		Drop Database FerreMax --Eliminar(Drop)
	End
go
Create database FerreMax
go

use FerreMax
go

Create Table Area(
	id int primary key,
	nombre varchar(120)
)
Create Table Rol(
	id int primary key,
	nombre varchar(120)
)

Create Table Permisos(
	id_rol int not null,
	id_area int not null,
	permiso int
)

Alter table Permisos add 
constraint fk_permisos_id_rol foreign key(id_rol) 
references Rol(id)

Alter table Permisos add 
constraint fk_permisos_id_area foreign key(id_area) 
references Area(id)

Alter table Permisos add 
constraint pk_permisos primary key(id_rol,id_area)

Create Table Empleado(
	dni char(8) primary key,
	nombres varchar(100),
	apellidos varchar(100),
	sexo char(1),
	fecha_nacimiento date,
	telefono varchar(12),
	email varchar(100),
	usuario varchar(80),
	password varchar(120),
	id_rol int
)

Alter table Empleado add 
constraint fk_empleado_id_rol foreign key(id_rol) 
references Rol(id)

Create Table Cliente(
	dni char(8) primary key,
	nombre varchar(100),
	apellidos varchar(100),
	telefono varchar(12),
	direccion varchar(200),
)

Create table Categoria(
	id int primary key,
	nombre varchar(80),
)
Create table Proveedor(
	ruc char(10) primary key,
	nombre varchar(120),
	email varchar(100),
	telefono varchar(12),
	direccion varchar(200)
)

Create table Producto(
	codigo char(4) primary key,
	nombre varchar(120),
	id_categoria int,
	precio_compra decimal(10,2),
	ruc_proveedor char(10),
	precio_venta decimal(10,2),
	stock int,
)

Alter table Producto add 
constraint fk_producto_id_prov foreign key(ruc_proveedor) 
references Proveedor(ruc)
----
Alter table Producto add 
constraint fk_producto_id_cat foreign key(id_categoria) 
references Categoria(id)

Create table Venta(
	id int primary key,
	dni_cliente char(8),
	dni_empleado char(8),
	fecha date,
	total decimal(10,2)
)

Alter table Venta add
constraint fk_dventa_dni_cliente foreign key(dni_cliente) references Cliente(dni)

Alter table Venta add
constraint fk_dventa_dni_empleado foreign key(dni_empleado) references Empleado(dni)

Create table Detalle_Venta(
	id_venta int not null,
	codigo_producto char(4) not null,
	cantidad int,
	sub_total decimal(10,2)
)

Alter table Detalle_Venta add 
constraint fk_dventa_id_venta foreign key(id_venta) 
references Venta(id)

Alter table Detalle_Venta add 
constraint fk_dventa_cod_produc foreign key(codigo_producto) 
references Producto(codigo)

Alter table Detalle_Venta add
constraint pk_dventa_venta_producto primary key(id_venta,codigo_producto)

Create table Compra(
	id int primary key,
	ruc_proveedor char(10),
	dni_empleado char(8),
	fecha date,
	total decimal(10,2)
)

Alter table Compra add
constraint fk_dcompra_ruc_proveedor foreign key(ruc_proveedor) references Proveedor(ruc)

Alter table Compra add
constraint fk_dcompra_dni_empleado foreign key(dni_empleado) references Empleado(dni)

Create table Detalle_Compra(
	id_compra int not null,
	codigo_producto char(4) not null,
	cantidad int,
	sub_total decimal(10,2)
)

Alter table Detalle_Compra add 
constraint fk_dcompra_id_venta foreign key(id_compra) 
references Compra(id)

Alter table Detalle_Compra add 
constraint fk_dcompra_cod_produc foreign key(codigo_producto) 
references Producto(codigo)

Alter table Detalle_Compra add 
constraint pk_dcompra primary key(id_compra,codigo_producto)


----------INSERTS------

--Categoria----
Insert into Categoria values(1,'Herramienta')
Insert into Categoria values(2,'Accesorio')
Insert into Categoria values(3,'Carpinteria')
Insert into Categoria values(4,'Electricidad')
Insert into Categoria values(5,'Pintura')
Insert into Categoria values(6,'Cemento')


----Area---
Insert into Area values(1,'Clientes')
Insert into Area values(2,'Empleados')
Insert into Area values(3,'Proveedores')
Insert into Area values(4,'Productos')
Insert into Area values(5,'Almacen')
Insert into Area values(6,'Ventas')
Insert into Area values(7,'Mantenimiento')

---Rol---
Insert into Rol values(1,'Administrador')
Insert into Rol values(2,'Vendedor')

----Permiso---
Insert into Permisos values(1,1,2)---Permisos para ADMIN
Insert into Permisos values(1,2,2)
Insert into Permisos values(1,3,2)
Insert into Permisos values(1,4,2)
Insert into Permisos values(1,5,2)
Insert into Permisos values(1,6,2)
Insert into Permisos values(1,7,2)

Insert into Permisos values(2,1,1) ---Permiso para VENDEDOR
Insert into Permisos values(2,4,1)

--Proveedor---
Insert into Proveedor values('RUC0000001','Aceros Arequipa SA','aceros@arequipa.com.pe','1111111','calle 1')
Insert into Proveedor values('RUC0000002','Cementos del Peru','cementos@peru.pe','2222222','calle 2')
Insert into Proveedor values('RUC0000003','Tuberias PAVCO','pavco@tuberias.com','3333333','calle 3')
Insert into Proveedor values('RUC0000004','Distribuidora MAX','max@distribuidora.com','4444444','calle 4')

----Cliente---
Insert into Cliente values('11111111','Esmeralda','Torres','987654321','Av. Peru calle 12')
Insert into Cliente values('22222222','Julio','Arias','933125984','Av. Nueva calle 6')

---Creando usuario ADMIN
Insert into Empleado values('88888888','Luis Eduardo','Rivera Huarcaya','M','2021-12-1','987654321','luis@gmail.com','luis','123',1)
---Creando usuario VENDEDOR
Insert into Empleado values('77777777','Maria','Ferrero','F','2012-08-06','7654321','maria@gmail.com','maria','123',2)

--Producto--
Insert into Producto values('P001','Cemento Andino 15kg',6,18.99,'RUC0000002',22.99,12)
Insert into Producto values('P002','Pintura CPP color blanco',5,15.99,'RUC0000004',18.99,7)

Select r.nombre, a.nombre, permiso 
        from Permisos per INNER JOIN Area a ON per.id_area = a.id
        INNER JOIN Rol r ON r.id = per.id_rol

Select * from Empleado