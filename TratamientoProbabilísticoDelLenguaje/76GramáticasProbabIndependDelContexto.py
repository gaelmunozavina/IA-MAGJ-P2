import collections

# Definición de la gramática con probabilidades
# S = Oración, NP = Frase Nominal, VP = Frase Verbal, PP = Frase Preposicional, P = Preposición
pcfg = {
    "S -> NP VP": 1.0,
    "VP -> V NP": 0.7,
    "VP -> VP PP": 0.3, # Ambigüedad: El VP incluye un instrumento
    "NP -> Det N": 0.6,
    "NP -> NP PP": 0.4, # Ambigüedad: El NP tiene el objeto
    "PP -> P NP": 1.0
}

def calcular_probabilidad_arbol(reglas_usadas):
    probabilidad = 1.0
    for regla in reglas_usadas:
        probabilidad *= pcfg.get(regla, 0.0)
    return probabilidad

# --- ESCENARIO: "Vi al hombre con el telescopio" ---
# Interpretación A: El telescopio modifica al verbo (yo lo usé)
arbol_a = ["S -> NP VP", "VP -> VP PP", "VP -> V NP", "PP -> P NP"]
# Interpretación B: El telescopio modifica al nombre (el hombre lo tenía)
arbol_b = ["S -> NP VP", "VP -> V NP", "NP -> NP PP", "PP -> P NP"]

prob_a = calcular_probabilidad_arbol(arbol_a)
prob_b = calcular_probabilidad_arbol(arbol_b)

print(f"Probabilidad Interpretación A (Instrumento): {prob_a:.4f}")
print(f"Probabilidad Interpretación B (Posesión):   {prob_b:.4f}")
print(f"La IA elige la opción con mayor probabilidad.")
