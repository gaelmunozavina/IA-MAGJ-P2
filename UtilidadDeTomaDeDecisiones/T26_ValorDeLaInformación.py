class AnalisisInformacion:
    def __init__(self, prob_exito, utilidad_exito, costo_perforacion):
        self.p_exito = prob_exito
        self.p_fallo = 1 - prob_exito
        self.u_exito = utilidad_exito - costo_perforacion
        self.u_fallo = -costo_perforacion
        self.u_no_hacer_nada = 0

    def utilidad_sin_informacion(self):
        # El agente elige entre perforar (EU) o no hacer nada (0)
        eu_perforar = (self.p_exito * self.u_exito) + (self.p_fallo * self.u_fallo)
        return max(eu_perforar, self.u_no_hacer_nada)

    def utilidad_con_informacion_perfecta(self):
        # Si la información dice "Hay petróleo", perforamos (u_exito)
        # Si la información dice "No hay", no hacemos nada (0)
        eu_con_vpi = (self.p_exito * self.u_exito) + (self.p_fallo * self.u_no_hacer_nada)
        return eu_con_vpi

    def calcular_vpi(self):
        vpi = self.utilidad_con_informacion_perfecta() - self.utilidad_sin_informacion()
        return vpi

# --- ESCENARIO ---
# Probabilidad de encontrar petróleo: 20%
# Ganancia si hay: 1,000,000 | Costo de perforar: 150,000
estudio = AnalisisInformacion(prob_exito=0.2, utilidad_exito=1000000, costo_perforacion=150000)

sin_info = estudio.utilidad_sin_informacion()
vpi = estudio.calcular_vpi()

print(f"Utilidad esperada actual: ${sin_info:,.2f}")
print(f"VALOR DE LA INFORMACIÓN (VPI): ${vpi:,.2f}")
print(f"\nInterpretación: No deberías pagar más de ${vpi:,.2f} por el estudio geológico.")
