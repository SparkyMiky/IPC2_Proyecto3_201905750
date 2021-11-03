from flask import Flask, request, jsonify, Response
from flask_cors import CORS

from analizador import Analizador
import xmltodict
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*":{"origin":"*"}})

@app.route('/', methods=['GET'])
def index():
    return Response(status=204, content_type="hola esto es una respuesta")

@app.route('/data', methods=['POST'])
def data():
    json_file = request.data.decode('utf-8')
    xml = xmltodict.parse(json_file)
    res = json.dumps(xml)
    print(json_file)
    print('\n*****************************\n')
    print(res)
    #analizador = Analizador() 
    #respuesta = analizador.analizar(json_file)

@app.route('/appClient', methods=['GET'])
def getDatos():
    save_file = open('save_file.txt', 'r+')
    respuesta = save_file.read()
    save_file.close()
    return Response(status=200,
                    response = respuesta,
                    content_type='text/plain')

@app.route('/appClient', methods=['POST'])
def postDatos():
    json_file = request.data.decode('utf-8')
    xml = xmltodict.parse(json_file)
    res = json.dumps(xml)
    res1 = json.loads(res)
    analizador = Analizador()
    analizador.analizar(res1['SOLICITUD_AUTORIZACION']['DTE']) 

    #Escritura de archivo
    strFile = request.data.decode('utf-8')
    save_file = open('save_file.txt','w+')
    save_file.write(strFile)
    save_file.close()
    return Response(status=204)



if __name__ == '__main__':
    app.run(debug=True)