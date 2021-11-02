from DTE import DTE
from ListaDiaria import ListaDiaria
import re

class Analizador():
    def __init__(self):
        self.listaDte = []
    
    def getFecha(self, DTE):
        expresion = '(([0][1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[1-2])\/(0[1-9][1-9][1-9]|1[1-9][1-9][1-9]|2[0][1][1-9]|2[0][2][0-1]))'
        fecha = re.search(expresion, DTE['TIEMPO']).group()
        return fecha

    def getReferencia(self, DTE):
        return DTE['REFERENCIA']
    
    def validarNit(self, NIT):
        suma = 0
        j = 0
        for j in range(len(NIT)-1): 
            suma += int(NIT[j])
            j += 1
        modulo11 = suma%11
        resta = 11 - modulo11
        modulo11 = resta%11

        if modulo11 < 10:
            return True
        else:
            return False
    
    def getValor(self, DTE):
        valor = round(float(DTE['VALOR'], 2))
        return valor
    
    def getIva(self, DTE):
        iva = float(DTE['IVA'])
        return iva
    
    def getTotal(self, DTE):
        total = float(DTE['TOTAL'])
        return total

    def analizar(self, listaDte):
        for i in listaDte:
            #Analis de Fechas
            Fecha = self.getFecha(i)
            #Analisis de Referencia
            Referencia = self.getReferencia(i)
            #Anlisis Nit Emisor
            validacionEmisor= self.validarNit(i['NIT_EMISOR'])
            if validacionEmisor:
                nitEmisor = i['NIT_EMISOR']+'k'
            else:
                nitEmisor = i['NIT_EMISOR']
            #Analisis Nit Receptor
            validacionReceptor = self.validarNit(i['NIT_RECEPTOR'])
            if validacionReceptor:
                nitReceptor = i['NIT_RECEPTOR']+'k'
            else:
                nitReceptor = i['NIT_RECEPTOR']
            #Analisis Valor
            valor = self.getValor(i)
            #Analisis Iva
            iva = self.getIva(i)
            #Analisis Total
            total = self.getTotal(i)
            DTE(Fecha, Referencia, nitEmisor, nitReceptor, valor, iva, total)

            #Verificacion de fecha
            listaDiaria = self.buscar(Fecha)
            if listaDiaria != None:
                listaDiaria.agregar(DTE)
            else:
                newLista = ListaDiaria(Fecha)
                self.listaDte.append(newLista)

        return None
    
    def buscar(self, Fecha):
        listaDiaria = None
        for i in self.listaDte:
            if i.fecha == Fecha:
                listaDiaria = i
            else:
                pass

        return listaDiaria