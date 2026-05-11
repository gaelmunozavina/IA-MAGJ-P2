import collections

def modelo_lenguaje_simple(texto_audio):
    # Simulamos una salida ruidosa del modelo acústico
    # El sensor escuchó algo que podría ser 'casa' o 'caza'
    opciones = {
        "la": ["la"],
        "caSA_o_caZA": ["casa", "caza"],
        "es": ["es"],
        "grande": ["grande"]
    }

    # Probabilidades de Bigramas (Modelo de Lenguaje W)
    # P(palabra_actual | palabra_anterior)
    prob_bigramas = {
        ("la", "casa"): 0.9,
        ("la", "caza"): 0.1,
    }

    secuencia_final = ["la"]
    
    # Decisión basada en contexto (Probabilidad de Markov)
    palabra_anterior = "la"
    posibles_actuales = opciones["caSA_o_caZA"]
    
    # Elegir la que tenga mayor probabilidad de bigrama
    mejor_palabra = max(posibles_actuales, 
                        key=lambda p: prob_bigramas.get((palabra_anterior, p), 0.01))
    
    secuencia_final.append(mejor_palabra)
    secuencia_final.extend(["es", "grande"])
    
    return " ".join(secuencia_final)

# --- EJECUCIÓN ---
resultado = modelo_lenguaje_simple("la ca[sa/za] es grande")
print(f"Audio ruidoso procesado por Modelo de Lenguaje:")
print(f"  Resultado: '{resultado}'")
