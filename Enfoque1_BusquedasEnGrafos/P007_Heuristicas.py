# Diccionario con las conexiones del grafo (nodo: [(vecino, costo)])
grafo = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 1)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []  # Nodo objetivo
}

# Diccionario con las heurísticas h(n) → estimación desde el nodo hasta G
heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 0
}
def greedy_search(inicio, objetivo):
    # Inicializamos la frontera con el nodo de inicio
    frontera = [(inicio, [inicio])]  # (nodo_actual, camino_recorrido)

    while frontera:
        # Ordenamos la frontera por valor heurístico (menor h(n) al principio)
        frontera.sort(key=lambda x: heuristica[x[0]])
        nodo_actual, camino = frontera.pop(0)  # Tomamos el mejor candidato

        print(f"Visitando nodo: {nodo_actual} con h(n)={heuristica[nodo_actual]}")

        if nodo_actual == objetivo:
            print("¡Objetivo alcanzado!")
            return camino  # Regresamos el camino completo al objetivo

        # Expandimos nodos vecinos
        for vecino, _ in grafo[nodo_actual]:
            if vecino not in camino:  # Evitamos ciclos
                nueva_ruta = camino + [vecino]
                frontera.append((vecino, nueva_ruta))

    return None  # Si no se encuentra el objetivo
camino = greedy_search('A', 'G')
print("\nCamino encontrado:", camino)
