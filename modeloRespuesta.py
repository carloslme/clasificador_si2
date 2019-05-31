import os, json

class Respuesta:
    def __init__(self, escena, probabilidades):
        self.escena = escena
        self.probabilidades = probabilidades 

    def probabilidades(self):
        print("El nombre de la escena es: " + self.escena)
        print(probabilidades)

probabilidades = {"escena":"Paisa", 
                  "probabilidades":[0,1,2,3,4]
                    }
# p1 = Respuesta("Paisa", probabilidades)
# p1.probabilidades()

# # Valor de un atributo
# print(probabilidades["escena"])
# print(probabilidades["probabilidades"])

# # Cambiar valor de un atributo
# probabilidades["escena"] = "Rolo"
# print(probabilidades["escena"])

# # Nombres de atributos
# for x in probabilidades:
#     print(x)

# # Valores
# for y in probabilidades:
#     print(probabilidades[y])
# for x in probabilidades.values():
#       print(x)

# # Atributos y valores
# for x, y in probabilidades.items():
#       print(x, y)

arrr = os.listdir('uploads')
print(arrr)
print(str(len(arrr)))
# arr = {
#     "escena": "Light",
#     "probabilidades": {
#         "Americano": "0.007252557",
#         "Cafetero": "0.027723735",
#         "Light": "0.28939617",
#         "Paisa": "0.071908794",
#         "Rolo": "0.13047332"
#     },
#     "materiales":{
#     }
# }
# print(arr)
# arrImgCateg = ['Cereales', 'Mantequilla', 'Cafe', 'Mantequilla']

# for i in range(len(arrr)):
#     print(arrImgCateg[i])
#     arr["materiales"][str(arrr[i])] = str(arrImgCateg[i])

# print('NUEVO::::::::::::::::')
# print(arr)

tam = len(arrr)
for x in range(tam):
    os.remove('uploads/' + str(arrr[x]))
print(arrr)