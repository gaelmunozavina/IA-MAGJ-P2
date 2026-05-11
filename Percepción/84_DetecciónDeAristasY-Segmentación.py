import cv2
import numpy as np

# Simulamos una imagen con un objeto (un cuadrado gris sobre fondo negro)
imagen = np.zeros((100, 100), dtype=np.uint8)
cv2.rectangle(imagen, (25, 25), (75, 75), 150, -1)

# 1. DETECCIÓN DE ARISTAS (Canny)
# Los parámetros son los umbrales mínimo y máximo
bordes = cv2.Canny(imagen, 100, 200)

# 2. SEGMENTACIÓN POR UMBRALIZACIÓN (Otsu)
# Calcula automáticamente el umbral óptimo para separar fondo de figura
_, segmentada = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print("Procesamiento completado:")
print(f"Píxeles detectados como borde: {np.sum(bordes > 0)}")
print(f"Píxeles detectados como objeto: {np.sum(segmentada == 255)}")

# Nota: En un entorno real, usarías cv2.imshow() para ver los resultados
