from xml.dom import minidom
class Archivo:
    def __init__(self, archivo_entrada, mydoc, nombre_terreno, pos_x, pos_y, dimen_x, dimen_y, gaso):
        self.archivoentrada = archivo_entrada
        self.mydoc = mydoc
        self.nombre_terreno = nombre_terreno
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dimen_x = dimen_x
        self.dimen_y = dimen_y
        self.gaso = gaso
    def leer_archivo(self):
        #aqui se solicita la ruta del archivo de entrada
        archivo_entrada = input('Ingrese ruta de su archivo: ')
        mydoc = minidom.parse(archivo_entrada)
        #para obtener los nombres de los terrenos
        nombre_terreno = mydoc.getElementsByTagName('terreno')
        #para obtener las dimensiones del terreno
        dimen_x = mydoc.getElementsByTagName('m')
        dimen_y = mydoc.getElementsByTagName('n')
        #para obtener la posicion inicial del objeto
        pos_x = mydoc.getElementsByTagName('x')
        pos_y = mydoc.getElementsByTagName('y')
        #para obtener las valores de gasolina de cada casilla
        gaso = mydoc.getElementsByTagName('posicion')
        #aqui imprimirá en la consola los atributos de cada objeto existente en el archivo
        for elem in nombre_terreno:
            print(elem.attributes['nombre'].value)
        #muestra la posicion del objeto
        print("Posicion en x")
        for elem in pos_x:
            print(elem.firstChild.data)

        print("Posicion en y")
        for elem in pos_y:
            print(elem.firstChild.data)

        #muestra las dimensiones del terreno
        print("Dimension m")
        for elem in dimen_x:
            print(elem.firstChild.data)

        print("Dimension n")
        for elem in dimen_y:
            print(elem.firstChild.data)

        #muestra el valor de la gasolina
        print("Cantidad de Gasolina")
        for elem in gaso:
            print(elem.firstChild.data)
