import numpy as np

class NeuronaSimple:
    def __init__(self, n_entradas, tasa_aprendizaje=0.1):
        # Inicializar pesos y sesgo al azar
        self.pesos = np.random.randn(n_entradas)
        self.sesgo = np.random.randn()
        self.eta = tasa_aprendizaje

    def activacion(self, x):
        # Función Escalón (Heaviside)
        return 1 if x >= 0 else 0

    def predecir(self, entradas):
        suma_ponderada = np.dot(entradas, self.pesos) + self.sesgo
        return self.activacion(suma_ponderada)

    def entrenar(self, datos_entrenamiento, etiquetas, epocas=100):
        for _ in range(epocas):
            for entradas, etiqueta in zip(datos_entrenamiento, etiquetas):
                prediccion = self.predecir(entradas)
                error = etiqueta - prediccion
                # Regla de aprendizaje del Perceptrón: actualizar pesos
                self.pesos += self.eta * error * entradas
                self.sesgo += self.eta * error

# --- ESCENARIO: COMPUERTA AND ---
# Si ambas entradas son 1, la salida debe ser 1
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 0, 0, 1])

modelo = NeuronaSimple(n_entradas=2)
modelo.entrenar(X, y)

print("Resultados de la Computación Neuronal (AND):")
for e in X:
    print(f"  Entrada {e} -> Predicción: {modelo.predecir(e)}")
  
