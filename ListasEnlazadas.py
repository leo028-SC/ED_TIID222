class Nodo:

    def __init__(self, numero):

        self.numero = numero

        self.siguiente = None

# Clase que va a administrar todos los nodos de las listasenlazadas
class ListaEnlazada:

    def __init__(self):

        self.cabeza = None

    def Insertar_Nodo_al_inicio(self, numero):

        nuevo_nodo = Nodo(numero)

        # Comprobar si la lista esta vacia
        if self.cabeza is None:

            # vamos a pasar el nuevo nodo en nuestra cabeza
            self.cabeza = nuevo_nodo

            return

        # si la lista tiene nodos el nuevo nodo apunta a lo que era la cabeza 
        nuevo_nodo.siguiente = self.cabeza

        # Actualiza nuestra cabeza para que apunte al nuevo nodo
        self.cabeza = nuevo_nodo

    # Metodo para insertar un nodo al final de la lista
    def Insertar_Nodo_al_final(self, numero):

        # Crear el nodo para el numero que se recibe       
        nuevo_nodo = Nodo(numero)

        # comprobar si la lista esta vacia
        if self.cabeza is None:

            # si la lista esta vacia el nuevo nodo sera el primero
            self.cabeza = nuevo_nodo

            return

        # referencia temporal al primer nodo
        actual = self.cabeza

        while actual.siguiente:

            actual = actual.siguiente

        # Cuando ya no hay siguiente, conecta al nuevo nodo
        actual.siguiente = nuevo_nodo

    def imprimir_ListaEnlazada(self):

        actual = self.cabeza

        while actual:
            # con esta linea imprimimos nuestro nodo sin saltos de linea
            print(actual.numero, "-> ", end="")

            # Avanzamos al siguiente nodo y ahora este sera el actual
            actual = actual.siguiente

        # Sino apunta al none
        print("None")


Mi_lista = ListaEnlazada()
Mi_lista.Insertar_Nodo_al_inicio(2)
Mi_lista.Insertar_Nodo_al_inicio(1)
Mi_lista.Insertar_Nodo_al_final(56)
Mi_lista.imprimir_ListaEnlazada()
