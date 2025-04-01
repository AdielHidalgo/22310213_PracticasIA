grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Función de búsqueda en profundidad limitada
def dls(grafo, nodo, objetivo, limite, camino):
    camino.append(nodo)  # Añadimos el nodo actual al camino

    if nodo == objetivo:
        return True  # Si encontramos el objetivo, detenemos

    if limite <= 0:
        camino.pop()  # Retiramos el nodo si no llegamos y ya no hay profundidad
        return False

    for vecino in grafo.get(nodo, []):
        if dls(grafo, vecino, objetivo, limite - 1, camino):
            return True

    camino.pop()  # Retrocedemos si no hay camino válido desde aquí
    return False

# Función de búsqueda en profundidad iterativa
def ids(grafo, inicio, objetivo, max_prof=10):
    for limite in range(max_prof + 1):  # Probamos diferentes profundidades
        camino = []
        if dls(grafo, inicio, objetivo, limite, camino):
            return camino  # Si se encuentra el objetivo, regresamos el camino
    return None  # Si no se encuentra

# Prueba
inicio = 'A'
objetivo = 'F'
camino_encontrado = ids(grafo, inicio, objetivo, max_prof=5)

print("Camino encontrado:", camino_encontrado)

