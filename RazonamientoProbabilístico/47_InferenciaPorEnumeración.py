def inferencia_por_enumeracion():
    # 1. Definición de la Red (Probabilidades)
    p_lluvia = {True: 0.2, False: 0.8}
    
    # P(Cesped | Lluvia)
    p_cesped_dado_lluvia = {
        True:  {True: 0.9, False: 0.1},
        False: {True: 0.4, False: 0.6}
    }

    # Consulta: P(Lluvia | Cesped=True)
    # Evidencia: Cesped = True
    # No hay variables ocultas en este modelo miniatura, 
    # pero calculamos los dos casos de la consulta:
    
    # Caso A: P(Lluvia=True, Cesped=True)
    res_true = p_lluvia[True] * p_cesped_dado_lluvia[True][True]
    
    # Caso B: P(Lluvia=False, Cesped=True)
    res_false = p_lluvia[False] * p_cesped_dado_lluvia[False][True]
    
    # 2. Normalización (Alpha)
    total = res_true + res_false
    prob_final_true = res_true / total
    prob_final_false = res_false / total

    print(f"Resultados antes de normalizar: True={res_true:.3f}, False={res_false:.3f}")
    print(f"Probabilidades Finales (Normalizadas):")
    print(f"  P(Lluvia | Cesped=True): {prob_final_true:.4f}")
    print(f"  P(~Lluvia | Cesped=True): {prob_final_false:.4f}")

inferencia_por_enumeracion()
