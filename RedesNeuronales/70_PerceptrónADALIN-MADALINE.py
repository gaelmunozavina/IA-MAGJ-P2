import numpy as np

class ModelosClasicos:
    def __init__(self, n_entradas):
        self.pesos = np.random.randn(n_entradas)
        self.bias = np.random.randn()
        self.eta = 0.01

    def perceptron_learn(self, x, y):
        # El error se basa en la salida binaria (0 o 1)
        prediccion = 1 if (np.dot(x, self.pesos) + self.bias) >= 0 else 0
        error = y - prediccion
        self.pesos += self.eta * error * x
        self.bias += self.eta * error

    def adaline_learn(self, x, y):
        # El error se basa en la salida lineal (continua) antes del escalón
        salida_lineal = np.dot(x, self.pesos) + self.bias
        error = y - salida_lineal
        # Descenso de gradiente: minimizamos el error cuadrático
        self.pesos += self.eta * error * x
        self.bias += self.eta * error

# --- ESCENARIO DE PRUEBA ---
X = np.array([1.5, 2.0])
y_deseada = 1

modelo_p = ModelosClasicos(2)
modelo_a = ModelosClasicos(2)

# El Adaline tiende a converger de forma más suave que el Perceptrón
modelo_p.perceptron_learn(X, y_deseada)
modelo_a.adaline_learn(X, y_deseada)

print("Pesos actualizados:")
print(f"  Perceptrón: {modelo_p.pesos}")
print(f"  ADALINE:    {modelo_a.pesos}")
