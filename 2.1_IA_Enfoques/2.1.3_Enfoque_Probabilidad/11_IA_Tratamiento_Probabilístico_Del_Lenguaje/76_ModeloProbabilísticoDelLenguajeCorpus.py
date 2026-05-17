import collections
import random

def entrenar_modelo_bigramas(corpus):
    # Tokenización simple
    palabras = corpus.lower().split()
    modelo = collections.defaultdict(lambda: collections.defaultdict(int))
    
    # Contar transiciones entre palabras
    for i in range(len(palabras) - 1):
        actual = palabras[i]
        siguiente = palabras[i+1]
        modelo[actual][siguiente] += 1
        
    return modelo

def generar_texto(modelo, inicio, longitud=10):
    frase = [inicio]
    palabra_actual = inicio
    
    for _ in range(longitud - 1):
        opciones = modelo[palabra_actual]
        if not opciones:
            break
        # Elegir la siguiente palabra basada en la frecuencia
        posibles = list(opciones.keys())
        pesos = list(opciones.values())
        siguiente = random.choices(posibles, weights=pesos)[0]
        
        frase.append(siguiente)
        palabra_actual = siguiente
        
    return " ".join(frase)

# --- ESCENARIO ---
corpus_ejemplo = """
la inteligencia artificial es el futuro de la tecnologia 
la inteligencia artificial aprende de los datos 
el futuro es hoy con la tecnologia actual
"""

modelo_entrenado = entrenar_modelo_bigramas(corpus_ejemplo)
resultado = generar_texto(modelo_entrenado, "la", longitud=6)

print(f"Corpus procesado. Texto generado:")
print(f"  > '{resultado}'")
