import random

# Función de aptitud: Queremos minimizar la diferencia con 42
def funcion_aptitud(solucion):
    return abs(solucion - 42)

# Genera una población inicial aleatoria
def inicializar_poblacion(tamano=10):
    return [random.randint(0, 100) for _ in range(tamano)]

# Selección por torneo: elige dos candidatos y selecciona el mejor
def seleccion(poblacion):
    candidato1, candidato2 = random.sample(poblacion, 2)
    return candidato1 if funcion_aptitud(candidato1) < funcion_aptitud(candidato2) else candidato2

# Cruce de dos padres: promedia los valores (puede ser otro método)
def cruzar(padre1, padre2):
    return (padre1 + padre2) // 2  # Redondeo entero

# Mutación: cambia la solución aleatoriamente dentro de un rango
def mutar(solucion, tasa_mutacion=0.1):
    if random.random() < tasa_mutacion:
        return solucion + random.randint(-5, 5)  # Pequeño cambio aleatorio
    return solucion

# Algoritmo Genético
def algoritmo_genetico(generaciones=50, tamano_poblacion=10, tasa_mutacion=0.1):
    poblacion = inicializar_poblacion(tamano_poblacion)

    for _ in range(generaciones):
        nueva_poblacion = []
        for _ in range(tamano_poblacion):
            padre1, padre2 = seleccion(poblacion), seleccion(poblacion)
            hijo = cruzar(padre1, padre2)
            hijo = mutar(hijo, tasa_mutacion)
            nueva_poblacion.append(hijo)
        
        # Reemplazamos la población
        poblacion = sorted(nueva_poblacion, key=funcion_aptitud)

        # Si encontramos la solución exacta, terminamos antes
        if funcion_aptitud(poblacion[0]) == 0:
            break

    return poblacion[0]  # Mejor solución encontrada

# Ejecutar el Algoritmo Genético
mejor_solucion = algoritmo_genetico()
print(f"Mejor solución encontrada: {mejor_solucion}")
