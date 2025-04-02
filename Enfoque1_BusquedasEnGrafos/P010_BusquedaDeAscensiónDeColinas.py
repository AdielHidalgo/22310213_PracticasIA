import random

def hill_climbing(graph, start, goal):
    """
    Implementación de Búsqueda de Ascensión de Colinas en un grafo.
    
    Parameters:
    graph: Diccionario representando el grafo con heurísticas.
    start: Nodo inicial.
    goal: Nodo objetivo.
    
    Returns:
    Ruta encontrada o None si se queda atrapado en un óptimo local.
    """
    current = start
    path = [current]
    
    while current != goal:
        neighbors = graph[current]['neighbors']
        
        if not neighbors:
            print("Se quedó atrapado en un óptimo local.")
            return None
        
        # Selecciona el vecino con la mejor heurística (mayor valor)
        best_neighbor = max(neighbors, key=lambda n: graph[n]['heuristic'])
        
        # Si el mejor vecino no mejora, detener la búsqueda
        if graph[best_neighbor]['heuristic'] <= graph[current]['heuristic']:
            print("No hay mejor opción, detenido en un óptimo local.")
            return None
        
        current = best_neighbor
        path.append(current)
    
    return path

# Definir un grafo con heurísticas asociadas a cada nodo
graph = {
    'A': {'heuristic': 10, 'neighbors': ['B', 'C']},
    'B': {'heuristic': 8, 'neighbors': ['D', 'E']},
    'C': {'heuristic': 7, 'neighbors': ['F']},
    'D': {'heuristic': 6, 'neighbors': []},
    'E': {'heuristic': 9, 'neighbors': ['G']},
    'F': {'heuristic': 5, 'neighbors': []},
    'G': {'heuristic': 12, 'neighbors': ['H']},
    'H': {'heuristic': 15, 'neighbors': []}  # Nodo objetivo
}

start_node = 'A'
goal_node = 'H'
path = hill_climbing(graph, start_node, goal_node)

if path:
    print("Ruta encontrada:", " -> ".join(path))
