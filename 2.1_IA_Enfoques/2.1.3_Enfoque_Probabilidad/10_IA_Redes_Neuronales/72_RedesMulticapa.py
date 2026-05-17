import numpy as np

# Función de activación Sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivate(x):
    return x * (1 - x)

# --- DATOS XOR ---
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Configuración: 2 entradas, 4 neuronas ocultas, 1 salida
np.random.seed(42)
pesos_ocultos = np.random.uniform(size=(2, 4))
pesos_salida = np.random.uniform(size=(4, 1))

# --- ENTRENAMIENTO ---
for i in range(10000):
    # Forward Pass
    capa_oculta_activacion = sigmoid(np.dot(X, pesos_ocultos))
    capa_salida_activacion = sigmoid(np.dot(capa_oculta_activacion, pesos_salida))
    
    # Backpropagation
    error = y - capa_salida_activacion
    d_salida = error * sigmoid_derivate(capa_salida_activacion)
    
    error_oculto = d_salida.dot(pesos_salida.T)
    d_oculto = error_oculto * sigmoid_derivate(capa_oculta_activacion)
    
    # Actualización de pesos
    pesos_salida += capa_oculta_activacion.T.dot(d_salida) * 0.1
    pesos_ocultos += X.T.dot(d_oculto) * 0.1

print("Predicciones para XOR (Red Multicapa):")
print(capa_salida_activacion)
