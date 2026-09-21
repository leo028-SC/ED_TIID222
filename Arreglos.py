""" #Declarando un arreglo
numeros = [10,20,30,40,50]

#Imprimiendo un elemento específico del arreglo
print(numeros[2])

#Reasignando un valor a un elemento específico del arreglo
numeros[3] =35 
print(numeros)

#Agregando un elemento al final del arreglo
numeros.append(60)
print(numeros)

#Eliminando un elemento específico del arreglo
numeros.remove(35)
print(numeros)

#Eliminando un elemento en una posición específica del arreglo
numeros.pop(4)
print(numeros)

#Declarando un arreglo de frutas
Frutas = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "platano"]

#Imprimiendo un elemento específico del arreglo
Frutas.pop(4)
print(Frutas)

#Eliminando un elemento específico del arreglo
Frutas.remove("Manzana")
print(Frutas)

#Declarar arreglo vacio
arreglo = []
print(arreglo)

#Creamos una variable para saber de que tamaño queremos el arreglo
n = int(input("Ingrese el tamaño del arreglo: "))
print(n)
#Se hace un ciclo para llenar el arreglo
for i in range(n):
    dato = int(input("Ingrese un numero: "))
    arreglo.append(dato)
print(arreglo)

n = int(input("Ingrese el tamaño del arreglo: "))
arreglo = [0] * n 
for i in range (n): 
    dato = int(input("Ingrese un numero: ")) 
    arreglo [i] = dato
    print(arreglo)
""" 
#Escribe un programa que rellene un array de 15 elementos con números enteros comprendidos entre o y 500 (pedir números). A continuacion. se mostrara el array "Cincurizado" según el siguiente criterio: si el numero que hay en una posicion del array es multiplo de 5, se deja idual y si no se cambia por el siguiente multiplo de 5 que exista a partir de él.
# Declaramos un arreglo vacío
arreglo = []

# Pedimos 15 números

for i in range(15):
    dato = int(input("Ingrese un número entre 0 y 500: "))
    arreglo.append(dato)

print("Array original:")
print(arreglo)


for i in range(15):

    # Si NO es múltiplo de 5
    if arreglo[i] % 5 != 0:

        # Buscamos el siguiente múltiplo de 5
        arreglo[i] = arreglo[i] + (5 - arreglo[i] % 5)

print("Array cincuerizado:")
print(arreglo)