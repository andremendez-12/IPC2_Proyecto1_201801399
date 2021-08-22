from io import open
from xml.dom import minidom

x = True

while x:
    print("Seccione una de las opciones siguientes: ")
    opcion = int(input("1. Cargar archivo \n2. Procesar archivo \n3. Escribir archivo de salida \n4. Mostrar datos del estudiante \n5. Generar grafica \n6. Salir \n"))
    if opcion == 1:
        print(" ...Abriendo el archivo \n")

        #archivo_nuevo = input("Ingrese la ruta del archivo: ")
        #cargar_archivo = open(archivo_nuevo, "r")
        #print(cargar_archivo.readlines()) 

        mydoc = minidom.parse('datos.xml')
        campos = mydoc.getElementsByTagName('terreno')

        for elem in campos:
            print(elem.attributes['nombre'].value)
            print('\n')

    elif opcion == 2:
        print(" ")
    elif opcion == 3:
        print(" ")
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