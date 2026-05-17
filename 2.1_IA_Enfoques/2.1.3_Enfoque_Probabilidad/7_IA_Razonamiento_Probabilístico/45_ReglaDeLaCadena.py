def regla_cadena_ejemplo():
    # Definimos las probabilidades condicionales (datos de entrenamiento)
    p_terremoto = 0.002
    p_alarma_dado_terremoto = 0.95
    p_llamada_dado_alarma = 0.80

    # Queremos calcular P(Terremoto AND Alarma AND Llamada)
    # Aplicando la Regla de la Cadena:
    # P(T, A, L) = P(T) * P(A | T) * P(L | A)
    
    p_conjunta = p_terremoto * p_alarma_dado_terremoto * p_llamada_dado_alarma
    
    print("Desglose de la Regla de la Cadena:")
    print(f"  1. P(Terremoto): {p_terremoto}")
    print(f"  2. P(Alarma | Terremoto): {p_alarma_dado_terremoto}")
    print(f"  3. P(Llamada | Alarma): {p_llamada_dado_alarma}")
    print("-" * 30)
    print(f"Probabilidad Conjunta Final: {p_conjunta:.6f}")

regla_cadena_ejemplo()
