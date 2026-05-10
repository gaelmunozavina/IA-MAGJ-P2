import random

class Bandit:
    def __init__(self, prob_exito):
        self.prob = prob_exito
    
    def jalar(self):
        return 1 if random.random() < self.prob else 0

def simular_exploracion(epsilon, pasos=1000):
    bandidos = [Bandit(0.1), Bandit(0.5), Bandit(0.8)] # El 3ro es el mejor
    recompensas_estimadas = [0.0, 0.0, 0.0]
    conteos = [0, 0, 0]
    total_recompensa = 0

    for _ in range(pasos):
        # Decisión Epsilon-Greedy
        if random.random() < epsilon:
            eleccion = random.randint(0, 2) # Explorar
        else:
            eleccion = recompensas_estimadas.index(max(recompensas_estimadas)) # Explotar

        # Obtener recompensa
        r = bandidos[eleccion].jalar()
        total_recompensa += r
        
        # Actualizar conocimiento (Media móvil)
        conteos[eleccion] += 1
        n = conteos[eleccion]
        recompensas_estimadas[eleccion] = ((n - 1) * recompensas_estimadas[eleccion] + r) / n
    
    return total_recompensa, recompensas_estimadas

# --- PRUEBA CON DIFERENTES EPSILONS ---
for e in [0.0, 0.1, 0.5]:
    puntos, estimaciones = simular_exploracion(e)
    print(f"Epsilon: {e} | Recompensa Total: {puntos} | Estimaciones finales: {estimaciones}")
  
