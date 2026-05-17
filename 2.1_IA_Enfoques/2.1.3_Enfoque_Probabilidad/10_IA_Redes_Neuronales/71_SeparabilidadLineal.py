import numpy as np

def comprobar_separabilidad(X, y, epocas=1000):
    # Inicialización de pesos
    pesos = np.zeros(X.shape[1])
    bias = 0
    eta = 0.1
    
    # Entrenamiento del Perceptrón
    for _ in range(epocas):
        errores_en_epoca = 0
        for xi, objetivo in zip(X, y):
            prediccion = 1 if (np.dot(xi, pesos) + bias) >= 0 else 0
            actualizacion = eta * (objetivo - prediccion)
            pesos += actualizacion * xi
            bias += actualizacion
            if actualizacion != 0:
                errores_en_epoca += 1
        
        # Si el error llega a cero, es linealmente separable
        if errores_en_epoca == 0:
            return True, pesos, bias
            
    return False, pesos, bias

# --- CASO 1: OR (Linealmente Separable) ---
X_or = np.array([[0,0], [0,1], [1,0], [1,1]])
y_or = np.array([0, 1, 1, 1])

# --- CASO 2: XOR (NO Linealmente Separable) ---
X_xor = np.array([[0,0], [0,1], [1,0], [1,1]])
y_xor = np.array([0, 1, 1, 0])

sep_or, _, _ = comprobar_separabilidad(X_or, y_or)
sep_xor, _, _ = comprobar_separabilidad(X_xor, y_xor)

print(f"¿Es la compuerta OR linealmente separable?: {sep_or}")
print(f"¿Es la compuerta XOR linealmente separable?: {sep_xor}")
