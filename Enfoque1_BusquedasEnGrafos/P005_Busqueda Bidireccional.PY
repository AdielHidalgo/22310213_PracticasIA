import matplotlib.pyplot as plt
import networkx as nx

# Definimos el grafo como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Creamos el grafo dirigido
G = nx.DiGraph()

# Agregamos las aristas (conexiones entre nodos)
for nodo, vecinos in grafo.items():
    for vecino in vecinos:
        G.add_edge(nodo, vecino)

# Dibujamos el grafo
plt.figure(figsize=(5, 2))
pos = nx.spring_layout(G, seed=42)  # Posiciones consistentes

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='skyblue',
    node_size=2000,
    font_size=16,
    font_weight='bold',
    arrows=True
)

plt.title("Grafo usado en Búsqueda Bidireccional", fontsize=14)
plt.show()

from collections import deque

def bidirectional_search(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]

    # Colas para las búsquedas desde ambos extremos
    cola_inicio = deque([[inicio]])
    cola_objetivo = deque([[objetivo]])

    # Visitados desde ambos extremos
    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}

    while cola_inicio and cola_objetivo:
        # Expandimos desde el inicio
        camino_inicio = cola_inicio.popleft()
        nodo_inicio = camino_inicio[-1]

        for vecino in grafo.get(nodo_inicio, []):
            if vecino not in visitados_inicio:
                nuevo_camino = list(camino_inicio)
                nuevo_camino.append(vecino)
                visitados_inicio[vecino] = nuevo_camino
                cola_inicio.append(nuevo_camino)

                if vecino in visitados_objetivo:
                    # Encontramos punto de encuentro
                    return nuevo_camino + visitados_objetivo[vecino][-2::-1]

        # Expandimos desde el objetivo (buscando al revés)
        camino_objetivo = cola_objetivo.popleft()
        nodo_objetivo = camino_objetivo[-1]

        for vecino in grafo:
            if nodo_objetivo in grafo[vecino]:  # Invertimos búsqueda
                if vecino not in visitados_objetivo:
                    nuevo_camino = list(camino_objetivo)
                    nuevo_camino.append(vecino)
                    visitados_objetivo[vecino] = nuevo_camino
                    cola_objetivo.append(nuevo_camino)

                    if vecino in visitados_inicio:
                        return visitados_inicio[vecino] + nuevo_camino[-2::-1]

    return None  # Si no hay conexión

# Prueba con el mismo grafo
camino_bidir = bidirectional_search(grafo, 'A', 'F')
print("Camino encontrado:", camino_bidir)
