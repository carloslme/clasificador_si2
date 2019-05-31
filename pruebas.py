import cv2
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.models import Sequential
import numpy as np

# from proyecto.prediccion import prediccion

def predecir(imagen):
    """
        Toma la imagen de entrada y realiza el proceso de predicción
    """
    model = load_model("modelo.keras")
    imagen = cv2.resize(imagen,(128,128))
    imagen = imagen.flatten()
    imagen = np.array(imagen)
    imagenNormalizada = imagen/255
    pruebas = []
    pruebas.append(imagenNormalizada)
    imagenesAPredecir = np.array(pruebas)
    predicciones = model.predict(x = imagenesAPredecir)
    claseMayorValor = np.argmax(predicciones,axis=1)
    return claseMayorValor[0]


categorias = ["Huevos","Arepas","Mantequilla","Chocolate","Pan","Cereales","Cafe","Leche","Tocino","Changua","Tamal","Papas","Calentado","Yuca frita","Jugo naranaja","Yogurth","Pollo"]
imagenPrueba = cv2.imread("uploads/huevos.jpg",0)
cv2.waitKey(0)
indiceCategoria = predecir(imagenPrueba)
print("La imagen cargada pertenece a la categoría: ",categorias[indiceCategoria])
while True:
   cv2.imshow("imagen",imagenPrueba)
   k=cv2.waitKey(30) & 0xff
   if k==27:
       break
cv2.destroyAllWindows()



