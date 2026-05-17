import numpy as np

def viterbi(observaciones, estados, prob_inicial, transicion, emision):
    T = len(observaciones)
    N = len(estados)
    
    # Matriz para guardar las probabilidades máximas
    viterbi_matrix = np.zeros((N, T))
    # Matriz para reconstruir el camino
    backpointer = np.zeros((N, T), dtype=int)
    
    # 1. Inicialización
    viterbi_matrix[:, 0] = prob_inicial * emision[:, observaciones[0]]
    
    # 2. Recursión (Paso hacia adelante)
    for t in range(1, T):
        for s in range(N):
            # Probabilidad de venir de cada estado anterior i y llegar a s
            prob_trans = viterbi_matrix[:, t-1] * transicion[:, s] * emision[s, observaciones[t]]
            viterbi_matrix[s, t] = np.max(prob_trans)
            backpointer[s, t] = np.argmax(prob_trans)
            
    # 3. Terminación y Reconstrucción del camino (Backtracking)
    mejor_camino = np.zeros(T, dtype=int)
    mejor_camino[T-1] = np.argmax(viterbi_matrix[:, T-1])
    
    for t in range(T-2, -1, -1):
        mejor_camino[t] = backpointer[mejor_camino[t+1], t+1]
        
    return [estados[i] for i in mejor_camino]

# --- DATOS DEL MODELO ---
# Estados: 0: Sano, 1: Gripe
estados_lista = ["Sano", "Gripe"]
# Obs: 0: Normal, 1: Estornudo, 2: Mareo
p_inicial = np.array([0.6, 0.4])
matriz_A = np.array([[0.7, 0.3], [0.3, 0.7]]) # Transición
matriz_B = np.array([[0.6, 0.3, 0.1], [0.1, 0.4, 0.5]]) # Emisión

# El paciente reporta: Normal -> Estornudo -> Mareo
secuencia_sintomas = [0, 1, 2]
diagnostico = viterbi(secuencia_sintomas, estados_lista, p_inicial, matriz_A, matriz_B)

print(f"Secuencia de síntomas: {[ 'Normal', 'Estornudo', 'Mareo' ][i] for i in secuencia_sintomas}")
print(f"Diagnóstico más probable (Viterbi): {' -> '.join(diagnostico)}")
