# RNA_PE: Red Neuronal Artificial Producto Escena
# Esta red neuronal permite identificar la escena de un desayuno con base en los productos que la integran.
# Paisa = Huevos, Arepas, Mantequilla, Chocolate, Pan
# Paisa Cafetero = Calentado, Cafe, Arepa, Huevos
# Rolo = Changua, Cafe, Pan
# Americano = Cereales, Leche, Huevos, Tocino
# Americano Light = Cereales, Yogurth

# 5 combinaciones
# Paisa = Huevos, Arepas, Mantequilla, Chocolate, Pan
# Paisa Cafetero = Calentado, Cafe, Arepa, Huevos
# Rolo = Changua, Cafe, Pan
# Americano = Cereales, Leche, Huevos, Tocino
# Americano Light = Cereales, Yogurth


import numpy as np
from tensorflow.python.keras.models import model_from_json
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers.core import Dense

# cargamos las 5 combinaciones de los productos
training_data = np.array([[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                          [1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
                          [0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0],
                          [1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0]], "float32")

# cargamos las 5 combinaciones de los productos
training_data_modificado = np.array([
                          [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0],
                          [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
                          [0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0],
                          [0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0],
                          [0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0]], "float32")

training_data_modificado2 = np.array([
                          [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], "float32")

# y estos son los resultados que se obtienen, en el mismo orden
target_data = np.array([[1,0,0,0,0],
                        [0,1,0,0,0],
                        [0,0,1,0,0],
                        [0,0,0,1,0],
                        [0,0,0,0,1]], "float32")


# Creamos una serie de capas de neuronas secuenciales "una delante de la otra"
model = Sequential()

# Se agregan dos capas Dense (en realidad son 3), 16 es la primer capa oculta con 16 neuronas
# e input_dim=17 es la capa de entrada con 17 neuronas, 'relu' es la función de activación
# que da buenos resultados.
model.add(Dense(34, input_dim=17, activation='relu'))

# Se agrega la capa de salida con una neurona con función de activación sigmoid
model.add(Dense(5, activation='sigmoid'))

# Se indica el tipo de pérdida (loss) que se utilizará, el "optimizador" de los pesos de las 
# conexiones de las neuronas y las métricas que se quieren obtener
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

# Se entrena la red
# training_data = entradas, target_data = salidas, epochs = interaciones de aprendizaje
# de entrenamiento
model.fit(training_data, target_data, epochs=1000)

# evaluamos el modelo
scores = model.evaluate(training_data, target_data)

print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print (model.predict(training_data_modificado).round())

name_file = 'modeloNNA.keras' #Debe ser .keras.
model.save(name_file) #Se guarda el archivo en la carpeta raíz.
model.summary() #Se imprime la estructura del archivo, reporte.

# # serializar el modelo a JSON
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
#    json_file.write(model_json)
# # serializar los pesos a HDF5
# model.save_weights("model.h5")
# print("Modelo Guardado!")