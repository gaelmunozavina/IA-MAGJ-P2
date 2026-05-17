import cv2
import numpy as np

# Simulamos dos fotogramas de video
# Frame 1: Fondo negro
frame1 = np.zeros((200, 200), dtype=np.uint8)
# Frame 2: Un cuadrado se ha movido a la derecha
frame2 = np.zeros((200, 200), dtype=np.uint8)
cv2.rectangle(frame2, (50, 50), (100, 100), 255, -1)

# 1. Calcular la diferencia absoluta entre fotogramas
diferencia = cv2.absdiff(frame1, frame2)

# 2. Umbralización para resaltar el movimiento
_, movimiento_detectado = cv2.threshold(diferencia, 25, 255, cv2.THRESH_BINARY)

# 3. Encontrar contornos del área que se movió
contornos, _ = cv2.findContours(movimiento_detectado, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contornos:
    x, y, w, h = cv2.boundingRect(c)
    print(f"Movimiento detectado en: x={x}, y={y}, ancho={w}, alto={h}")

# Nota: En un sistema real, se usa cv2.VideoCapture(0) para procesar el flujo en vivo
