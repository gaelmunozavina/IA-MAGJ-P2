import numpy as np

class RedHopfield:
    def __init__(self, tamano):
        self.n = tamano
        self.pesos = np.zeros((tamano, tamano))

    def entrenar(self, patrones):
        for p in patrones:
            # Regla de Hebb: el peso es el producto externo del patrón
            p = p.reshape(-1, 1)
            self.pesos += np.dot(p, p.T)
        # La diagonal debe ser cero (una neurona no se conecta consigo misma)
        np.fill_diagonal(self.pesos, 0)

    def recuperar(self, entrada, intentos=5):
        estado = np.array(entrada)
        for _ in range(intentos):
            for i in range(self.n):
                # Activación: signo de la suma ponderada
                u = np.dot(self.pesos[i], estado)
                estado[i] = 1 if u >= 0 else -1
        return estado

# --- ESCENARIO ---
# Patrón a recordar: [1, 1, -1, -1]
patron_memoria = np.array([1, 1, -1, -1])
red = RedHopfield(tamano=4)
red.entrenar([patron_memoria])

# Entrada con ruido (el último bit está mal)
entrada_ruidosa = np.array([1, 1, -1, 1])
recuerdo = red.recuperar(entrada_ruidosa)

print(f"Patrón Original:  {patron_memoria}")
print(f"Entrada Ruidosa:  {entrada_ruidosa}")
print(f"Patrón Recuperado: {recuerdo}")
