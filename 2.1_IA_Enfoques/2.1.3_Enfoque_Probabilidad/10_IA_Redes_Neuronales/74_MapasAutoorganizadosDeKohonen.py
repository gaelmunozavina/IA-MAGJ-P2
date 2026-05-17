import numpy as np

def entrenamiento_som(datos, dimensiones_red=(10, 10), epocas=100, tasa_aprendizaje=0.1):
    # 1. Inicializar la red con pesos aleatorios (Colores R, G, B)
    ancho, alto = dimensiones_red
    red = np.random.random((ancho, alto, 3))
    
    for epoca in range(epocas):
        for dato in datos:
            # 2. COMPETENCIA: Encontrar la BMU (Best Matching Unit)
            # Calculamos la distancia entre el dato y cada neurona de la red
            distancias = np.linalg.norm(red - dato, axis=2)
            bmu_idx = np.unravel_index(np.argmin(distancias), (ancho, alto))
            
            # 3. COOPERACIÓN y ADAPTACIÓN (Simplificada)
            # Actualizamos la BMU y sus vecinos inmediatos
            for i in range(max(0, bmu_idx[0]-1), min(ancho, bmu_idx[0]+2)):
                for j in range(max(0, bmu_idx[1]-1), min(alto, bmu_idx[1]+2)):
                    # Las neuronas se vuelven más parecidas al color de entrada
                    red[i, j] += tasa_aprendizaje * (dato - red[i, j])
                    
        # Reducir la tasa de aprendizaje con el tiempo
        tasa_aprendizaje *= 0.99
        
    return red

# --- ESCENARIO ---
# Colores: Rojo puro, Verde puro, Azul puro
colores_entrenamiento = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0]])
mapa_final = entrenamiento_som(colores_entrenamiento)

print("Mapa de Kohonen entrenado.")
print(f"Esquina [0,0] color (RGB): {np.round(mapa_final[0,0], 2)}")
print(f"Esquina [9,9] color (RGB): {np.round(mapa_final[9,9], 2)}")
