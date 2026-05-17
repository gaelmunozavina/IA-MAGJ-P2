import numpy as np

# 1. Distribución de Bernoulli (Éxito en una tarea)
# Simula si un brazo robótico logra sujetar un objeto con 75% de éxito
prob_exito = 0.75
intentos = 10
exitos = np.random.binomial(n=1, p=prob_exito, size=intentos)
print(f"Resultados de Bernoulli (1=Éxito, 0=Fallo): {exitos}")

# 2. Distribución Normal (Ruido de un sensor de distancia)
# Media (valor real) = 100cm, Desviación estándar (error) = 2cm
media = 100
sigma = 2
lecturas_sensor = np.random.normal(media, sigma, 5)

print("\nLecturas del sensor con ruido Gaussiano (en cm):")
for i, l in enumerate(lecturas_sensor, 1):
    print(f"  Lectura {i}: {l:.2f}")
  
