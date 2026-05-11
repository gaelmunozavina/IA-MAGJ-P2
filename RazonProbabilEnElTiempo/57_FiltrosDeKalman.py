import numpy as np

def filtro_kalman_simple(mediciones, posicion_inicial=0, error_inicial=1):
    # Parámetros del sistema
    posicion_estimada = posicion_inicial
    error_estimado = error_inicial
    
    error_proceso = 0.1  # Qué tanto confiamos en nuestro modelo físico
    error_sensor = 0.5   # Qué tanto ruido tiene el sensor
    
    trayectoria = []

    for z in mediciones:
        # 1. PASO DE PREDICCIÓN
        # En este modelo simple, predecimos que la posición no cambia
        posicion_predicha = posicion_estimada
        error_predicho = error_estimado + error_proceso
        
        # 2. PASO DE ACTUALIZACIÓN (Ganancia de Kalman)
        # K = Error_Predicho / (Error_Predicho + Error_Sensor)
        ganancia_kalman = error_predicho / (error_predicho + error_sensor)
        
        # Corregir la predicción con la nueva medición z
        posicion_estimada = posicion_predicha + ganancia_kalman * (z - posicion_predicha)
        error_estimado = (1 - ganancia_kalman) * error_predicho
        
        trayectoria.append(posicion_estimada)
        
    return trayectoria

# --- ESCENARIO ---
# La posición real es 10, pero el sensor nos da valores con ruido
lecturas_ruidosas = [10.2, 9.8, 10.5, 11.0, 9.5, 10.1, 9.9]
filtrado = filtro_kalman_simple(lecturas_ruidosas)

print("Lecturas del Sensor vs Filtrado de Kalman:")
for r, f in zip(lecturas_ruidosas, filtrado):
    print(f"  Sensor: {r:.2f} -> Estimación Kalman: {f:.4f}")
  
