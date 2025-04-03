import random

def objetivo(solucion):
    """Función de evaluación: en este caso, minimizamos el valor absoluto."""
    return abs(solucion - 42)  # Queremos encontrar el número 42

def generar_vecinos(solucion, rango=5):
    """Genera vecinos dentro de un pequeño rango de la solución actual."""
    return [solucion + random.randint(-rango, rango) for _ in range(5)]

def busqueda_tabu(solucion_inicial, iteraciones_max=100, tamano_tabu=5):
    """Implementación de la Búsqueda Tabú."""
    mejor_solucion = solucion_inicial
    mejor_valor = objetivo(mejor_solucion)
    solucion_actual = solucion_inicial
    lista_tabu = []  # Lista Tabú para evitar ciclos

    for _ in range(iteraciones_max):
        vecinos = generar_vecinos(solucion_actual)

        # Eliminamos vecinos en la lista tabú
        vecinos_validos = [v for v in vecinos if v not in lista_tabu]

        if not vecinos_validos:
            break  # Si no hay vecinos válidos, terminamos

        # Seleccionamos el mejor vecino
        solucion_actual = min(vecinos_validos, key=objetivo)
        valor_actual = objetivo(solucion_actual)

        # Actualizamos la mejor solución si mejora
        if valor_actual < mejor_valor:
            mejor_solucion, mejor_valor = solucion_actual, valor_actual

        # Agregamos la solución a la lista tabú
        lista_tabu.append(solucion_actual)

        # Si la lista tabú supera su tamaño, eliminamos el más antiguo
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0)

    return mejor_solucion, mejor_valor

# Prueba del algoritmo
solucion_inicial = random.randint(0, 100)  # Número inicial aleatorio
mejor_solucion, mejor_valor = busqueda_tabu(solucion_inicial)

print(f"Mejor solución encontrada: {mejor_solucion} con valor de objetivo: {mejor_valor}")
