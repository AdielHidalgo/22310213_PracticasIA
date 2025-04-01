"""
# Diccionario del grafo con conexiones y costos entre nodos
grafo = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 1)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Heurística: estimación del costo desde un nodo hasta el objetivo G
heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 0
}

# Algoritmo A* con explicación paso a paso
def a_estrella(inicio, objetivo):
    # Cada elemento en la frontera es (nodo_actual, camino_recorrido, costo_acumulado g)
    frontera = [(inicio, [inicio], 0)]

    while frontera:
        # Ordenamos por la función f(n) = g(n) + h(n)
        frontera.sort(key=lambda x: x[2] + heuristica[x[0]])
        nodo_actual, camino, costo_actual = frontera.pop(0)

        print(f"Visitando: {nodo_actual} | g={costo_actual} | h={heuristica[nodo_actual]} | f={costo_actual + heuristica[nodo_actual]}")

        if nodo_actual == objetivo:
            print("¡Objetivo alcanzado!")
            return camino, costo_actual

        # Expandimos vecinos
        for vecino, costo in grafo[nodo_actual]:
            if vecino not in camino:  # Evitar ciclos
                nuevo_camino = camino + [vecino]
                nuevo_costo = costo_actual + costo  # g(n) se actualiza
                frontera.append((vecino, nuevo_camino, nuevo_costo))

    print("No se encontró un camino.")
    return None, None
camino, costo = a_estrella('A', 'G')
print("\nCamino encontrado:", camino)
print("Costo total:", costo)
"""

# Estructura del grafo AND-OR
grafo = {
    'A': [('B', 'AND'), ('C', 'OR')],
    'B': [('D', 'LEAF'), ('E', 'LEAF')],
    'C': [('F', 'LEAF')],
    'D': [],
    'E': [],
    'F': []
}

# Costos para cada transición
costos = {
    ('A', 'B'): 1,
    ('A', 'C'): 2,
    ('B', 'D'): 2,
    ('B', 'E'): 2,
    ('C', 'F'): 4
}

# Costos heurísticos iniciales (estimados)
heuristica = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 0,
    'E': 0,
    'F': 0
}

# Nodos ya solucionados
solucionados = {}

# Camino óptimo elegido en cada nodo
padres = {}

# AO* recursivo
def ao_star(nodo):
    print(f"\nEvaluando nodo: {nodo}")

    if nodo in solucionados:
        return heuristica[nodo]

    hijos = grafo[nodo]

    if not hijos:
        solucionados[nodo] = True
        return heuristica[nodo]

    mejor_costo = float('inf')
    mejor_opcion = []

    for hijo, tipo in hijos:
        if tipo == 'LEAF':
            costo_total = heuristica[hijo] + costos.get((nodo, hijo), 0)
            if costo_total < mejor_costo:
                mejor_costo = costo_total
                mejor_opcion = [hijo]
        elif tipo == 'AND':
            subhijos = grafo[hijo]
            total = 0
            for sub, _ in subhijos:
                total += ao_star(sub) + costos.get((hijo, sub), 0)
            total += costos.get((nodo, hijo), 0)
            if total < mejor_costo:
                mejor_costo = total
                mejor_opcion = [sub for sub, _ in subhijos]
        elif tipo == 'OR':
            for sub, _ in grafo[hijo]:
                total = ao_star(sub) + costos.get((hijo, sub), 0) + costos.get((nodo, hijo), 0)
                if total < mejor_costo:
                    mejor_costo = total
                    mejor_opcion = [sub]

    heuristica[nodo] = mejor_costo
    padres[nodo] = mejor_opcion

    # Si todos los hijos están solucionados, marcar como solucionado
    if all(h in solucionados for h in mejor_opcion):
        solucionados[nodo] = True

    return mejor_costo
ao_star('A')
print("\nCamino óptimo elegido:", padres)
