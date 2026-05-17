class RedBayesianaSimple:
    def __init__(self):
        # P(Lluvia)
        self.prior_lluvia = 0.2
        
        # P(CespedMojado | Lluvia)
        # {Lluvia: {Cesped: Prob}}
        self.cpt_cesped = {
            True:  {True: 0.9, False: 0.1}, # Si llueve, 90% mojado
            False: {True: 0.4, False: 0.6}  # Si no llueve, 40% mojado (quizás por el rociador)
        }

    def inferir_cesped_dado_lluvia(self, hubo_lluvia):
        prob_mojado = self.cpt_cesped[hubo_lluvia][True]
        return prob_mojado

    def probabilidad_conjunta(self, llueve, mojado):
        # P(L, M) = P(M | L) * P(L)
        p_l = self.prior_lluvia if llueve else (1 - self.prior_lluvia)
        p_m_dado_l = self.cpt_cesped[llueve][mojado]
        return p_m_dado_l * p_l

# --- PRUEBA ---
red = RedBayesianaSimple()
p_conjunta = red.probabilidad_conjunta(llueve=True, mojado=True)

print(f"Probabilidad de que llueva y el césped esté mojado: {p_conjunta:.4f}")
