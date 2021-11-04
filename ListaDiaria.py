from DTE import DTE

class ListaDiaria():
    def __init__(self, fecha):
        self.fecha = fecha
        self.listaFacturas = []
        self.listaFacturasValidas = []
        self.listaEmisores = []
        self.listaReceptores = []
        self.listaReferencias = []
        self.ReceptoresInvalidos = 0
        self.EmisoresInvalidos = 0
        self.IvaErroneos = 0
        self.TotalesErroneos = 0
        self.referenciasDuplicadas = 0
        self.dia = ''
        self.mes = ''
        self.year = ''
        self.formatoFecha()
     
    def analizar(self):
        print('analizando fecha'+self.fecha)
        for i in self.listaFacturas:
            print(i.nitEmisor)
            facturaInvalida = False
            if i.nitEmisor.endswith('k'):
                existeE = False
                for a in self.listaEmisores:
                    if i.nitEmisor == a:
                        existeE = True
                if existeE != True:
                    self.listaEmisores.append(i.nitEmisor)
            else:
                self.EmisoresInvalidos += 1
                facturaInvalida = True
                continue

            if i.nitReceptor.endswith('k'):
                existeR = False
                for a in self.listaReceptores:
                    if i.nitReceptor == a:
                        existeR = True
                if existeR != True:
                    self.listaReceptores.append(i.nitReceptor)
            else:
                self.ReceptoresInvalidos += 1
                facturaInvalida = True
                continue

            iva = round((i.valor*0.12), 2)
            if iva == i.iva:
                pass
            else:
                self.IvaErroneos += 1
                facturaInvalida = True
                continue
            
            total = round((i.valor+iva),2)
            if total == i.total:
                pass
            else:
                self.TotalesErroneos += 1
                facturaInvalida = True
                continue

            referencia = i.referencia
            repetida = False
            for j in self.listaReferencias:
                if referencia == j:
                    self.referenciasDuplicadas =+ 1
                    facturaInvalida = True
                    repetida = True
                    continue

            if repetida != True:
                self.listaReferencias.append(referencia)
            
            if facturaInvalida != True:
                self.listaFacturasValidas.append(i)

    def agregar(self, DTE):
        self.listaFacturas.append(DTE)

    def getCantidad(self):
        return len(self.listaFacturas)

    def formatoFecha(self):
        banderaMes = False
        banderaYear = False
        buffer = ''
        for  i in self.fecha:
            if banderaMes == False and banderaYear == False:
                if i == '/':
                    self.dia = buffer
                    buffer = ''
                    banderaMes = True
                else:
                    buffer += i
            elif banderaMes == True:
                if i == '/':
                    self.mes = buffer
                    buffer = ''
                    banderaYear = True
                    banderaMes = False
                else:
                    buffer += i
            else:
                buffer += i
        self.year = buffer


