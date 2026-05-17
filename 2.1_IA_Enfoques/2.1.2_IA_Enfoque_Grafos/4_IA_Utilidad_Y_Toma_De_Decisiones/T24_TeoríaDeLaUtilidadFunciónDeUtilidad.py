class AgenteRacional:
    def __init__(self, utilidades):
        """
        utilidades: Diccionario {estado: valor_utilidad}
        """
        self.utilidades = utilidades

    def calcular_utilidad_esperada(self, escenarios):
        """
        escenarios: Lista de tuplas (probabilidad, estado)
        """
        eu = sum(prob * self.utilidades[estado] for prob, estado in escenarios)
        return eu

# --- CONFIGURACIÓN DEL ESCENARIO ---
# Definimos qué tanto valora el agente ciertos resultados (Función de Utilidad)
utilidades_agente = {
    "gran_ganancia": 100,
    "ganancia_moderada": 50,
    "sin_cambio": 0,
    "perdida_pequeña": -20,
    "quiebra": -200
}

# Definimos dos posibles acciones con sus probabilidades
# Acción A: Inversión de alto riesgo
accion_riesgosa = [
    (0.2, "gran_ganancia"),
    (0.5, "sin_cambio"),
    (0.3, "quiebra")
]

# Acción B: Inversión segura
accion_segura = [
    (0.1, "ganancia_moderada"),
    (0.8, "sin_cambio"),
    (0.1, "perdida_pequeña")
]

# --- TOMA DE DECISIÓN ---
agente = AgenteRacional(utilidades_agente)

eu_riesgosa = agente.calcular_utilidad_esperada(accion_riesgosa)
eu_segura = agente.calcular_utilidad_esperada(accion_segura)

print(f"Utilidad Esperada (Riesgosa): {eu_riesgosa}")
print(f"Utilidad Esperada (Segura): {eu_segura}")

if eu_riesgosa > eu_segura:
    print("El agente elige la acción RIESGOSA.")
else:
    print("El agente elige la acción SEGURA.")
