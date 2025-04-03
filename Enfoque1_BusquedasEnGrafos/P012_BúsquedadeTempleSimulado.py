import math
import random

def objetivo(solucion):
    """Función de evaluación: queremos minimizar la distancia a 42."""
    return abs(solucion - 42)

def generar_vecino(solucion, rango=5):
    """Genera un vecino modificando la solución actual dentro de un pequeño rango."""
    return solucion + random.randint(-rango, rango)

def probabilidad_aceptacion(diferencia, temperatura):
    """Calcula la probabilidad de aceptar una solución peor."""
    return math.exp(-diferencia / temperatura)

def busqueda_temple_simulado(solucion_inicial, temp_inicial=100, enfriamiento=0.95, iteraciones=100):
    """Implementación del Temple Simulado."""
    solucion_actual = solucion_inicial
    mejor_solucion = solucion_actual
    mejor_valor = objetivo(solucion_actual)
    temperatura = temp_inicial

    for _ in range(iteraciones):
        vecino = generar_vecino(solucion_actual)
        valor_vecino = objetivo(vecino)
        valor_actual = objetivo(solucion_actual)

        # Si el vecino es mejor, lo aceptamos directamente
        if valor_vecino < valor_actual:
            solucion_actual = vecino
        else:
            # Si es peor, lo aceptamos con una probabilidad dependiente de la temperatura
            delta = valor_vecino - valor_actual
            if random.random() < probabilidad_aceptacion(delta, temperatura):
                solucion_actual = vecino

        # Actualizamos la mejor solución encontrada
        if objetivo(solucion_actual) < mejor_valor:
            mejor_solucion, mejor_valor = solucion_actual, objetivo(solucion_actual)

        # Reducimos la temperatura
        temperatura *= enfriamiento

        # Si la temperatura es muy baja, terminamos antes
        if temperatura < 0.01:
            break

    return mejor_solucion, mejor_valor

# Prueba del algoritmo
solucion_inicial = random.randint(0, 100)  # Solución inicial aleatoria
mejor_solucion, mejor_valor = busqueda_temple_simulado(solucion_inicial)

print(f"Mejor solución encontrada: {mejor_solucion} con valor de objetivo: {mejor_valor}")
