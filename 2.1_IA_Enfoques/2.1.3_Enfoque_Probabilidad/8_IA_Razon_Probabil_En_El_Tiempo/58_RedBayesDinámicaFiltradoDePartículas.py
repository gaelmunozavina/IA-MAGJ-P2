import numpy as np

def filtrado_particulas(medicion, n_particulas=1000):
    # 1. Inicialización: Partículas distribuidas uniformemente entre 0 y 20m
    particulas = np.random.uniform(0, 20, n_particulas)
    pesos = np.ones(n_particulas) / n_particulas

    # 2. Predicción: El robot se movió (supongamos +2 metros)
    particulas += 2 + np.random.normal(0, 0.5, n_particulas)

    # 3. Actualización: El sensor mide 'medicion'
    # Calculamos el peso basado en la cercanía a la medición (Gaussiana)
    sigma_sensor = 1.0
    pesos = np.exp(-0.5 * ((particulas - medicion) / sigma_sensor)**2)
    pesos += 1e-300 # Evitar división por cero
    pesos /= sum(pesos) # Normalizar

    # 4. Resampleo (Muestreo por importancia)
    indices = np.random.choice(range(n_particulas), size=n_particulas, p=pesos)
    particulas = particulas[indices]

    return np.mean(particulas), np.std(particulas)

# --- ESCENARIO ---
# El robot cree que está cerca de los 12 metros según sus sensores
pos_estimada, incertidumbre = filtrado_particulas(medicion=12.0)

print(f"Localización por Partículas:")
print(f"  Posición media estimada: {pos_estimada:.2f} m")
print(f"  Incertidumbre (Desviación): {incertidumbre:.4f}")
