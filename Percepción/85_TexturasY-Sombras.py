import numpy as np
import cv2

def extraer_lbp_pixel(img, x, y):
    # Comparamos el píxel central con sus 8 vecinos
    centro = img[x, y]
    patron = 0
    # Vecinos en orden de las manecillas del reloj
    vecinos = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y+1), (x+1,y+1), (x+1,y), (x+1,y-1), (x,y-1)]
    
    for i, (vx, vy) in enumerate(vecinos):
        # Si el vecino es mayor o igual al centro, ponemos un 1 (bit)
        if img[vx, vy] >= centro:
            patron += (1 << i)
            
    return patron

# --- ESCENARIO ---
# Creamos una "textura" sintética 3x3
textura = np.array([
    [50,  100, 200],
    [30,   80,  90],
    [10,   20,  30]
], dtype=np.uint8)

# Analizamos el centro (80)
codigo_lbp = extraer_lbp_pixel(textura, 1, 1)

print(f"Imagen de textura:\n{textura}")
print(f"\nCódigo LBP del centro: {codigo_lbp} (Binario: {bin(codigo_lbp)})")
