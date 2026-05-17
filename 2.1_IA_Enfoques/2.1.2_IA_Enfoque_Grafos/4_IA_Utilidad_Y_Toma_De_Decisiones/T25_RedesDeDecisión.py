class RedDecisionSimple:
    def __init__(self):
        # Probabilidades del Clima (Nodo de Azar)
        self.prob_clima = {"Lluvia": 0.3, "Soleado": 0.7}
        
        # Probabilidad del Pronóstico dado el Clima (Incertidumbre del sensor)
        self.prob_pronostico = {
            "Lluvia": {"Dice_Lluvia": 0.9, "Dice_Sol": 0.1},
            "Soleado": {"Dice_Lluvia": 0.2, "Dice_Sol": 0.8}
        }
        
        # Función de Utilidad (Nodo de Utilidad)
        # U(Clima, Decision)
        self.utilidad = {
            ("Lluvia", "Llevar_Paraguas"): 70,
            ("Lluvia", "No_Llevar"): 0,
            ("Soleado", "Llevar_Paraguas"): 20,
            ("Soleado", "No_Llevar"): 100
        }

    def calcular_mejor_decision(self, observacion_pronostico):
        print(f"Pronóstico recibido: {observacion_pronostico}")
        mejores_decisiones = {}
        
        for accion in ["Llevar_Paraguas", "No_Llevar"]:
            eu = 0
            # Aplicamos Bayes para saber la prob. real de clima dado el pronóstico
            # Simplificado: sumamos (P(Clima) * P(Pronóstico|Clima) * Utilidad)
            for clima in ["Lluvia", "Soleado"]:
                p_c = self.prob_clima[clima]
                p_p_c = self.prob_pronostico[clima][observacion_pronostico]
                u = self.utilidad[(clima, accion)]
                
                eu += p_c * p_p_c * u
            
            mejores_decisiones[accion] = eu
            print(f"  Acción: {accion} -> Utilidad Esperada: {eu:.2f}")

        return max(mejores_decisiones, key=mejores_decisiones.get)

# --- EJECUCIÓN ---
red = RedDecisionSimple()
decision_final = red.calcular_mejor_decision("Dice_Lluvia")

print(f"\nResultado: El agente decide {decision_final.upper()}")
