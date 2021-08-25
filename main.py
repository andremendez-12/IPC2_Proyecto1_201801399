from io import open
from lista import lista
from xml.dom import minidom

x = True

while x:
    print("Seccione una de las opciones siguientes: ")
    opcion = int(input("1. Cargar archivo \n2. Procesar archivo \n3. Escribir archivo de salida \n4. Mostrar datos del estudiante \n5. Generar grafica \n6. Salir \n"))
    
    if opcion == 1:
        print(" ...Abriendo el archivo \n")
        #aqui se solicita la ruta del archivo de entrada
        archivo_entrada = input('Ingrese ruta de su archivo: ')
        mydoc = minidom.parse(archivo_entrada)
        campos = mydoc.getElementsByTagName('terreno')
        #aqui imprimirá en la consola los atributos de cada objeto existente en el archivo
        for elem in campos:
            print(elem.attributes['nombre'].value)

    elif opcion == 2:
        s = lista() # llamo a la lista a ser ejecutada
        s.agregar_enfrente(5) 
        s.agregaral_final(8) 
        s.agregar_enfrente(9) 

        s.mostrar_lista() 
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