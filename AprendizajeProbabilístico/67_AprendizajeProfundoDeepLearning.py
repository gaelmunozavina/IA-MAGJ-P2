import numpy as np

# Función de activación (Sigmoide) para introducir no linealidad
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivate(x):
    return x * (1 - x)

# --- ARQUITECTURA DE LA RED ---
# Entradas (4 ejemplos de 3 características cada uno)
X = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
# Salidas deseadas
y = np.array([[0], [1], [1], [0]])

# Inicialización de pesos aleatorios (Sinapsis)
np.random.seed(1)
pesos_capa1 = 2 * np.random.random((3, 4)) - 1
pesos_capa2 = 2 * np.random.random((4, 1)) - 1

# --- ENTRENAMIENTO (Forward y Backward) ---
for iteracion in range(10000):
    # Capa 1 (Entrada -> Oculta)
    capa_entrada = X
    capa_oculta = sigmoid(np.dot(capa_entrada, pesos_capa1))
    
    # Capa 2 (Oculta -> Salida)
    capa_salida = sigmoid(np.dot(capa_oculta, pesos_capa2))
    
    # Cálculo del Error
    error_salida = y - capa_salida
    
    # Backpropagation (Ajuste de pesos)
    delta_salida = error_salida * sigmoid_derivate(capa_salida)
    error_capa_oculta = delta_salida.dot(pesos_capa2.T)
    delta_capa_oculta = error_capa_oculta * sigmoid_derivate(capa_oculta)
    
    pesos_capa2 += capa_oculta.T.dot(delta_salida)
    pesos_capa1 += capa_entrada.T.dot(delta_capa_oculta)

print("Salida de la red después del entrenamiento:")
print(capa_salida)
