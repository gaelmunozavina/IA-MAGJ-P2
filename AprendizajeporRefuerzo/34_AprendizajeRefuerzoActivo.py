import random

class AgenteQLearning:
    def __init__(self, estados, acciones, alpha=0.1, gamma=0.9, epsilon=0.2):
        # Tabla Q: {estado: {accion: valor}}
        self.q_table = {s: {a: 0.0 for a in acciones} for s in estados}
        self.alpha = alpha     # Tasa de aprendizaje
        self.gamma = gamma     # Descuento
        self.epsilon = epsilon # Probabilidad de exploración

    def elegir_accion(self, estado):
        # Estrategia Epsilon-Greedy
        if random.random() < self.epsilon:
            return random.choice(list(self.q_table[estado].keys())) # Explorar
        else:
            # Explotar: elegir la acción con el valor Q más alto
            return max(self.q_table[estado], key=self.q_table[estado].get)

    def aprender(self, s, a, r, s_sig):
        # Valor Q máximo del siguiente estado
        max_q_sig = max(self.q_table[s_sig].values())
        
        # Actualización de la tabla Q
        target = r + self.gamma * max_q_sig
        self.q_table[s][a] += self.alpha * (target - self.q_table[s][a])

# --- ENTRENAMIENTO ---
estados = ['Inicio', 'Pasillo', 'Meta']
acciones = ['Izquierda', 'Derecha']
agente = AgenteQLearning(estados, acciones)

# Simulación de 500 pasos de entrenamiento
estado_actual = 'Inicio'
for _ in range(500):
    accion = agente.elegir_accion(estado_actual)
    
    # Lógica simple del mundo
    if estado_actual == 'Inicio' and accion == 'Derecha':
        s_siguiente, recompensa = 'Pasillo', -1
    elif estado_actual == 'Pasillo' and accion == 'Derecha':
        s_siguiente, recompensa = 'Meta', 100
    else:
        s_siguiente, recompensa = estado_actual, -2 # Castigo por chocar o ir atrás
        
    agente.aprender(estado_actual, accion, recompensa, s_siguiente)
    estado_actual = s_siguiente if s_siguiente != 'Meta' else 'Inicio'

print("Tabla Q aprendida (Valores Estado-Acción):")
for s, valores in agente.q_table.items():
    print(f"  {s}: {valores}")
  
