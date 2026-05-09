import random

def calcular_fitness(individuo, objetivo):
    """Mide qué tan cerca está la suma del individuo al objetivo (menor es mejor)."""
    return abs(objetivo - sum(individuo))

def crear_individuo(longitud):
    """Crea una lista de números aleatorios."""
    return [random.randint(0, 50) for _ in range(longitud)]

def crossover(padre1, padre2):
    """Combina la mitad de cada padre para crear un hijo."""
    punto = len(padre1) // 2
    return padre1[:punto] + padre2[punto:]

def mutar(individuo, probabilidad=0.1):
    """Cambia un gen (número) al azar con una probabilidad dada."""
    if random.random() < probabilidad:
        indice = random.randint(0, len(individuo) - 1)
        individuo[indice] = random.randint(0, 50)
    return individuo

def algoritmo_genetico(objetivo, tamaño_poblacion=20, generaciones=100):
    # 1. Crear población inicial
    poblacion = [crear_individuo(5) for _ in range(tamaño_poblacion)]
    
    for gen in range(generaciones):
        # 2. Evaluar y ordenar por fitness (el mejor primero)
        poblacion = sorted(poblacion, key=lambda ind: calcular_fitness(ind, objetivo))
        
        # Si encontramos la solución perfecta, terminamos
        if sum(poblacion[0]) == objetivo:
            print(f"¡Solución encontrada en Gen {gen}!")
            break
            
        # 3. Selección: Nos quedamos con la mejor mitad (elite)
        elite = poblacion[:tamaño_poblacion // 2]
        nueva_poblacion = list(elite)
        
        # 4. Reproducción: Creamos hijos hasta completar la población
        while len(nueva_poblacion) < tamaño_poblacion:
            p1, p2 = random.sample(elite, 2)
            hijo = crossover(p1, p2)
            hijo = mutar(hijo)
            nueva_poblacion.append(hijo)
            
        poblacion = nueva_poblacion
        
        if gen % 20 == 0:
            print(f"Gen {gen}: Mejor suma = {sum(poblacion[0])} (Fitness: {calcular_fitness(poblacion[0], objetivo)})")

    return poblacion[0]

# --- EJECUCIÓN ---
meta_suma = 150
mejor_individuo = algoritmo_genetico(objetivo=meta_suma)

print(f"\nResultado Final: {mejor_individuo}")
print(f"Suma alcanzada: {sum(mejor_individuo)}")
