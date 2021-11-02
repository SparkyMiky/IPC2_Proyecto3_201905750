from DTE import DTE

class ListaDiaria():
    def __init__(self, fecha):
        self.fecha = fecha
        self.listaFacturas = []
        self.listaEmisores = []
        self.listaReceptores = []
        self.ReceptoresInvalidos = 0
        self.EmisoresInvalidos = 0
        self.IvaErroneos = 0
        self.TotalesErroneos = 0
        self.referenciasDuplicadas = 0

    def getErrores(self):
        for i in self.listaFacturas:
           pass
        return
     


    def agregar(self, DTE):
        self.listaFacturas.append(DTE)


    def getCantidad(self):
        return len(self.listaFacturas)
    
