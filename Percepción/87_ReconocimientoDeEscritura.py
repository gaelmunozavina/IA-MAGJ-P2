import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Cargar el dataset MNIST (Dígitos escritos a mano 0-9)
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. Preprocesado: Normalizar los píxeles (0-255 a 0-1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. Crear una Red Neuronal Simple (MLP)
modelo = models.Sequential([
    layers.Flatten(input_shape=(28, 28)), # Convertir matriz 28x28 a vector de 784
    layers.Dense(128, activation='relu'), # Capa oculta
    layers.Dropout(0.2),                  # Evitar sobreajuste
    layers.Dense(10, activation='softmax')# 10 salidas (una por cada dígito)
])

# 4. Compilar y entrenar
modelo.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("Entrenando modelo de reconocimiento de dígitos...")
modelo.fit(x_train, y_train, epochs=3, verbose=1)

# 5. Evaluar
perdida, precision = modelo.evaluate(x_test, y_test, verbose=0)
print(f"\nPrecisión en datos nuevos: {precision:.2%}")
