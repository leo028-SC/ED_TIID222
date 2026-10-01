# 1. Crear una pila vacía
pila = []

# 2. Agregar elementos (Push)
pila.append("Plato 1")
pila.append("Plato 2")
pila.append("Plato 3")

print("Pila actual:", pila) 
# Resultado: ['Plato 1', 'Plato 2', 'Plato 3']

# 3. Consultar el elemento en la cima (sin eliminarlo)
cima = pila[-1]
print("Elemento en la cima:", cima) 
# Resultado: Plato 3

# 4. Sacar elementos (Pop)
ultimo_plato = pila.pop()
print("Se quitó:", ultimo_plato) 
# Resultado: Se quitó: Plato 3

print("Pila restante:", pila) 
# Resultado: ['Plato 1', 'Plato 2']