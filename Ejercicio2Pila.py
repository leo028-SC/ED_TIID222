while True:
    pila = []
    opcion = 0

    while opcion != 4:
        print("1. Insertar en pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            numero = int(input("Escribe un número: "))
            pila.append(numero)
        elif opcion == 2:
            if len(pila) > 0:
                pila.pop()
            else:
                print("La pila está vacía")
        elif opcion == 3:
            print(pila)

    repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").lower()
    if repetir != "s":
        print("Fin del programa. ¡Hasta luego!")
        break