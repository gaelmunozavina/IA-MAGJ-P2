import numpy as np
from collections import Counter

# --- K-NN (Clasificación) ---
def knn_clasificar(punto_nuevo, datos_entrenamiento, etiquetas, k=3):
    # Calcular distancias euclidianas
    distancias = [np.linalg.norm(punto_nuevo - x) for x in datos_entrenamiento]
    # Obtener los índices de los k vecinos más cercanos
    k_vecinos_indices = np.argsort(distancias)[:k]
    # Votación de etiquetas
    votos = [etiquetas[i] for i in k_vecinos_indices]
    return Counter(votos).most_common(1)[0][0]

# --- k-Medias (Agrupamiento) ---
def k_medias_simple(datos, k=2, iteraciones=5):
    # Inicializar centroides al azar
    centroides = datos[np.random.choice(len(datos), k, replace=False)]
    for _ in range(iteraciones):
        # Asignar cada punto al centroide más cercano
        etiquetas = np.array([np.argmin([np.linalg.norm(x - c) for c in centroides]) for x in datos])
        # Recalcular centroides
        centroides = np.array([datos[etiquetas == i].mean(axis=0) for i in range(k)])
    return etiquetas, centroides

# --- PRUEBA ---
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
y = ["Bajo", "Bajo", "Alto", "Alto", "Bajo", "Alto"]

# 1. Probar KNN
nuevo = np.array([2, 2])
clase = knn_clasificar(nuevo, X, y)
print(f"KNN: El punto {nuevo} pertenece a la clase: {clase}")

# 2. Probar k-Medias
clusters, centros = k_medias_simple(X, k=2)
print(f"k-Medias: Clusters encontrados: {clusters}")
