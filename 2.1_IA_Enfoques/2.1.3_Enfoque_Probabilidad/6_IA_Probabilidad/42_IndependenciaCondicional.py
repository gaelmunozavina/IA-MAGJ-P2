def comprobar_independencia_condicional():
    # Supongamos: P(Lluvia) = 0.2
    # P(Césped_Mojado | Lluvia) = 0.95
    # P(Zapatos_Mojados | Lluvia) = 0.8
    
    # Si YA SABEMOS que está lloviendo (Evento C)
    p_a_dado_c = 0.95 # P(Césped|Lluvia)
    p_b_dado_c = 0.8  # P(Zapatos|Lluvia)
    
    # Por Independencia Condicional: P(Césped Y Zapatos | Lluvia)
    p_conjunta_condicionada = p_a_dado_c * p_b_dado_c
    
    print(f"Probabilidad de Césped Mojado dado que llueve: {p_a_dado_c}")
    print(f"Probabilidad de Zapatos Mojados dado que llueve: {p_b_dado_c}")
    print(f"Probabilidad de ambos eventos simultáneos: {p_conjunta_condicionada:.2f}")
    print("\nConclusión: Sabiendo que llueve, la probabilidad de uno no afecta al otro.")

comprobar_independencia_condicional()
