import numpy as np

def evaluacion_politica(politica, estados, prob_transicion, recompensas, gamma):
    """Calcula la utilidad de los estados siguiendo la política actual."""
    V = {s: 0 for s in estados}
    for _ in range(100):  # Iteraciones para converger V
        V_nueva = {}
        for s in estados:
            a = politica[s]
            # Ecuación de Bellman simplificada para una acción fija
            V_nueva[s] = sum(p * (recompensas.get(s, -0.01) + gamma * V[s_sig]) 
                             for s_sig, p in prob_transicion[s][a].items())
        V = V_nueva
    return V

def iteracion_politicas(estados, acciones, prob_transicion, recompensas, gamma=0.9):
    """Algoritmo principal de Iteración de Políticas."""
    # 1. Inicializar política aleatoria
    politica = {s: acciones[0] for s in estados}
    estable = False

    while not estable:
        # 2. Evaluación
        V = evaluacion_politica(politica, estados, prob_transicion, recompensas, gamma)
        estable = True
        
        # 3. Mejora
        for s in estados:
            accion_vieja = politica[s]
            
            # Buscar la mejor acción según los valores V actuales
            mejor_accion = None
            mejor_valor = -float('inf')
            
            for a in acciones:
                valor_a = sum(p * (recompensas.get(s, -0.01) + gamma * V[s_sig]) 
                              for s_sig, p in prob_transicion[s][a].items())
                if valor_a > mejor_valor:
                    mejor_valor = valor_a
                    mejor_accion = a
            
            politica[s] = mejor_accion
            if accion_vieja != mejor_accion:
                estable = False # La política aún está cambiando

    return politica, V

# --- CONFIGURACIÓN ---
estados_simples = ['A', 'B', 'Meta']
acciones_simples = ['Derecha', 'Izquierda']
recompensas_simples = {'Meta': 10, 'A': -1, 'B': -1}
prob_trans = {
    'A': {'Derecha': {'B': 1.0}, 'Izquierda': {'A': 1.0}},
    'B': {'Derecha': {'Meta': 1.0}, 'Izquierda': {'A': 1.0}},
    'Meta': {'Derecha': {'Meta': 1.0}, 'Izquierda': {'Meta': 1.0}}
}

mejor_pi, valores_pi = iteracion_politicas(estados_simples, acciones_simples, prob_trans, recompensas_simples)

print("Política Óptima:")
for s, a in mejor_pi.items():
    print(f" En {s} hacer {a}")
