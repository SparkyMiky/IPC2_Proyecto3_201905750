from DTE import DTE
from ListaDiaria import ListaDiaria
import re

class Analizador():
    def __init__(self):
        self.listaDte = []
        self.facturasRecibidas = 0
    
    def getFecha(self, DTE):
        expresion = '(([0][1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[1-2])\/(0[1-9][1-9][1-9]|1[1-9][1-9][1-9]|2[0][1][1-9]|2[0][2][0-1]))'
        fecha = re.search(expresion, DTE['TIEMPO']).group()
        return fecha

    def getReferencia(self, DTE):
        return DTE['REFERENCIA']
    
    def validarNit(self, NIT):
        suma = 0
        j = 0
        modulo11 = 11
        try:
            for j in range(len(NIT)-1): 
                suma += int(NIT[j])
                j += 1
            modulo11 = suma%11
            resta = 11 - modulo11
            modulo11 = resta%11
        except Exception as e:
            pass

        if modulo11 < 10:
            return True
        else:
            return False
    
    def getValor(self, DTE):
        valor = round(float(DTE['VALOR']),2)
        return valor
    
    def getIva(self, DTE):
        iva = round(float(DTE['IVA']),2)
        return iva
    
    def getTotal(self, DTE):
        total = round(float(DTE['TOTAL']),2)
        return total

    def analizar(self, listaDte):
        self.facturasRecibidas = len(listaDte)
        for i in listaDte:
            try:
                #Analis de Fechas
                Fecha = self.getFecha(i)
                #Analisis de Referencia
                Referencia = self.getReferencia(i)
                #Anlisis Nit Emisor
                validacionEmisor= self.validarNit(i['NIT_EMISOR'])
                if validacionEmisor:
                    nitEmisor = i['NIT_EMISOR']+'k'
                else:
                    print('Error Emisor')
                    nitEmisor = i['NIT_EMISOR']
                #Analisis Nit Receptor
                validacionReceptor = self.validarNit(i['NIT_RECEPTOR'])
                if validacionReceptor:
                    nitReceptor = i['NIT_RECEPTOR']+'k'
                else:
                    print('Error Receptor')
                    nitReceptor = i['NIT_RECEPTOR']
                #Analisis Valor
                valor = self.getValor(i)
                #Analisis Iva
                iva = self.getIva(i)
                #Analisis Total
                total = self.getTotal(i)
                dte = DTE(Fecha, Referencia, nitEmisor, nitReceptor, valor, iva, total)

                #Verificacion de fecha
                listaDiaria = self.buscar(Fecha)
                if listaDiaria != None:
                    listaDiaria.agregar(dte)
                else:
                    newLista = ListaDiaria(Fecha)
                    newLista.agregar(dte)
                    self.listaDte.append(newLista)
            except Exception as e:
                print(e)
        return None
    
    def buscar(self, Fecha):
        listaDiaria = None
        for i in self.listaDte:
            if i.fecha == Fecha:
                listaDiaria = i
            else:
                pass

        return listaDiaria

    def crearXML(self):
        inicio = '<LISTAAUTORIZACIONES>\n'
        for i in self.listaDte:
            year = int(i.year)*1000000000000
            month = int(i.mes)*10000000000
            day = int(i.dia)*100000000
            codigoAprobacion = year+month+day
            try:
                i.analizar()
            except Exception as e:
                print(e)
            inicio += '\t<AUTORIZACION>\n'
            inicio += '\t\t<FECHA> '+i.fecha+' </FECHA>\n'
            inicio += '\t\t<FACTURAS_RECIBIDAS> '+str(len(i.listaFacturas))+' </FACTURAS_RECIBIDAS>\n'
            inicio += '\t\t<ERRORES>\n'
            inicio += '\t\t\t<NIT_EMISOR> '+str(i.EmisoresInvalidos)+' </NIT_EMISOR>\n'
            inicio += '\t\t\t<NIT_RECEPTOR> '+str(i.ReceptoresInvalidos)+' </NIT_RECEPTOR>\n'
            inicio += '\t\t\t<IVA> '+str(i.IvaErroneos)+' </IVA>\n'
            inicio += '\t\t\t<TOTAL> '+str(i.TotalesErroneos)+' </TOTAL>\n'
            inicio += '\t\t\t<REFERENCIA_DUPLICADA> '+str(i.referenciasDuplicadas)+' </REFERENCIA>\n'
            inicio += '\t\t</ERRORES>\n'
            inicio += '\t\t<FACTURAS_CORRECTAS> '+str(len(i.listaFacturasValidas))+' </FACTURAS_CORRECTAS>\n'
            inicio += '\t\t<CANTIDAD_EMISORES> '+str(len(i.listaEmisores))+' </CANTIDAD_EMISORES>\n'
            inicio += '\t\t<CANTIDAD_RECEPTORES> '+str(len(i.listaReceptores))+' </CANTIDAD_RECEPTORES>\n'
            inicio += '\t\t<LISTADO_AUTORIZACIONES>\n'
            for j in i.listaFacturasValidas:
                codigoAprobacion += 1
                inicio += '\t\t\t<APROBACION>\n'
                inicio += '\t\t\t\t<NIT_EMISOR ref='+j.referencia+'> '+j.nitEmisor+' </NIT_EMISOR>\n'
                inicio += '\t\t\t\t<CODIGO_APROBACION> '+str(codigoAprobacion)+' </CODIGO_APROBACION>\n'
                inicio += '\t\t\t<\APROBACION>\n'
            inicio += '\t\t</LISTADO_AUTORIZACIONES>\n'
            inicio += '\t</AUTORIZACION>\n'
        inicio += '</LISTAAUTORIZACIONES>'
        archivo = open('autorizaciones.xml', 'w')
        archivo.write(inicio)
        archivo.close()
