import xml.etree.cElementTree as ET
from procesar import Proceso_Archivo
class Archivo_Salida:
    def __init__(self, nuevo_archivo):
       self.nuevo_archivo = nuevo_archivo
    def Creacion_archivo(self):
        print("Creación del archivo de salida---")

        root = ET.Element("root")
        doc = ET.SubElement(root, "doc")
        nodo1 = ET.SubElement(doc, "nodo1", name="nodo")
        nodo1.text = "Texto de nodo1"
        ET.SubElement(doc, "nodo2", atributo="algo").text = "texto 2"
        arbol = ET.ElementTree(root)

        salida_archivo = input('Ingrese la ruta para guardar su archivo de salida: ')
        arbol.write(salida_archivo)

        print("Archivo de salida creado con éxito!!!!!")