import numpy as np

def aprendizaje_bayesiano_moneda(lanzamientos):
    # 1. Prior: Al principio creemos que cualquier probabilidad (0 a 1) es posible
    # (Distribución Uniforme)
    probabilidades_hipotesis = np.linspace(0, 1, 100)
    prior = np.ones(100) / 100
    
    creencia_actual = prior
    
    for i, resultado in enumerate(lanzamientos):
        # 2. Verosimilitud (Likelihood): 
        # Si salió Cara (1), las hipótesis con p alta son más probables.
        # Si salió Cruz (0), las hipótesis con p baja son más probables.
        if resultado == 1:
            likelihood = probabilidades_hipotesis
        else:
            likelihood = 1 - probabilidades_hipotesis
            
        # 3. Posterior: Prior * Likelihood (y normalizar)
        creencia_actual = creencia_actual * likelihood
        creencia_actual /= creencia_actual.sum()
        
    # Encontrar la hipótesis más probable (MAP - Maximum A Posteriori)
    indice_max = np.argmax(creencia_actual)
    return probabilidades_hipotesis[indice_max], creencia_actual

# --- ESCENARIO ---
# Lanzamos una moneda y sale: Cara, Cara, Cara, Cruz, Cara (4 Caras, 1 Cruz)
datos = [1, 1, 1, 0, 1]
estimacion, distribucion = aprendizaje_bayesiano_moneda(datos)

print(f"Tras {len(datos)} lanzamientos:")
print(f"  Estimación de la probabilidad de Cara: {estimacion:.2f}")
print(f"  (La IA ha 'aprendido' que la moneda tiende a salir cara)")
