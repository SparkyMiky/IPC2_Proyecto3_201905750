from flask import Flask, request, jsonify, Response
from flask_cors import CORS

from analizador import Analizador
import xmltodict
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*":{"origin":"*"}})
datos = ''

@app.route('/', methods=['GET'])
def index():
    return Response(status=204, content_type="hola esto es una respuesta")

@app.route('/data', methods=['GET'])
def data():
    global datos
    respuesta = datos
    return Response(status=200,
                    response = respuesta,
                    content_type='text/plain')
    

@app.route('/appClient', methods=['GET'])
def getDatos():
    save_file = open('autorizaciones.xml', 'r+')
    respuesta = save_file.read()
    save_file.close()
    return Response(status=200,
                    response = respuesta,
                    content_type='text/plain')

@app.route('/appClient', methods=['POST'])
def postDatos():
    json_file = request.data.decode('utf-8')
    global datos 
    datos = json_file
    xml = xmltodict.parse(json_file)
    res = json.dumps(xml)
    res1 = json.loads(res)
    analizador = Analizador()
    analizador.analizar(res1['SOLICITUD_AUTORIZACION']['DTE']) 
    analizador.crearXML()
    return Response(status=204)



if __name__ == '__main__':
    app.run(debug=True)