class JuegoMatriz:
    def __init__(self, matriz):
        """
        matriz: Diccionario {(accion_A, accion_B): (pago_A, pago_B)}
        """
        self.matriz = matriz
        self.acciones = ['Cooperar', 'Traicionar']

    def analizar_equilibrio(self):
        print("Analizando Dilema del Prisionero...")
        for a1 in self.acciones:
            for a2 in self.acciones:
                pago = self.matriz[(a1, a2)]
                print(f"Si A elige {a1} y B elige {a2} -> Pagos: A={pago[0]}, B={pago[1]}")

    def buscar_estrategia_dominante(self):
        # En el dilema del prisionero, Traicionar domina a Cooperar
        # ya que siempre da un mejor resultado individual sin importar el otro.
        return "Traicionar"

# --- CONFIGURACIÓN ---
# Los pagos representan años de cárcel (queremos el número menor)
# (Accion_A, Accion_B): (Años_A, Años_B)
dilema_prisionero = {
    ('Cooperar', 'Cooperar'): (-1, -1),
    ('Cooperar', 'Traicionar'): (-3, 0),
    ('Traicionar', 'Cooperar'): (0, -3),
    ('Traicionar', 'Traicionar'): (-2, -2)
}

juego = JuegoMatriz(dilema_prisionero)
juego.analizar_equilibrio()

dominante = juego.buscar_estrategia_dominante()
print(f"\nLa estrategia racional (egoísta) es: {dominante}")
