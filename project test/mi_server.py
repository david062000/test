from flask import Flask
from flask import request
from joblib import load
import pandas as pd

app = Flask(__name__)
 
modelo = load('model_mpl.joblib')# Cargamos el modelo
encoder = load('label_encoder.joblib')# Cargarmo el label encoder

@app.route('/users')
def hello_world(nombre=None):
 
    return("Hola {}!".format(nombre))

@app.route('/predecir', methods=["POST"])
def predecir():
    datos = request.json
    return str(modelo.predict(datos)[0])