import collections

# Corpus Paralelo simplificado
corpus_paralelo = [
    (["el", "gato", "negro"], ["the", "black", "cat"]),
    (["la", "casa", "roja"], ["the", "red", "house"]),
    (["el", "perro", "negro"], ["the", "black", "dog"])
]

def calcular_alineacion_basica(corpus):
    conteo_traducciones = collections.defaultdict(lambda: collections.defaultdict(int))
    
    for origen, destino in corpus:
        for p_orig in origen:
            for p_dest in destino:
                # Contamos cuántas veces aparecen juntas en el mismo par de frases
                conteo_traducciones[p_orig][p_dest] += 1
                
    return conteo_traducciones

# --- PRUEBA ---
traducciones = calcular_alineacion_basica(corpus_paralelo)

palabra_buscada = "negro"
posibles = traducciones[palabra_buscada]

print(f"Probabilidades de traducción para '{palabra_buscada}':")
total = sum(posibles.values())
for trad, count in posibles.items():
    prob = count / total
    print(f"  -> {trad}: {prob:.2%}")
  
