def normalizar(distribucion_prob):
    """
    Ajusta una lista de valores para que su suma sea exactamente 1.0.
    """
    total = sum(distribucion_prob.values())
    
    if total == 0:
        return {k: 1/len(distribucion_prob) for k in distribucion_prob} # Distribución uniforme si no hay datos
        
    return {estado: prob / total for estado, prob in distribucion_prob.items()}

# --- ESCENARIO ---
# El agente tiene estas probabilidades 'crudas' tras observar el entorno:
creencias_sucias = {
    "Cocina": 0.45,
    "Sala": 0.15,
    "Baño": 0.05
}

print(f"Suma inicial: {sum(creencias_sucias.values())}") # Suma 0.65

# Aplicamos normalización
creencias_finales = normalizar(creencias_sucias)

print("\nCreencias Normalizadas (Distribución Final):")
for lugar, prob in creencias_finales.items():
    print(f"  - {lugar}: {prob:.4f}")

print(f"\nSuma final: {sum(creencias_finales.values()):.1f}")
