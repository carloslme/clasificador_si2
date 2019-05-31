#!flask/bin/python
from flask import Flask, jsonify, flash, request, redirect, url_for, send_from_directory, Response
import base64
import os, json
from werkzeug.utils import secure_filename
from os.path import isfile, join
import cv2
from analisisDeEscena import escena
import json

# # Se añaden todas las imagenes recibidas y guardadas en la carpeta upload a un arreglo
# arr = os.listdir('uploads')
# print ('tamaño arr: ' + str(len(arr)))
# print ('contenido arr: ' + str(arr))
# for item in range(0,len(arr)):
#     try:
#         img = "uploads/"+arr[item]
#         # Imagenes a grises
#         imagen = cv2.imread(str(img), cv2.IMREAD_GRAYSCALE)
#         cv2.imshow("prueba", imagen)
#         cv2.waitKey(0)
#         width = 128
#         height = 128
#         dim = (width, height)
#         # Redimensionar imagen
#         resized = cv2.resize(imagen, dim, interpolation = cv2.INTER_AREA)
#         # Guardar imagen
#         newname = "uploads/"+str(arr[item])
#         cv2.imwrite(newname, resized)
#         print ('img convertida: ' + str(img))
#         cv2.waitKey(0)
#     except Exception as e:
#         print(str(e))


# Pruebas prediccion ANN
escena = escena()
resultados = [
                "Cafe",
                "Pan",
                "Changua",
                "Jugo"
            ]
resAnalisis = escena.predecir(resultados)
print(resAnalisis)
