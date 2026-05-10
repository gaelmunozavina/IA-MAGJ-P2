import numpy as np

def simular_procesos(n_puntos=500):
    # 1. Proceso Estacionario (Ruido Blanco)
    # La media siempre tiende a 0 y la varianza es constante
    estacionario = np.random.normal(0, 1, n_puntos)
    
    # 2. Proceso No Estacionario (Caminata Aleatoria / Random Walk)
    # La media y la varianza "vagan" sin control con el tiempo
    no_estacionario = np.cumsum(np.random.normal(0, 1, n_puntos))
    
    print("Análisis de Procesos:")
    print("-" * 30)
    print(f"Estacionario    | Media: {np.mean(estacionario):.4f} | Var: {np.var(estacionario):.4f}")
    print(f"No Estacionario | Media: {np.mean(no_estacionario):.4f} | Var: {np.var(no_estacionario):.4f}")
    
    return estacionario, no_estacionario

# --- EJECUCIÓN ---
datos_s, datos_ns = simular_procesos()

# Nota para el repositorio: 
# Si el proceso es No Estacionario, la IA suele aplicar una "Diferenciación" 
# (restar el valor actual menos el anterior) para intentar volverlo estacionario.
