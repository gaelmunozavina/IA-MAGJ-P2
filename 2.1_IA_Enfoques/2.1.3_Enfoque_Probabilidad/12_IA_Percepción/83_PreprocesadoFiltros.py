import cv2
import numpy as np

# Simulamos una imagen con ruido (matriz 5x5)
imagen = np.array([
    [10, 10, 10, 10, 10],
    [10, 255, 10, 10, 10], # Píxel ruidoso (Sal)
    [10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10]
], dtype=np.uint8)

# 1. Filtro de Mediana (Ideal para ruido tipo sal y pimienta)
img_mediana = cv2.medianBlur(imagen, 3)

# 2. Filtro Gaussiano (Suavizado general)
img_gauss = cv2.GaussianBlur(imagen, (3, 3), 0)

# 3. Filtro Sobel (Detección de bordes)
# Usualmente se aplica a imágenes reales, aquí un ejemplo de sintaxis:
# sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)

print("Imagen Original (con ruido en [1,1]):\n", imagen)
print("\nTras Filtro de Mediana (Ruido eliminado):\n", img_mediana)
print("\nTras Filtro Gaussiano (Ruido difuminado):\n", img_gauss)
