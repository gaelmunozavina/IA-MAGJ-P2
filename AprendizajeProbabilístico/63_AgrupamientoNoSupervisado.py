import numpy as np

def k_means(datos, k, iteraciones=10):
    # 1. Inicialización: Elegir k centroides al azar de entre los datos
    indices = np.random.choice(len(datos), k, replace=False)
    centroides = datos[indices]
    
    for _ in range(iteraciones):
        # 2. Asignación: Calcular a qué centroide está más cerca cada punto
        # Usamos la distancia euclidiana
        distancias = np.linalg.norm(datos[:, np.newaxis] - centroides, axis=2)
        etiquetas = np.argmin(distancias, axis=1)
        
        # 3. Actualización: Mover los centroides al promedio de sus puntos asignados
        nuevos_centroides = np.array([datos[etiquetas == i].mean(axis=0) for i in range(k)])
        
        # Si los centroides no cambian, hemos terminado
        if np.all(centroides == nuevos_centroides):
            break
        centroides = nuevos_centroides
        
    return etiquetas, centroides

# --- ESCENARIO ---
# Creamos datos sintéticos en 2D (ej. 3 grupos de personas por altura y peso)
grupo1 = np.random.normal([160, 60], 5, (20, 2))
grupo2 = np.random.normal([180, 80], 5, (20, 2))
datos = np.vstack([grupo1, grupo2])

etiquetas, centros = k_means(datos, k=2)

print(f"Agrupamiento completado:")
print(f"  Centroide Grupo 0 (Altura, Peso): {centros[0]}")
print(f"  Centroide Grupo 1 (Altura, Peso): {centros[1]}")
