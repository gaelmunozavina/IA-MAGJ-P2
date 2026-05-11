import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- CORPUS: Nuestra base de datos de documentos ---
documentos = [
    "La inteligencia artificial utiliza redes neuronales para aprender.",
    "El aprendizaje profundo es una rama avanzada de la IA.",
    "Los coches autónomos usan sensores y visión artificial.",
    "La cocina mexicana es famosa por sus tacos y sabores."
]

# 1. Crear el vectorizador TF-IDF
vectorizador = TfidfVectorizer()
tfidf_matrix = vectorizador.fit_transform(documentos)

# 2. Procesar una consulta (Query)
query = "sensores para coches"
query_vec = vectorizador.transform([query])

# 3. Calcular similitud (Coseno) entre la query y todos los documentos
similitudes = cosine_similarity(query_vec, tfidf_matrix).flatten()

# 4. Obtener el resultado más relevante
indice_mejor = np.argmax(similitudes)

print(f"Consulta: '{query}'")
print(f"Documento más relevante: '{documentos[indice_mejor]}'")
print(f"Puntaje de similitud: {similitudes[indice_mejor]:.4f}")
