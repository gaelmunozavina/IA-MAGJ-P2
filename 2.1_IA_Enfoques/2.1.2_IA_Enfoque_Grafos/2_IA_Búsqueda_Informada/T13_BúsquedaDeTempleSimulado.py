import math
import random

def funcion_objetivo(x):
    """
    Función con muchos picos y valles (óptimos locales).
    Queremos encontrar el x que dé el valor más bajo.
    """
    return x**2 + 10 * math.sin(x)

def temple_simulado(inicio_x, temp_inicial, enfriamiento, iteraciones):
    """
    Algoritmo de Temple Simulado.
    
    Args:
        inicio_x: Punto de partida.
        temp_inicial: Temperatura de inicio (audacia).
        enfriamiento: Factor de reducción de temperatura (0.9 a 0.99).
        iteraciones: Número de pasos.
    """
    actual_x = inicio_x
    actual_costo = funcion_objetivo(actual_x)
    mejor_x = actual_x
    mejor_costo = actual_costo
    
    temp_actual = temp_inicial

    print(f"Inicio en x: {actual_x:.2f}, Costo inicial: {actual_costo:.2f}")

    for i in range(iteraciones):
        # Generar un vecino aleatorio cercano
        vecino_x = actual_x + random.uniform(-1, 1)
        vecino_costo = funcion_objetivo(vecino_x)
        
        # Calcular la diferencia de costo
        diff = vecino_costo - actual_costo
        
        # ¿Aceptamos el nuevo movimiento?
        # 1. Si es mejor, lo aceptamos siempre.
        # 2. Si es peor, lo aceptamos con una probabilidad basada en la temperatura.
        if diff < 0 or random.random() < math.exp(-diff / temp_actual):
            actual_x = vecino_x
            actual_costo = vecino_costo
            
            # Actualizar el récord histórico
            if actual_costo < mejor_costo:
                mejor_x = actual_x
                mejor_costo = actual_costo
        
        # Enfriar el sistema
        temp_actual *= enfriamiento
        
        if i % 100 == 0:
            print(f"Iteración {i}: Mejor costo = {mejor_costo:.4f}, Temp = {temp_actual:.4f}")

    return mejor_x, mejor_costo

# --- EJECUCIÓN ---
res_x, res_costo = temple_simulado(inicio_x=10, temp_inicial=100, enfriamiento=0.95, iteraciones=1000)

print(f"\nResultado Final:")
print(f"Mejor x encontrado: {res_x:.4f}")
print(f"Costo mínimo alcanzado: {res_costo:.4f}")
