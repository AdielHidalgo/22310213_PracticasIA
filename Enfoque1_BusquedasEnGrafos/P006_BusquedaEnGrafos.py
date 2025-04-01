grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

from collections import deque

def busqueda_en_grafo(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para evitar visitar nodos repetidos
    cola = deque([[inicio]])  # Cola con caminos a explorar

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == objetivo:
            return camino  # Camino encontrado

        if nodo not in visitados:
            visitados.add(nodo)  # Marcamos como visitado

            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None  # Si no se encuentra camino

camino = busqueda_en_grafo(grafo, 'A', 'F')
print("Camino encontrado:", camino)