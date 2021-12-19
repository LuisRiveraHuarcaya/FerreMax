import pyodbc

class Conexion():

    def conectar(self):
        self.server = 'localhost'
        self.usuario = 'sa' #Ingresar un usuario
        self.contrasena = '' #Ingresar Password
        self.bd='FerreMax'
        
        try:
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};\
            SERVER='+ self.server+';DATABASE='+self.bd+';UID='+self.usuario+';PWD='+self.contrasena)

        except:
            print ('error al conectarse')
        return conexion
