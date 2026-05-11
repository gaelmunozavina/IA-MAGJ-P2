import cv2
import numpy as np

# 1. Crear una imagen de "escena" (negra con un cuadrado blanco)
escena = np.zeros((200, 200), dtype=np.uint8)
cv2.rectangle(escena, (50, 50), (100, 100), 255, -1)

# 2. Crear la "plantilla" (el objeto que queremos encontrar)
# En un caso real, esto sería una imagen cargada: cv2.imread('pieza.jpg', 0)
plantilla = np.ones((50, 50), dtype=np.uint8) * 255

# 3. Aplicar Template Matching
# cv2.TM_CCOEFF_NORMED devuelve valores entre -1 y 1 (1 es coincidencia perfecta)
resultado = cv2.matchTemplate(escena, plantilla, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

# El punto max_loc es la esquina superior izquierda del objeto encontrado
top_left = max_loc
h, w = plantilla.shape
bottom_right = (top_left[0] + w, top_left[1] + h)

print(f"Confianza de la detección: {max_val:.4f}")
print(f"Objeto encontrado en las coordenadas: {top_left} hasta {bottom_right}")
