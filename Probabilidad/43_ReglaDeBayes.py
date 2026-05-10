def regla_de_bayes(prior_h, likelihood_e_h, likelihood_e_not_h):
    """
    Calcula P(H|E) usando la Regla de Bayes.
    
    prior_h: P(H)
    likelihood_e_h: P(E|H)
    likelihood_e_not_h: P(E|~H)
    """
    # 1. Calcular la probabilidad total de la evidencia P(E)
    # P(E) = P(E|H)P(H) + P(E|~H)P(~H)
    prior_not_h = 1 - prior_h
    p_evidencia = (likelihood_e_h * prior_h) + (likelihood_e_not_h * prior_not_h)
    
    # 2. Aplicar la fórmula
    posterior = (likelihood_e_h * prior_h) / p_evidencia
    
    return posterior

# --- EJEMPLO: Diagnóstico de Sensor ---
# Prior: Hay un 5% de probabilidad de que el motor falle.
# Sensibilidad: Si falla, el sensor avisa el 99% de las veces.
# Falsa Alarma: Si NO falla, el sensor avisa el 10% de las veces.

prob_fallo_real = regla_de_bayes(0.05, 0.99, 0.10)

print(f"Probabilidad A Priori de fallo: 5%")
print(f"El sensor se activa (Evidencia).")
print(f"Probabilidad A Posteriori de fallo real: {prob_fallo_real * 100:.2f}%")
