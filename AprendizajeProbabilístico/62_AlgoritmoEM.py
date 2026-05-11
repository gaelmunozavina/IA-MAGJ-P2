import numpy as np

def algoritmo_em_simple(datos, iteraciones=20):
    # Inicialización aleatoria de las medias de dos grupos
    mu1, mu2 = np.random.choice(datos), np.random.choice(datos)
    
    for i in range(iteraciones):
        # --- PASO E: Estimar pertenencia ---
        # Calculamos la "responsabilidad" de cada grupo sobre cada dato
        # (Usamos una distancia simple para este ejemplo pedagógico)
        dist1 = np.abs(datos - mu1)
        dist2 = np.abs(datos - mu2)
        
        # Probabilidad de pertenecer al grupo 1
        pertenencia1 = dist2 / (dist1 + dist2)
        pertenencia2 = 1 - pertenencia1
        
        # --- PASO M: Maximizar parámetros ---
        # Recalcular las medias ponderadas por la pertenencia
        mu1 = np.sum(pertenencia1 * datos) / np.sum(pertenencia1)
        mu2 = np.sum(pertenencia2 * datos) / np.sum(pertenencia2)
        
    return mu1, mu2

# --- ESCENARIO ---
# Generamos dos grupos de datos: uno centrado en 10 y otro en 50
grupo_a = np.random.normal(10, 2, 50)
grupo_b = np.random.normal(50, 2, 50)
datos_mezclados = np.concatenate([grupo_a, grupo_b])

m1, m2 = algoritmo_em_simple(datos_mezclados)

print(f"Tras el algoritmo EM:")
print(f"  Media estimada Grupo 1: {m1:.2f}")
print(f"  Media estimada Grupo 2: {m2:.2f}")
