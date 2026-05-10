import random

class MDP:
    def __init__(self, estados, acciones, transiciones, recompensas, gamma=0.9):
        self.estados = estados
        self.acciones = acciones
        self.transiciones = transiciones  # {s: {a: {s_sig: prob}}}
        self.recompensas = recompensas      # {s: valor}
        self.gamma = gamma

    def obtener_transicion(self, s, a):
        """Retorna las probabilidades de transición para un estado y acción."""
        return self.transiciones.get(s, {}).get(a, {})

    def simular_paso(self, s, a):
        """Simula una transición estocástica en el entorno."""
        probabilidades = self.obtener_transicion(s, a)
        if not probabilidades:
            return s, self.recompensas.get(s, 0)
        
        # Elegir siguiente estado basado en las probabilidades
        s_siguiente = random.choices(
            list(probabilidades.keys()), 
            weights=list(probabilidades.values())
        )[0]
        
        recompensa = self.recompensas.get(s_siguiente, 0)
        return s_siguiente, recompensa

# --- INSTANCIA DE EJEMPLO: El Robot en el Pasillo ---
estados_mdp = ['Pasillo', 'Meta', 'Fuego']
acciones_mdp = ['Mover', 'Quedarse']

# El robot intenta moverse a la Meta, pero hay 20% de probabilidad de caer al Fuego
trans_mdp = {
    'Pasillo': {
        'Mover': {'Meta': 0.8, 'Fuego': 0.2},
        'Quedarse': {'Pasillo': 1.0}
    }
}

recomp_mdp = {'Meta': 100, 'Fuego': -50, 'Pasillo': -1}

mundo = MDP(estados_mdp, acciones_mdp, trans_mdp, recomp_mdp)

# Simulación de un intento
estado_actual = 'Pasillo'
accion = 'Mover'
nuevo_estado, premio = mundo.simular_paso(estado_actual, accion)

print(f"Agente estaba en {estado_actual}, hizo {accion}.")
print(f"Resultado: Llegó a {nuevo_estado} y recibió {premio} puntos.")
