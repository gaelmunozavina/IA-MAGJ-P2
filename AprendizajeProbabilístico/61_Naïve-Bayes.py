import collections
import math

class NaiveBayesSpam:
    def __init__(self):
        self.vocabulario = set()
        self.conteo_palabras = {"spam": collections.Counter(), "ham": collections.Counter()}
        self.total_mensajes = {"spam": 0, "ham": 0}

    def entrenar(self, mensajes, etiquetas):
        for msg, etiqueta in zip(mensajes, etiquetas):
            palabras = msg.lower().split()
            self.total_mensajes[etiqueta] += 1
            for p in palabras:
                self.vocabulario.add(p)
                self.conteo_palabras[etiqueta][p] += 1

    def predecir(self, mensaje):
        palabras = mensaje.lower().split()
        prob_spam = math.log(self.total_mensajes["spam"] / sum(self.total_mensajes.values()))
        prob_ham = math.log(self.total_mensajes["ham"] / sum(self.total_mensajes.values()))

        for p in palabras:
            # Aplicamos suavizado de Laplace (+1) para evitar probabilidad cero
            prob_spam += math.log((self.conteo_palabras["spam"][p] + 1) / 
                                  (sum(self.conteo_palabras["spam"].values()) + len(self.vocabulario)))
            prob_ham += math.log((self.conteo_palabras["ham"][p] + 1) / 
                                 (sum(self.conteo_palabras["ham"].values()) + len(self.vocabulario)))

        return "Spam" if prob_spam > prob_ham else "Ham"

# --- ENTRENAMIENTO ---
data = ["oferta ganar dinero gratis", "hola como estas amigo", "premio gratis clic aqui", "reunion mañana a las diez"]
labels = ["spam", "ham", "spam", "ham"]

clf = NaiveBayesSpam()
clf.entrenar(data, labels)

# --- PRUEBA ---
test_msg = "ganar premio gratis"
print(f"Mensaje: '{test_msg}'")
print(f"Clasificación: {clf.predecir(test_msg)}")
