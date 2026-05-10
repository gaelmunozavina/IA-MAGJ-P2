class RedBayesianaEstructura:
    def __init__(self):
        # Representación de arcos: (Padre -> Hijo)
        self.arcos = [
            ('Nube', 'Lluvia'), ('Nube', 'Rociador'),
            ('Lluvia', 'Cesped'), ('Rociador', 'Cesped'),
            ('Cesped', 'Zapatos_Mojados')
        ]

    def obtener_manto_markov(self, nodo):
        padres = {p for p, h in self.arcos if h == nodo}
        hijos = {h for p, h in self.arcos if p == nodo}
        conyuges = set()
        
        for hijo in hijos:
            otros_padres = {p for p, h in self.arcos if h == hijo and p != nodo}
            conyuges.update(otros_padres)
            
        manto = padres | hijos | conyuges
        return {
            "Padres": padres,
            "Hijos": hijos,
            "Conyuges": conyuges,
            "Total": manto
        }

# --- PRUEBA PARA EL NODO 'Lluvia' ---
red = RedBayesianaEstructura()
manto_lluvia = red.obtener_manto_markov('Lluvia')

print(f"Manto de Markov para 'Lluvia':")
print(f"  - Padres: {manto_lluvia['Padres']}")
print(f"  - Hijos: {manto_lluvia['Hijos']}")
print(f"  - Cónyuges (otros padres de sus hijos): {manto_lluvia['Conyuges']}")
print(f"  => El agente solo necesita estos {len(manto_lluvia['Total'])} nodos para saber todo sobre 'Lluvia'.")
