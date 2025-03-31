import heapq  # Importamos la librería heapq, que permite usar una cola de prioridad (min-heap)

def ucs(grafo, inicio, objetivo):
    cola = [(0, [inicio])]  # Cola de prioridad que almacenará los caminos con su costo acumulado
    visitados = set() # Conjunto que guarda los nodos visitados para no procesarlos dos veces

    while cola:
        costo_actual, camino = heapq.heappop(cola)  # Sacamos el camino de menor costo de la cola
        nodo = camino[-1]   # El nodo actual es el último en el camino

        if nodo == objetivo:
            return camino, costo_actual  # Si hemos llegado al objetivo, devolvemos el camino y su costo

        if nodo not in visitados:
            visitados.add(nodo) # Marcamos el nodo como visitado para no procesarlo de nuevo

            for vecino, costo in grafo.get(nodo, []): # Iteramos sobre los vecinos del nodo actual
                if vecino not in visitados: 
                    nuevo_camino = list(camino) # Creamos una nueva lista del camino actual
                    nuevo_camino.append(vecino) # Agregamos el vecino al nuevo camino
                    nuevo_costo = costo_actual + costo # Calculamos el nuevo costo acumulado
                    heapq.heappush(cola, (nuevo_costo, nuevo_camino)) # Agregamos el nuevo camino a la cola

    return None, float('inf')  # Si no encontramos un camino, retornamos None y costo infinito

# Grafo con pesos (costo entre nodos)
grafo_con_costos = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Ejecutamos UCS
inicio = 'A'
objetivo = 'F'
camino, costo = ucs(grafo_con_costos, inicio, objetivo)

print("Camino encontrado:", camino)
print("Costo total:", costo)
