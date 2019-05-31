#!flask/bin/python
from flask import Flask, jsonify, flash, request, redirect, url_for, send_from_directory, Response
import base64
import os, json
from werkzeug.utils import secure_filename
from os.path import isfile, join
import cv2
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.models import Sequential
import numpy as np
from analisisDeEscena import escena


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg','PNG', 'JPG', 'JPEG'])
RESPUESTA = {}
categorias = ["Huevos","Arepas","Mantequilla","Chocolate","Pan","Cereales","Cafe","Leche","Tocino","Changua","Tamal","Papas","Calentado","Yuca frita","Jugo naranaja","Yogurth","Pollo"]
arrImgCateg = []
arrEscenas = []
respuestaCategorias = {}
escena = escena()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['RESPUESTA'] = RESPUESTA


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def identificarEscena(resultados):
    rutaModelo = "modeloNNA.keras"
    model = load_model(rutaModelo) 
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
                    },
                    "materiales":{
                    }
                }
    for i in range(len(resultados)):
        for j in range(len(categorias)):
            if categorias[j] == resultados[i]:
                conjunto[0][j] = 1
    resultadoEscena = model.predict(conjunto)
    # print('resultadoEscena')
    # print(resultadoEscena)
    aux = 0
    # print(max(max(resultadoEscena)))
    # print(sorted(resultadoEscena[0]))
    for x in range(0,5):
        if resultadoEscena[0][x] == max(max(resultadoEscena)):
            aux = x
    respuesta["probabilidades"]["Paisa"] = str(resultadoEscena[0][0])
    respuesta["probabilidades"]["Cafetero"] = str(resultadoEscena[0][1])
    respuesta["probabilidades"]["Rolo"] = str(resultadoEscena[0][2])
    respuesta["probabilidades"]["Americano"] = str(resultadoEscena[0][3])
    respuesta["probabilidades"]["Light"] = str(resultadoEscena[0][4])
    # print('El valor de x es ' + str(aux))
    # print('El desayuno identificado es: ' + escenas[aux])
    respuesta["escena"] = escenas[aux]
    # print(respuesta["probabilidades"]["Light"])
    return respuesta


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

def analizar(imagen):
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

@app.route('/analizarEscena', methods=['GET'])
def analize_scene():
    # Se añaden todas las imagenes recibidas y guardadas en la carpeta upload a un arreglo
    arr = os.listdir('uploads')
    print ('tamaño arr: ' + str(len(arr)))
    print ('contenido arr: ' + str(arr))
    for item in range(0,len(arr)):
        try:
            img = "uploads/"+arr[item]
            # Se lee la imagen y se convierte a grises
            imagen = cv2.imread(str(img), 0)
            # Se ingresan las imagenes una por una al modelo de CNN para clasificar a que categoria pertenece, 
            indiceCategoria = predecir(imagen)
            print("La imagen cargada pertenece a la categoría: ",categorias[indiceCategoria])
            arrImgCateg.append(categorias[indiceCategoria])

        except Exception as e:
            print(str(e))
    # ress = [
    #             "Cafe",
    #             "Pan",
    #             "Changua",
    #             "Jugo"
    #         ]
    RESPUESTA = identificarEscena(arrImgCateg)
    for i in range(len(arr)):
        print(arrImgCateg[i])
        RESPUESTA["materiales"][str(arr[i])] = str(arrImgCateg[i])

    tam = len(arr)
    for x in range(tam):
        os.remove('uploads/' + str(arr[x]))

    return jsonify(RESPUESTA)

@app.route('/subirImagen', methods=['GET', 'POST'])
def upload_file():
    resp = Response(status=200, mimetype='application/json')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'No tiene la parte de file'
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return 'No se selecciono ninguna imagen'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename + '')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return resp

    return resp
    # '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>
    # '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/allUploads/')
def uploaded_files():
        arr = os.listdir(app.config['UPLOAD_FOLDER'])
        print (arr)
        return jsonify(arr)


@app.route('/remove/<name>', methods=['DELETE'])
def remove_file(name):
        arr = os.listdir(app.config['UPLOAD_FOLDER'])
        print (arr)
        os.remove("uploads/"+name) 
        return 'Borrado exitoso'

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})




if __name__ == '__main__':
    app.run(debug=True)