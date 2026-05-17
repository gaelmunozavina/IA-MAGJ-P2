class AgenteBusquedaOnline:
    def __init__(self, meta):
        self.meta = meta
        self.visitados = set()
        # Mapa que el agente va construyendo: {estado: {accion: resultado}}
        self.mapa = {}
        # Pila para el retroceso (backtracking) físico
        self.camino_regreso = []

    def buscar(self, estado_actual, vecinos_disponibles):
        """
        Simula la decisión del agente en cada paso.
        vecinos_disponibles: Lista de nodos que el agente ve desde su posición actual.
        """
        print(f"Agente en: {estado_actual}")

        if estado_actual == self.meta:
            print("¡Meta encontrada!")
            return "EXITO"

        # Marcar el nodo actual como visitado
        if estado_actual not in self.visitados:
            self.visitados.add(estado_actual)

        # Buscar un vecino que no hayamos visitado (Exploración)
        for vecino in vecinos_disponibles:
            if vecino not in self.visitados:
                print(f"  Explorando nuevo camino hacia: {vecino}")
                self.camino_regreso.append(estado_actual) # Guardamos para volver
                return vecino

        # Si no hay vecinos nuevos, hacemos Backtracking (Retroceso)
        if self.camino_regreso:
            destino_regreso = self.camino_regreso.pop()
            print(f"  Callejón sin salida. Regresando a: {destino_regreso}")
            return destino_regreso

        return "FALLO"

# --- SIMULACIÓN DEL ENTORNO ---
# El agente NO conoce este grafo al inicio
grafo_desconocido = {
    'Inicio': ['A', 'B'],
    'A': ['Inicio', 'C', 'D'],
    'B': ['Inicio'],
    'C': ['A'],
    'D': ['A', 'Meta'],
    'Meta': ['D']
}

agente = AgenteBusquedaOnline(meta='Meta')
estado_actual = 'Inicio'

# Ciclo de vida del agente
for paso in range(15):
    vecinos = grafo_desconocido[estado_actual]
    proximo_paso = agente.buscar(estado_actual, vecinos)
    
    if proximo_paso == "EXITO":
        break
    elif proximo_paso == "FALLO":
        print("No se pudo encontrar la meta.")
        break
    
    estado_actual = proximo_paso
