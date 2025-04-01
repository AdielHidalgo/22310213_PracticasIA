# Diccionario del grafo con sus conexiones y costos
grafo = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 1)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Diccionario con la heurística de cada nodo
heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 0
}

# Función para la búsqueda Voraz (Greedy Best-First Search)
def voraz_primero_el_mejor(inicio, objetivo):
    frontera = [(inicio, [inicio])]  # Lista de tuplas: (nodo_actual, camino_recorrido)
    visitados = set()  # Para evitar visitar un nodo dos veces

    while frontera:
        # Ordenamos por la heurística (menor primero)
        frontera.sort(key=lambda x: heuristica[x[0]])
        nodo_actual, camino = frontera.pop(0)

        print(f"Visitando: {nodo_actual} (h={heuristica[nodo_actual]})")

        if nodo_actual == objetivo:
            print("¡Objetivo alcanzado!")
            return camino

        visitados.add(nodo_actual)

        # Expandimos nodos vecinos
        for vecino, _ in grafo[nodo_actual]:
            if vecino not in visitados and vecino not in [n for n, _ in frontera]:
                nueva_ruta = camino + [vecino]
                frontera.append((vecino, nueva_ruta))

    print("No se encontró un camino.")
    return None

camino = voraz_primero_el_mejor('A', 'G')
print("\nCamino encontrado:", camino)
