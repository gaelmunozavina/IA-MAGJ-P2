def actualizar_creencia(prior_fallo, sensibilidad_test, especificidad_test, evidencia):
    """
    Calcula la probabilidad de fallo dado un reporte de error.
    
    prior_fallo: P(Fallo)
    sensibilidad_test: P(Reporte|Fallo)
    especificidad_test: P(No_Reporte|No_Fallo)
    evidencia: True si hubo reporte, False si no.
    """
    p_no_fallo = 1 - prior_fallo
    
    if evidencia:
        # P(Reporte) = P(Reporte|Fallo)P(Fallo) + P(Reporte|No_Fallo)P(No_Fallo)
        p_reporte_dado_no_fallo = 1 - especificidad_test
        verosimilitud = (sensibilidad_test * prior_fallo) + (p_reporte_dado_no_fallo * p_no_fallo)
        
        # Bayes: P(Fallo|Reporte)
        posterior = (sensibilidad_test * prior_fallo) / verosimilitud
    else:
        # P(Fallo|No_Reporte)
        p_no_reporte_dado_fallo = 1 - sensibilidad_test
        verosimilitud = (p_no_reporte_dado_fallo * prior_fallo) + (especificidad_test * p_no_fallo)
        posterior = (p_no_reporte_dado_fallo * prior_fallo) / verosimilitud
        
    return posterior

# --- ESCENARIO ---
# P(Fallo) inicial es muy baja: 0.1%
# El sistema de monitoreo detecta el 99% de los fallos (sensibilidad)
# Pero da falsas alarmas el 5% de las veces (especificidad del 95%)

prob_final = actualizar_creencia(0.001, 0.99, 0.95, True)

print(f"Probabilidad inicial de fallo: 0.1%")
print(f"Evidencia recibida: ¡REPORTE DE ERROR EN CONSOLA!")
print(f"Nueva probabilidad de fallo real: {prob_final * 100:.2f}%")
