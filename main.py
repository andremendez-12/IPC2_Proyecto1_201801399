from lista import lista
from archivo import Archivo
from procesar import Proceso_Archivo
from arcSalida import Archivo_Salida
from xml.dom import minidom
import xml.etree.cElementTree as ET

x = True

while x:
    print("---------------MENU PROGRAM 1.0-----------------")
    print("Seccione una de las opciones siguientes: ")
    opcion = int(input("1. Cargar archivo \n2. Procesar archivo \n3. Escribir archivo de salida \n4. Mostrar datos del estudiante \n5. Generar grafica \n6. Salir \n"))
    
    if opcion == 1:
        print("...Abriendo el archivo \n")
        Archivo.leer_archivo(Archivo)

    elif opcion == 2:
        print("...Procesamiento de su archivo \n")
        Proceso_Archivo.Lectura_terreno(Proceso_Archivo)
        
    elif opcion == 3:
        print("...Creando Archivo de Salida \n")
        Archivo_Salida.Creacion_archivo(Archivo_Salida)

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
        print("...Generando gráfica solución")
        
    elif opcion == 6:
        print("Saliendo del programa...")
        x = False