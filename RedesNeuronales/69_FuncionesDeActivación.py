import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

def softmax(x):
    e_x = np.exp(x - np.max(x)) # Estabilidad numérica
    return e_x / e_x.sum()

# --- PRUEBA ---
valores_entrada = np.array([-2.0, -0.5, 0.0, 1.0, 2.0])

print("Transformaciones de Activación:")
print(f"Entrada original: {valores_entrada}")
print(f"Sigmoide:    {np.round(sigmoid(valores_entrada), 3)}")
print(f"ReLU:        {relu(valores_entrada)}")
print(f"Tanh:        {np.round(tanh(valores_entrada), 3)}")
print(f"Softmax:     {np.round(softmax(valores_entrada), 3)}")
