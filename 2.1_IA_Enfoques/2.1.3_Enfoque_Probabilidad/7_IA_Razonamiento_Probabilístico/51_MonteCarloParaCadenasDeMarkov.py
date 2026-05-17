import random
from collections import Counter

# Definición de la Red: Nube -> Lluvia -> Cesped
# Queremos P(Nube | Cesped=True)
p_nube = 0.5
p_lluvia = {True: 0.8, False: 0.2} # Dado Nube
p_cesped = {True: 0.9, False: 0.1} # Dado Lluvia

def gibbs_sampling(iteraciones, evidencia={'Cesped': True}):
    # 1. Inicialización de variables no-evidencia
    estado_actual = {
        'Nube': random.choice([True, False]),
        'Lluvia': random.choice([True, False]),
        'Cesped': evidencia['Cesped']
    }
    
    conteo = Counter()

    for _ in range(iteraciones):
        # 2. Muestrear 'Nube' dado sus hijos (Lluvia)
        # Aplicamos Bayes simplificado sobre el Manto de Markov
        p_n_true = p_nube * (p_lluvia[True] if estado_actual['Lluvia'] else (1 - p_lluvia[True]))
        p_n_false = (1 - p_nube) * (p_lluvia[False] if estado_actual['Lluvia'] else (1 - p_lluvia[False]))
        
        # Normalizar y actualizar
        norm = p_n_true + p_n_false
        estado_actual['Nube'] = random.random() < (p_n_true / norm)

        # 3. Muestrear 'Lluvia' dados sus padres (Nube) e hijos (Cesped)
        p_l_true = p_lluvia[estado_actual['Nube']] * (p_cesped[True] if estado_actual['Cesped'] else (1 - p_cesped[True]))
        p_l_false = (1 - p_lluvia[estado_actual['Nube']]) * (p_cesped[False] if estado_actual['Cesped'] else (1 - p_cesped[False]))
        
        norm_l = p_l_true + p_l_false
        estado_actual['Lluvia'] = random.random() < (p_l_true / norm_l)

        # Registramos el estado de la variable de interés
        conteo[estado_actual['Nube']] += 1

    return {k: v / iteraciones for k, v in conteo.items()}

# --- EJECUCIÓN ---
n_iter = 20000
resultados = gibbs_sampling(n_iter)

print(f"Resultados MCMC (Gibbs) tras {n_iter} iteraciones:")
print(f"  P(Nube | Cesped=True) ≈ {resultados[True]:.4f}")
print(f"  P(~Nube | Cesped=True) ≈ {resultados[False]:.4f}")
