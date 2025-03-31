from collections import deque

def bfs(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([[inicio]])  # Cola con caminos, no solo nodos

    while cola:
        camino = cola.popleft()  # Sacamos el primer camino
        nodo = camino[-1]  # Último nodo del camino

        if nodo == objetivo:
            return camino  # Regresamos el camino si llegamos al objetivo

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None  # Si no se encuentra el objetivo

# Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Prueba del algoritmo
inicio = 'A'
objetivo = 'F'
resultado = bfs(grafo, inicio, objetivo)

print("Camino encontrado:", resultado)
