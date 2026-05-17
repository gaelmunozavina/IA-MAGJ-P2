def funcion_objetivo(solucion):
    """Calcula qué tan cerca está la suma de la solución al objetivo de 100."""
    return abs(100 - sum(solucion))

def obtener_vecinos(solucion):
    """Genera soluciones vecinas cambiando un número de la lista."""
    vecinos = []
    for i in range(len(solucion)):
        vecino = list(solucion)
        # Cambiamos un valor aleatoriamente para crear una variante
        vecino[i] = vecino[i] + 1 
        vecinos.append(vecino)
    return vecinos

def busqueda_tabu(solucion_inicial, max_iteraciones, tamaño_tabu):
    """
    Algoritmo de Búsqueda Tabú.
    """
    mejor_solucion = solucion_inicial
    solucion_actual = solucion_inicial
    lista_tabu = []

    print(f"Inicio: {solucion_inicial}, Costo: {funcion_objetivo(solucion_inicial)}")

    for i in range(max_iteraciones):
        vecinos = obtener_vecinos(solucion_actual)
        mejor_vecino = None
        mejor_vecino_costo = float('inf')

        for vecino in vecinos:
            # Solo consideramos al vecino si no está en la lista tabú
            if vecino not in lista_tabu:
                costo_v = funcion_objetivo(vecino)
                if costo_v < mejor_vecino_costo:
                    mejor_vecino = vecino
                    mejor_vecino_costo = costo_v

        # Si encontramos un vecino válido que no es tabú
        if mejor_vecino is not None:
            solucion_actual = mejor_vecino
            # Actualizamos la mejor solución global
            if mejor_vecino_costo < funcion_objetivo(mejor_solucion):
                mejor_solucion = mejor_vecino
            
            # Agregamos a la lista tabú y mantenemos su tamaño
            lista_tabu.append(mejor_vecino)
            if len(lista_tabu) > tamaño_tabu:
                lista_tabu.pop(0)

        if i % 5 == 0:
            print(f"Iteración {i}: Mejor costo actual = {funcion_objetivo(mejor_solucion)}")

    return mejor_solucion

# --- EJECUCIÓN ---
inicial = [10, 20, 30] # Suma 60, objetivo 100
resultado = busqueda_tabu(inicial, 20, 5)

print(f"\nResultado Final: {resultado}")
print(f"Costo Final: {funcion_objetivo(resultado)}")
