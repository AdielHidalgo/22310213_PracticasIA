import random

def objetivo(solucion):
    """Función de evaluación: queremos minimizar la distancia a 42."""
    return abs(solucion - 42)

def generar_vecinos(solucion, rango=5, num_vecinos=3):
    """Genera un conjunto de vecinos de la solución actual."""
    return [solucion + random.randint(-rango, rango) for _ in range(num_vecinos)]

def busqueda_haz_local(k=3, iteraciones=100):
    """Implementación de la Búsqueda de Haz Local."""
    soluciones = [random.randint(0, 100) for _ in range(k)]  # Inicializar k soluciones aleatorias

    for _ in range(iteraciones):
        # Generamos vecinos de todas las soluciones actuales
        vecinos = []
        for solucion in soluciones:
            vecinos.extend(generar_vecinos(solucion))

        # Seleccionamos las k mejores soluciones entre las actuales y los vecinos
        soluciones = sorted(soluciones + vecinos, key=objetivo)[:k]

        # Si alguna solución es óptima (objetivo = 0), terminamos
        if objetivo(soluciones[0]) == 0:
            break

    return soluciones[0]  # Devolvemos la mejor solución encontrada

# Prueba del algoritmo
mejor_solucion = busqueda_haz_local()
print(f"Mejor solución encontrada: {mejor_solucion}")
