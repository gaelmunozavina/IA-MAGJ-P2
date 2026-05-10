import numpy as np

# Configuración del entorno
estados = 5  # [0, 1, 2, 3, META]
acciones = 2 # 0: Izquierda, 1: Derecha
q_table = np.zeros((estados, acciones))

# Hiperparámetros
alpha = 0.5
gamma = 0.9
episodios = 100

for _ in range(episodios):
    estado = 0 # Iniciar siempre en la izquierda
    while estado < estados - 1:
        # Acción simple: siempre ir a la derecha (para fines de demostración)
        accion = 1 
        
        # El mundo responde
        s_siguiente = estado + 1
        recompensa = 100 if s_siguiente == estados - 1 else -1
        
        # Actualización de Q-Learning
        mejor_q_siguiente = np.max(q_table[s_siguiente])
        q_table[estado, accion] += alpha * (recompensa + gamma * mejor_q_siguiente - q_table[estado, accion])
        
        estado = s_siguiente

print("Tabla Q Final (Filas=Estados, Columnas=[Izq, Der]):")
print(q_table)
