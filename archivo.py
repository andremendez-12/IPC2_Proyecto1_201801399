from xml.dom import minidom
class Archivo:
    def __init__(self, archivo_entrada, mydoc, nombre_terreno):
        self.archivoentrada = archivo_entrada
        self.mydoc = mydoc
        self.nombre_terreno = nombre_terreno
    def leer_archivo(self):
        #aqui se solicita la ruta del archivo de entrada
        archivo_entrada = input('Ingrese ruta de su archivo: ')
        mydoc = minidom.parse(archivo_entrada)
        nombre_terreno = mydoc.getElementsByTagName('terreno')
        #aqui imprimirá en la consola los atributos de cada objeto existente en el archivo
        for elem in nombre_terreno:
            print(elem.attributes['nombre'].value)