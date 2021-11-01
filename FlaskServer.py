from flask import Flask, request,jsonify
import re
import xmltodict
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Rony Omar Miguel  Lopez - 201905750'

@app.route('/data', methods=['POST'])
def data():
    json_file = request.json
    print(type(json_file[0]))
    print('buscando fecha')
    print(json_file[0]['TIEMPO'])
    expresion = '(([0][1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[1-2])\/(0[1-9][1-9][1-9]|1[1-9][1-9][1-9]|2[0][1][1-9]|2[0][2][0-1]))'
    coincidencias = []
    for i in json_file:
        coincidencias.append(re.search(expresion, i['TIEMPO']).group())
        nitEmisor = i['NIT_EMISOR']
        suma = 0
        for j in range(len(nitEmisor)-1):
            suma += int(nitEmisor[j])
            j += 1
        modulo11 = suma%11
        resta = 11 - modulo11
        modulo11 = resta%11

        if modulo11 < 10:
            print(nitEmisor+'k')
        else:
            print(nitEmisor+' no es valido')

        
    print(coincidencias)

    return jsonify({'status':200})



if __name__ == '__main__':
    app.run(debug=True)