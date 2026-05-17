import numpy as np

def rotar_punto_2d(punto, angulo_grados):
    # Convertir a radianes
    theta = np.radians(angulo_grados)
    
    # Matriz de Rotación 2D
    # [ cos(theta)  -sin(theta) ]
    # [ sin(theta)   cos(theta) ]
    matriz_rotacion = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  (np.sin(theta))]
    ])
    
    return np.dot(matriz_rotacion, punto)

# --- ESCENARIO ---
# Un punto en la coordenada (1, 0)
punto_original = np.array([1, 0])
# Rotarlo 90 grados
punto_rotado = rotar_punto_2d(punto_original, 90)

print(f"Punto original: {punto_original}")
print(f"Punto tras rotación de 90°: {np.round(punto_rotado, 2)}")
