import numpy as np
from sklearn import svm
from sklearn.datasets import make_circles

# 1. Generar datos que NO son linealmente separables (un círculo dentro de otro)
X, y = make_circles(n_samples=100, factor=0.3, noise=0.05)

# 2. Definir la SVM con el "Truco del Núcleo" RBF
# C: Regularización (qué tanto queremos evitar errores)
# gamma: Define qué tan lejos llega la influencia de un solo ejemplo
modelo_svm = svm.SVC(kernel='rbf', C=1.0, gamma='auto')

# 3. Entrenar el modelo
modelo_svm.fit(X, y)

# 4. Predicción
punto_prueba = np.array([[0, 0]]) # Un punto en el centro del círculo
prediccion = modelo_svm.predict(punto_prueba)

print(f"Resultado de la SVM con Núcleo RBF:")
print(f"  Punto de prueba [0,0] clasificado como clase: {prediccion[0]}")
print(f"  Vectores de soporte encontrados: {len(modelo_svm.support_vectors_)}")
