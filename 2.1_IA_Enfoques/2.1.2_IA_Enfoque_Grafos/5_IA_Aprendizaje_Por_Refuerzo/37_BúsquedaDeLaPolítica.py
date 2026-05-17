import random

def simular_entorno(theta):
    """Simula el éxito de una política basada en el parámetro theta."""
    # Supongamos que el valor óptimo oculto es 0.72
    objetivo = 0.72
    rendimiento = -abs(theta - objetivo) # Entre más cerca de 0.72, mejor
    return rendimiento

def busqueda_politica_estocastica(iteraciones=100):
    # 1. Inicializar política aleatoria
    theta_actual = random.random()
    mejor_rendimiento = simular_entorno(theta_actual)
    
    print(f"Política inicial: theta = {theta_actual:.4f} | Rendimiento: {mejor_rendimiento:.4f}")

    for i in range(iteraciones):
        # 2. Perturbar la política (Exploración de parámetros)
        variacion = random.uniform(-0.05, 0.05)
        nueva_theta = max(0, min(1, theta_actual + variacion))
        
        nuevo_rendimiento = simular_entorno(nueva_theta)
        
        # 3. Si es mejor, actualizar (Ascenso de colinas)
        if nuevo_rendimiento > mejor_rendimiento:
            theta_actual = nueva_theta
            mejor_rendimiento = nuevo_rendimiento
            
    return theta_actual, mejor_rendimiento

# --- EJECUCIÓN ---
mejor_theta, score = busqueda_politica_estocastica()

print(f"\nPolítica Óptima Encontrada: theta = {mejor_theta:.4f}")
print(f"Rendimiento Final: {score:.4f}")
