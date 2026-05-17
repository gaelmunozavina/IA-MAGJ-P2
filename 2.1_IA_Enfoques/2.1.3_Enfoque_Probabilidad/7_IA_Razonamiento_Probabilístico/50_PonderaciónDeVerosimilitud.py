import random

# Definición de la Red Bayesiana (Probabilidades)
# Nube -> Lluvia -> Cesped
p_nube = 0.5
p_lluvia_dado_nube = {True: 0.8, False: 0.2}
p_cesped_dado_lluvia = {True: 0.9, False: 0.01} # Evidencia muy rara si no llueve

def likelihood_weighting(n_muestras, evidencia={'Cesped': True}):
    acumulador_pesos = {True: 0.0, False: 0.0} # Pesos para Lluvia=True/False

    for _ in range(n_muestras):
        w = 1.0
        
        # 1. Nodo Nube (No es evidencia, se muestrea normal)
        nube = random.random() < p_nube
        
        # 2. Nodo Lluvia (Variable que queremos consultar)
        llueve = random.random() < p_lluvia_dado_nube[nube]
        
        # 3. Nodo Cesped (Es evidencia, se FUERZA el valor)
        # En lugar de muestrear, multiplicamos el peso por la probabilidad de la evidencia
        valor_evidencia = evidencia['Cesped']
        w *= p_cesped_dado_lluvia[llueve] if valor_evidencia else (1 - p_cesped_dado_lluvia[llueve])
        
        # Acumulamos el peso en la categoría correspondiente de Lluvia
        acumulador_pesos[llueve] += w

    # Normalización final
    total_w = sum(acumulador_pesos.values())
    if total_w == 0: return {True: 0.5, False: 0.5}
    
    return {k: v / total_w for k, v in acumulador_pesos.items()}

# --- EJECUCIÓN ---
n = 10000
resultados = likelihood_weighting(n)

print(f"Resultados tras {n} muestras ponderadas:")
print(f"  P(Lluvia | Cesped=True) ≈ {resultados[True]:.4f}")
print(f"  P(~Lluvia | Cesped=True) ≈ {resultados[False]:.4f}")
print("\nNota: ¡Ninguna muestra fue rechazada!")
