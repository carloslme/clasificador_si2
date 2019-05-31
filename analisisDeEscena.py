from tensorflow.python.keras.models import load_model
import numpy as np
import cv2

class escena():
    """
    Carga el modelo de la red neuronal de la ruta especificada
    """
    def __init__(self):
        self.rutaModelo = "modeloNNA.keras"
        self.model = load_model(self.rutaModelo) 

    def predecir(self,resultados):
        conjunto = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], "float32")
        categorias = ["Huevos","Arepas","Mantequilla","Chocolate","Pan","Cereales","Cafe","Leche","Tocino","Changua","Tamal","Papas","Calentado","Yuca frita","Jugo naranaja","Yogurth","Pollo"]
        escenas = ["Paisa","Cafetero","Rolo","Americano","Light"]
        respuesta = {"escena":"",
                     "probabilidades":{
                        "Paisa": 1,     
                        "Cafetero": 2,     
                        "Rolo": 3,     
                        "Americano": 4,     
                        "Light": 5,     
                     }
                    }
        for i in range(len(resultados)):
            for j in range(len(categorias)):
                if categorias[j] == resultados[i]:
                    conjunto[0][j] = 1
        resultadoEscena = self.model.predict(conjunto)
        # print('resultadoEscena')
        # print(resultadoEscena)
        aux = 0
        # print(max(max(resultadoEscena)))
        # print(sorted(resultadoEscena[0]))
        for x in range(0,5):
            if resultadoEscena[0][x] == max(max(resultadoEscena)):
                aux = x
        respuesta["probabilidades"]["Paisa"] = resultadoEscena[0][0]
        respuesta["probabilidades"]["Cafetero"] = resultadoEscena[0][1]
        respuesta["probabilidades"]["Rolo"] = resultadoEscena[0][2]
        respuesta["probabilidades"]["Americano"] = resultadoEscena[0][3]
        respuesta["probabilidades"]["Light"] = resultadoEscena[0][4]
        # print('El valor de x es ' + str(aux))
        # print('El desayuno identificado es: ' + escenas[aux])
        respuesta["escena"] = escenas[aux]
        # print(respuesta["probabilidades"]["Light"])
        return respuesta


# def predecir(conjunto):
#     rutaModelo = "modeloNNA.keras"
#     model = load_model(rutaModelo)
    
#     return model.predict(conjunto).round()

# conjunto = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], "float32")

# categorias = ["Huevos","Arepas","Mantequilla","Chocolate","Pan","Cereales","Cafe","Leche","Tocino","Changua","Tamal","Papas","Calentado","Yuca frita","Jugo naranaja","Yogurth","Pollo"]
# escenas = ["Paisa","Cafetero","Rolo","Americano","Light"]

# resultados = [
#                 "Cafe",
#                 "Pan",
#                 "Changua",
#                 "Jugo"
#             ]
# for i in range(len(resultados)):
#     for j in range(len(categorias)):
#         if categorias[j] == resultados[i]:
#             conjunto[0][j] = 1

# print(conjunto)
# resultadoEscena = predecir(conjunto)
# print('resultadoEscena')
# print(resultadoEscena)
# aux = 0
# for x in range(0,5):
#     if resultadoEscena[0][x] == 1:
#         aux = x
# print('El valor de x es ' + str(aux))
# print('El desayuno identificado es: ' + escenas[aux])

    