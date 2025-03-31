from collections import deque  # Importamos deque para usar una cola eficiente (FIFO)

def bfs(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para llevar registro de los nodos ya visitados
    cola = deque([[inicio]])  # Creamos la cola con una lista que contiene solo el nodo inicial

    while cola:  # Mientras haya caminos por explorar en la cola
        camino = cola.popleft()  # Sacamos el primer camino de la cola (FIFO)
        nodo = camino[-1]  # Tomamos el último nodo del camino (el nodo actual)

        if nodo == objetivo:
            return camino  # Si llegamos al objetivo, regresamos el camino completo

        if nodo not in visitados:  # Si no hemos visitado este nodo
            visitados.add(nodo)  # Lo marcamos como visitado

            # Recorremos todos los vecinos del nodo actual
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)  # Copiamos el camino actual
                nuevo_camino.append(vecino)  # Añadimos el vecino al nuevo camino
                cola.append(nuevo_camino)  # Guardamos este nuevo camino en la cola

    return None  # Si terminamos el ciclo sin encontrar el objetivo, regresamos None

# Definimos un grafo como diccionario de listas (adyacencias)
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Datos de entrada para la búsqueda
inicio = 'A'
objetivo = 'F'

# Ejecutamos la función BFS
resultado = bfs(grafo, inicio, objetivo)

# Mostramos el camino encontrado
print("Camino encontrado:", resultado)
