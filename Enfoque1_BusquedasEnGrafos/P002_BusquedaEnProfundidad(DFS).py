grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(grafo, inicio, objetivo, visitados=None, camino=None):
    """
    Implementación de DFS (Depth-First Search) para buscar un camino desde 'inicio' hasta 'objetivo'.
    
    Args:
        grafo (dict): Diccionario que representa el grafo.
        inicio (str): Nodo inicial de la búsqueda.
        objetivo (str): Nodo objetivo a encontrar.
        visitados (set): Conjunto de nodos ya visitados (para evitar ciclos).
        camino (list): Camino actual desde el inicio hasta el nodo explorado.
    
    Returns:
        list: Camino desde 'inicio' hasta 'objetivo', o None si no existe.
    """
    
    # Inicializar conjuntos y listas en la primera llamada a la función
    if visitados is None:
        visitados = set()  # Evita revisitar nodos (para grafos con ciclos)
    if camino is None:
        camino = []        # Almacena el camino actual
    
    camino.append(inicio)   # Añadir el nodo actual al camino
    visitados.add(inicio)   # Marcar el nodo como visitado
    
    # Caso base: Si el nodo actual es el objetivo, retornar el camino
    if inicio == objetivo:
        return camino
    
    # Explorar todos los vecinos del nodo actual
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            # Llamada recursiva con el vecino como nuevo nodo actual
            resultado = dfs(grafo, vecino, objetivo, visitados.copy(), camino.copy())
            
            # Si se encontró un camino, retornarlo
            if resultado is not None:
                return resultado
    
    # Si no se encontró el objetivo en este camino, retornar None
    return None


# Ejemplo de uso
inicio = 'A'
objetivo = 'F'
print(f"Camino de {inicio} a {objetivo}: {dfs(grafo, inicio, objetivo)}")