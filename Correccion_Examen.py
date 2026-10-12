matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 3]
]

matriz.append([39, 22, 69, 17])  # Agregar una nueva fila con ceros
print(matriz)
print(matriz[1])

for i in matriz:
    if 61 in i:
        print(f"El número 61 se encuentra en la fila {i}")
        break

    for filas in matriz:
        for numeros in filas:
            if numeros == 3:
                print(f"El número 3 se encuentra en la fila {filas}")
                break


numeros = [10, 20, 30, 40, 50]
numeros.append([60, 70])
print(numeros[5])

numeros = [10, 20, 30, 40]
numeros.insert(2, 25)
print(numeros)


print("Pila actual:", pila)  # [10, 20, 30]
desempilar = pila.pop()
print("Pila después del pop:", pila)