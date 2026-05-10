import matplotlib.pyplot as plt

def visualizar_prior(cuadrantes, probabilidades):
    """
    Dibuja la creencia inicial (prior) del agente sobre la ubicación.
    """
    plt.bar(cuadrantes, probabilidades, color='skyblue')
    plt.xlabel('Zonas del Mapa')
    plt.ylabel('Probabilidad a Priori P(H)')
    plt.title('Creencia Inicial del Agente')
    plt.ylim(0, 1)
    plt.show()

# --- CONFIGURACIÓN ---
# El agente sabe por historial que los intrusos suelen entrar por la 'Zona A'
zonas = ['Zona A', 'Zona B', 'Zona C', 'Zona D']
# Distribución a priori: La Zona A tiene el 70% de las probabilidades
priors = [0.7, 0.1, 0.1, 0.1]

print("Distribución a Priori cargada.")
print(f"La zona con mayor probabilidad inicial es: {zonas[0]}")

# Nota: En una implementación real de GitHub, podrías guardar esto 
# como un diccionario: prior_dict = dict(zip(zonas, priors))

# visualizar_prior(zonas, priors) # Descomentar si se usa en un entorno con GUI
