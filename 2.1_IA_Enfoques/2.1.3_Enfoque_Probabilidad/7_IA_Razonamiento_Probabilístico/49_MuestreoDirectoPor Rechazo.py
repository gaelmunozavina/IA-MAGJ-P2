import random

def muestreo_por_rechazo(n_muestras, evidencia_cesped=True):
    muestras_aceptadas = []
    
    for _ in range(n_muestras):
        # 1. Muestreo Directo (Generar la muestra)
        llueve = random.random() < 0.2
        
        # P(Cesped | Lluvia)
        prob_cesped = 0.9 if llueve else 0.4
        esta_mojado = random.random() < prob_cesped
        
        # 2. Lógica de Rechazo
        # Solo nos interesan las muestras que coinciden con la evidencia
        if esta_mojado == evidencia_cesped:
            muestras_aceptadas.append(llueve)
            
    if not muestras_aceptadas:
        return 0
        
    # Calcular proporción de éxito en las muestras válidas
    prob_estimada = sum(muestras_aceptadas) / len(muestras_aceptadas)
    return prob_estimada, len(muestras_aceptadas)

# --- EJECUCIÓN ---
n = 10000
resultado, validas = muestreo_por_rechazo(n)

print(f"Total de simulaciones: {n}")
print(f"Muestras que cumplieron la evidencia: {validas}")
print(f"Probabilidad estimada P(Lluvia | Cesped=True): {resultado:.4f}")
