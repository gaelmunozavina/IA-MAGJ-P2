import numpy as np

# Definición de estados: 0: Soleado, 1: Lluvioso
estados = ["Soleado", "Lluvioso"]

# Matriz de Transición (Filas=Hoy, Columnas=Mañana)
# [0,0]: Soleado -> Soleado (0.8)
# [0,1]: Soleado -> Lluvioso (0.2)
# [1,0]: Lluvioso -> Soleado (0.4)
# [1,1]: Lluvioso -> Lluvioso (0.6)
P = np.array([
    [0.8, 0.2],
    [0.4, 0.6]
])

def simular_clima(dias, estado_inicial=0):
    historial = [estado_inicial]
    estado_actual = estado_inicial
    
    for _ in range(dias - 1):
        # Elegir el siguiente estado basado en las probabilidades de la matriz P
        proximo_estado = np.random.choice([0, 1], p=P[estado_actual])
        historial.append(proximo_estado)
        estado_actual = proximo_estado
        
    return [estados[s] for s in historial]

# --- EJECUCIÓN ---
pronostico = simular_clima(10)
print(f"Simulación de 10 días basada en la Hipótesis de Markov:")
print(f"  {' -> '.join(pronostico)}")
