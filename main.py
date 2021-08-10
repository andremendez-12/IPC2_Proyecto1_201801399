import time
from io import open

a = True

while a:
    print("Seccione una opcion")
    eleccion = int(input("1. Cargar archivo \n2. Procesar archivo \n3. Escribir archivo de salida \n4. Mostrar datos del estudiante \n5. Generar grafica \n6. Salir \n"))
    if eleccion == 1:
        print(" ...Abriendo el archivo ")

        archivo_nuevo = input("Ingrese la ruta del archivo: ")
        cargar_archivo = open(archivo_nuevo, "r")
        print(cargar_archivo.readlines()) 
        cargar_archivo.close() 

    elif eleccion == 2:
        print(" ")
    elif eleccion == 3:
        print(" ")
    elif eleccion == 4:
        print("*----------------------------------------------------------------*")
        print("--- André Valentín Méndez Cárdenas ---")
        print("--- Carnet: 201801399 ---")
        print("--- Introducción a la Programación y Computación 2 sección 'A' ---")
        print("--- Ingenieria en Ciencias y Sistemas ---")
        print("--- 4to Semestre ---")
        print("*----------------------------------------------------------------*")
    elif eleccion == 5:
        print(eleccion)
    elif eleccion == 6:
        print("Saliendo del programa...")
        time.sleep(3)
        a = False