from flask import Flask, request, jsonify
from analizador import Analizador
import re
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Rony Omar Miguel  Lopez - 201905750'

@app.route('/data', methods=['POST'])
def data():
    json_file = request.json
    analizador = Analizador() 
    respuesta = analizador.analizar(json_file)

    return jsonify({'status':200})



if __name__ == '__main__':
    app.run(debug=True)