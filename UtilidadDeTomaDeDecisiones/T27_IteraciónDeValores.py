import copy

def iteracion_valores(estados, acciones, prob_transicion, recompensas, gamma=0.9, epsilon=0.01):
    """
    Algoritmo de Iteración de Valores para resolver un MDP.
    """
    # Inicializar utilidades en 0
    V = {s: 0 for s in estados}
    
    while True:
        V_nueva = copy.deepcopy(V)
        delta = 0
        
        for s in estados:
            if s == 'Meta' or s == 'Peligro':
                continue
                
            # Calcular el valor para cada acción y elegir el máximo (Bellman)
            valores_acciones = []
            for a in acciones:
                suma_utilidad = 0
                for s_primera in estados:
                    p = prob_transicion[s][a].get(s_primera, 0)
                    r = recompensas.get(s, -0.04) # Recompensa por paso (costo de vida)
                    suma_utilidad += p * (r + gamma * V[s_primera])
                valores_acciones.append(suma_utilidad)
            
            V_nueva[s] = max(valores_acciones)
            delta = max(delta, abs(V_nueva[s] - V[s]))
        
        V = V_nueva
        # Condición de convergencia
        if delta < epsilon * (1 - gamma) / gamma:
            break
            
    return V

# --- CONFIGURACIÓN DEL MDP ---
estados = ['S1', 'S2', 'Meta', 'Peligro']
acciones = ['Norte', 'Sur']
recompensas = {'Meta': 1.0, 'Peligro': -1.0, 'S1': -0.04, 'S2': -0.04}

# Probabilidades: 80% éxito, 20% quedarse igual
prob_transicion = {
    'S1': {'Norte': {'S2': 0.8, 'S1': 0.2}, 'Sur': {'S1': 1.0}},
    'S2': {'Norte': {'Meta': 0.8, 'S2': 0.2}, 'Sur': {'S1': 0.8, 'S2': 0.2}}
}

utilidades_finales = iteracion_valores(estados, acciones, prob_transicion, recompensas)

print("Utilidades finales de los estados:")
for s, v in utilidades_finales.items():
    print(f"Estado {s}: {v:.4f}")
