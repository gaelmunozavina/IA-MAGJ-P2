import random

def funcion_objetivo(x):
    """
    Representa la 'colina'. Queremos encontrar el valor de x que maximice esta función.
    f(x) = -(x-5)^2 + 20  (Una parábola invertida con cima en x=5)
    """
    return -(x - 5)**2 + 20

def hill_climbing(inicio_x, paso=0.1, iteraciones=100):
    """
    Algoritmo de Ascensión de Colinas simple.
    
    Args:
        inicio_x: Punto de partida aleatorio.
        paso: Qué tanto nos movemos para explorar vecinos.
        iteraciones: Cuántas veces intentaremos subir.
    """
    actual_x = inicio_x
    actual_valor = funcion_objetivo(actual_x)
    
    print(f"Inicio en x: {actual_x:.2f}, Valor: {actual_valor:.2f}")

    for i in range(iteraciones):
        # Exploramos los vecinos (un paso a la izquierda y un paso a la derecha)
        vecino_izq = actual_x - paso
        vecino_der = actual_x + paso
        
        valor_izq = funcion_objetivo(vecino_izq)
        valor_der = funcion_objetivo(vecino_der)
        
        # ¿Algún vecino es mejor (más alto) que mi posición actual?
        if valor_izq > actual_valor and valor_izq >= valor_der:
            actual_x = vecino_izq
            actual_valor = valor_izq
        elif valor_der > actual_valor and valor_der > valor_izq:
            actual_x = vecino_der
            actual_valor = valor_der
        else:
            # Si ningún vecino es mejor, hemos llegado a una cima (local o global)
            print(f"Cima encontrada en iteración {i}")
            break
            
        if i % 10 == 0:
            print(f"  Paso {i}: x = {actual_x:.2f}, f(x) = {actual_valor:.2f}")

    return actual_x, actual_valor

# --- EJECUCIÓN ---
# Empezamos en un punto aleatorio lejos de la meta (x=5)
punto_partida = random.uniform(-10, 10)
mejor_x, mejor_valor = hill_climbing(punto_partida)

print(f"\nResultado Final:")
print(f"Mejor punto encontrado: {mejor_x:.4f}")
print(f"Valor máximo alcanzado: {mejor_valor:.4f}")
