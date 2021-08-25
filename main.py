from lista import lista
from archivo import Archivo
from xml.dom import minidom
import xml.etree.cElementTree as ET

x = True

while x:
    print("Seccione una de las opciones siguientes: ")
    opcion = int(input("1. Cargar archivo \n2. Procesar archivo \n3. Escribir archivo de salida \n4. Mostrar datos del estudiante \n5. Generar grafica \n6. Salir \n"))
    
    if opcion == 1:
        print(" ...Abriendo el archivo \n")
        Archivo.leer_archivo(Archivo)
    elif opcion == 2:
        print("...Procesamiento de su archivo \n")

        #entry = lista() # llamo a la lista a ser ejecutada
        #entry.agregar_enfrente(5) 
        #entry.agregaral_final(8) 
        #entry.agregar_enfrente(9) 
        #entry.mostrar_lista() 
        
    elif opcion == 3:
        root = ET.Element("root")
        doc = ET.SubElement(root, "doc")
        nodo1 = ET.SubElement(doc, "nodo1", name="nodo")
        nodo1.text = "Texto de nodo1"
        ET.SubElement(doc, "nodo2", atributo="algo").text = "texto 2"
        arbol = ET.ElementTree(root)

        salida_archivo = input('Ingrese la ruta para guardar su archivo de salida: ')
        arbol.write(salida_archivo)

    elif opcion == 4:

        print("Datos del creador\n")
        print("*----------------------------------------------------------------*")
        print("--- André Valentín Méndez Cárdenas ---")
        print("--- Carnet: 201801399 ---")
        print("--- Introducción a la Programación y Computación 2 sección 'A' ---")
        print("--- Ingenieria en Ciencias y Sistemas ---")
        print("--- 4to Semestre ---")
        print("*----------------------------------------------------------------*")

    elif opcion == 5:
        print(" ")
    elif opcion == 6:
        print("Saliendo del programa...")
        x = False