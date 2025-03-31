def dls(grafo, nodo, objetivo, limite, visitados=None, camino=None):
    """
    Búsqueda en Profundidad Limitada (DLS).
    
    Args:
        grafo (dict): Grafo representado como diccionario de adyacencia.
        nodo (str): Nodo actual en la búsqueda.
        objetivo (str): Nodo objetivo a encontrar.
        limite (int): Profundidad máxima permitida.
        visitados (set): Nodos ya visitados (para evitar ciclos).
        camino (list): Camino recorrido hasta el momento.
    
    Returns:
        list: Camino al objetivo si se encuentra, de lo contrario None.
    """
    # Inicializar estructuras en la primera llamada
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []
    
    camino.append(nodo)
    visitados.add(nodo)
    
    # Caso base: nodo actual es el objetivo
    if nodo == objetivo:
        return camino
    
    # Caso base: se alcanzó el límite de profundidad
    if limite <= 0:
        return None  # Retroceder
    
    # Explorar vecinos recursivamente
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            resultado = dls(grafo, vecino, objetivo, limite - 1, visitados.copy(), camino.copy())
            if resultado is not None:
                return resultado
    
    return None  # Si no se encontró en esta rama


# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

inicio = 'A'
objetivo = 'F'

# Límites de profundidad para probar
print("DLS (límite 1):", dls(grafo, inicio, objetivo, 1))  # No encuentra F
print("DLS (límite 2):", dls(grafo, inicio, objetivo, 2))  # A → C → F
print("DLS (límite 3):", dls(grafo, inicio, objetivo, 3))  # A → B → E → F