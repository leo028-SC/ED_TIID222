while True:
    cola = []
    opcion = 0

    while opcion != 4:
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            numero = int(input("Escribe un número: "))
            cola.append(numero)
        elif opcion == 2:
            if len(cola) > 0:
                cola.pop(0)
            else:
                print("La cola está vacía")
        elif opcion == 3:
            print(cola)

    repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").lower()
    if repetir != "s":
        print("Fin del programa. ¡Hasta luego!")
        break