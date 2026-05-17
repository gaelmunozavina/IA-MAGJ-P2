import numpy as np

# Preparación de datos (Compuerta lógica simple)
X = np.array([[0, 1]])
y_real = np.array([[1]])

# Pesos iniciales
w1 = 0.5 # Peso entrada -> oculta
w2 = 0.7 # Peso oculta -> salida
tasa_aprendizaje = 0.1

def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_der(x): return x * (1 - x)

# --- 1. FORWARD PASS ---
capa_oculta = sigmoid(X * w1)
prediccion = sigmoid(capa_oculta * w2)

# --- 2. CÁLCULO DEL ERROR ---
error = y_real - prediccion

# --- 3. BACKPROPAGATION (Paso hacia atrás) ---
# Gradiente en la salida
delta_salida = error * sigmoid_der(prediccion)

# Gradiente en la capa oculta (propagando el error hacia atrás)
error_oculto = delta_salida * w2
delta_oculto = error_oculto * sigmoid_der(capa_oculta)

# --- 4. ACTUALIZACIÓN DE PESOS ---
w2 += (capa_oculta * delta_salida * tasa_aprendizaje).sum()
w1 += (X * delta_oculto * tasa_aprendizaje).sum()

print(f"Predicción inicial: {prediccion[0][0]:.4f}")
print(f"Nuevos pesos tras 1 iteración: w1={w1:.4f}, w2={w2:.4f}")
