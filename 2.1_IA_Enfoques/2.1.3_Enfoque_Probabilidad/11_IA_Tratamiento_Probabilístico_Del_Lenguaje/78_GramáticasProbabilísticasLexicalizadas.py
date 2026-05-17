import collections

# Simulación de afinidades léxicas (Bigramas de Cabeza)
# P(Objeto | Verbo)
afinidad_lexica = {
    ("comer", "manzana"): 0.8,
    ("comer", "telescopio"): 0.001,
    ("ver", "manzana"): 0.2,
    ("ver", "telescopio"): 0.5
}

def analizar_afinidad(verbo, objeto):
    prob = afinidad_lexica.get((verbo, objeto), 0.01)
    return prob

# --- ESCENARIO ---
# Frase 1: "Vi al hombre con el telescopio" (El telescopio es para VER)
# Frase 2: "Comí la pizza con el telescopio" (Estructuralmente posible, semánticamente absurdo)

v1, obj1 = "ver", "telescopio"
v2, obj2 = "comer", "telescopio"

print(f"Análisis Lexicalizado:")
print(f"  Afinidad '{v1}' + '{obj1}': {analizar_afinidad(v1, obj1)}")
print(f"  Afinidad '{v2}' + '{obj2}': {analizar_afinidad(v2, obj2)}")

if analizar_afinidad(v1, obj1) > analizar_afinidad(v2, obj2):
    print("\nConclusión: Es mucho más probable que el telescopio sea un instrumento del verbo VER.")
  
